from flask import Flask, request, render_template
from knowledge_base import generate_story, STORY_TEMPLATES, CHARACTERS
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

GENRES = list(STORY_TEMPLATES.keys())

@app.route('/')
def index():
    return render_template('index.html', genres=GENRES, characters=CHARACTERS)

@app.route('/generate_story', methods=['POST'])
def generate_story_endpoint():
    data = request.json
    logger.debug(f"Received request data: {data}")
    
    custom_prompt = data.get('custom_prompt')
    genre = data.get('genre')
    selected_characters = data.get('characters', [])
    
    try:
        story = generate_story(custom_prompt=custom_prompt, genre=genre, characters=selected_characters)
        logger.debug("Story generated successfully")
        return {"response": story}
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        return {"error": str(e)}, 400
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {"error": f"Failed to generate story: {str(e)}"}, 500

if __name__ == '__main__':
    app.run(debug=True)