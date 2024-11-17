# arabic-narrative-generator
A Hybrid Rule-Based and Machine Learning System for Generating Arabic Narrative Stories Inspired by One Thousand and One Nights
# Arabic Narrative Generation System

A hybrid system combining Large Language Models with rule-based approaches for generating Arabic narratives inspired by One Thousand and One Nights.

## Features
- Story planning with classical Arabic narrative structures
- Character and setting generation
- LLM-enhanced narrative generation
- Classical Arabic style processing
- Cultural authenticity validation

## Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables:
   ```bash
   export OPENAI_API_KEY=your-api-key
   ```

## Usage
```python
from src.core.story_planner import StoryPlanner
from src.core.narrative_generator import NarrativeGenerator

# Initialize components
planner = StoryPlanner()
generator = NarrativeGenerator()

# Generate a story
plot = planner.generate_plot(
    theme="wisdom and patience",
    length=3000
)

elements = planner.plan_narrative_elements(plot)
narrative = generator.generate_narrative(plot, elements)

print(narrative)
