STORY_PLANNING_PROMPT = """
Generate a story outline in the style of One Thousand and One Nights with the following elements:
- A clear moral lesson
- Rich character development
- Magical or supernatural elements
- Cultural authenticity
- Classical Arabic narrative style

Story Theme: {theme}
Required Elements: {elements}
Length: {length}

Output the story structure in the following format:
1. Opening Scene
2. Character Introduction
3. Conflict Development
4. Plot Twists
5. Resolution
6. Moral Lesson
"""

CHARACTER_GENERATION_PROMPT = """
Create a character for an Arabic narrative in the style of One Thousand and One Nights:
Context: {context}
Character Type: {character_type}
Role in Story: {role}

Include:
1. Name and title
2. Physical description
3. Personality traits
4. Background story
5. Motivations
6. Speech patterns

SETTING_GENERATION_PROMPT = """
Create a vivid setting for an Arabic narrative in the classical style:
Time Period: {period}
Location Type: {location}
Atmosphere: {atmosphere}

Include:
1. Sensory details
2. Cultural elements
3. Historical authenticity
4. Magical elements (if applicable)
"""
