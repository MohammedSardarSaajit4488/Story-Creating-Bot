import random

# Define characters
CHARACTERS = ["Zira", "Abshi", "Kamini"]

# Story templates for each genre
STORY_TEMPLATES = {
    "horror": {
        "beginning": [
            "{chars} ventured into the dark, abandoned mansion, the wind howling through broken windows.",
            "Late at night, {chars} stumbled upon a foggy graveyard, shadows moving in the mist."
        ],
        "middle": [
            "A chilling scream echoed as {chars} discovered an old, blood-stained journal.",
            "The floor creaked under {chars} as glowing eyes appeared in the darkness."
        ],
        "end": [
            "{chars} fled, hearts pounding, vowing never to return to that cursed place.",
            "In the end, {chars} escaped, but the whispers followed them into the night."
        ]
    },
    "isekai": {
        "beginning": [
            "{chars} tripped and fell through a glowing portal, landing in a strange, magical land.",
            "After a blinding light, {chars} awoke in a forest, surrounded by unfamiliar creatures."
        ],
        "middle": [
            "{chars} met a wise elf who revealed they were chosen to save this world.",
            "A dragon challenged {chars}, testing their courage in this new realm."
        ],
        "end": [
            "{chars} mastered their powers and decided to stay in this fantastical world.",
            "With a tearful goodbye, {chars} returned home, forever changed."
        ]
    },
    "robots": {
        "beginning": [
            "{chars} activated an ancient robot in a dusty lab, its lights flickering to life.",
            "In a futuristic city, {chars} found a rogue android hiding among the crowd."
        ],
        "middle": [
            "{chars} teamed up with the robot to stop a malfunctioning AI overlord.",
            "Sparks flew as {chars} battled a swarm of drones sent by a robotic tyrant."
        ],
        "end": [
            "{chars} reprogrammed the robots, bringing peace to the metallic city.",
            "In the end, {chars} and their robot ally flew off into the neon sunset."
        ]
    }
}

def generate_story(custom_prompt=None, genre=None, characters=None):
    """Generate a story based on custom prompt or genre/character selection."""
    if custom_prompt:
        # Extract characters from custom prompt if present, else use provided characters or random
        chars = characters if characters else []
        for char in CHARACTERS:
            if char.lower() in custom_prompt.lower() and char not in chars:
                chars.append(char)
        if not chars:
            chars = [random.choice(CHARACTERS)]
        chars_str = ", ".join(chars)
        
        # Use genre from prompt if detectable, else default to a random one
        detected_genre = next((g for g in STORY_TEMPLATES if g in custom_prompt.lower()), random.choice(list(STORY_TEMPLATES.keys())))
        templates = STORY_TEMPLATES[detected_genre]
        
        beginning = random.choice(templates["beginning"]).format(chars=chars_str)
        middle = random.choice(templates["middle"]).format(chars=chars_str)
        end = random.choice(templates["end"]).format(chars=chars_str)
        
        filler = " ".join([
            f"The scene was set as {chars_str} moved cautiously, hearts racing with anticipation.",
            "Every sound amplified their curiosity, pushing them deeper into the unknown.",
            "Their bond grew stronger with each challenge, a testament to their resilience."
        ])
        # Return only the story, without the prompt
        story = f"{beginning}\n\n{filler}\n\n{middle}\n\n{end}"
    else:
        if not genre or genre not in STORY_TEMPLATES:
            raise ValueError("Invalid genre.")
        if not characters or len(characters) > 3:
            raise ValueError("Must select 1 to 3 characters.")
        
        chars_str = ", ".join(characters)
        templates = STORY_TEMPLATES[genre]
        beginning = random.choice(templates["beginning"]).format(chars=chars_str)
        middle = random.choice(templates["middle"]).format(chars=chars_str)
        end = random.choice(templates["end"]).format(chars=chars_str)
        
        filler = " ".join([
            "The air was thick with tension as they moved forward, each step echoing in the silence.",
            f"{chars_str} exchanged glances, unsure of what lay ahead but determined to press on.",
            "Time seemed to slow, every moment stretching into eternity as the story unfolded.",
            "Their journey was fraught with peril, yet hope flickered like a distant star.",
            "In that moment, they realized the true strength within them, a bond unbreakable."
        ])
        story = f"{beginning}\n\n{filler}\n\n{middle}\n\n{end}"
    
    return story

if __name__ == "__main__":
    print(generate_story(custom_prompt="Write a horror story with Zira and Abshi"))