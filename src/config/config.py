from dataclasses import dataclass
from typing import List, Dict

@dataclass
class LLMConfig:
    model_name: str = "gpt-4"  # or your preferred Arabic-capable model
    temperature: float = 0.7
    max_tokens: int = 2000
    presence_penalty: float = 0.6
    frequency_penalty: float = 0.6

@dataclass
class StoryConfig:
    min_length: int = 1000
    max_length: int = 5000
    allowed_genres: List[str] = ("fantasy", "adventure", "moral_tale")
    required_elements: List[str] = ("moral_lesson", "character_growth", "plot_twist")

CONFIG = {
    "llm": LLMConfig(),
    "story": StoryConfig(),
    "arabic": {
        "dialect": "classical",
        "style_markers": ["قال", "كان يا ما كان", "وفي يوم من الأيام"],
        "ending_phrases": ["وعاشوا في سعادة وهناء", "وهكذا انتهت حكايتنا"]
    }
}
