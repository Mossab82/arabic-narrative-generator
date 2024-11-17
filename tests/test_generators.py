```python
import pytest
from src.generators.story_generator import StoryGenerator

@pytest.fixture
def generator():
    return StoryGenerator()

def test_story_generation(generator):
    prompt = "في قديم الزمان"
    result = generator.generate(prompt, max_length=100)
   
    assert isinstance(result, dict)
    assert 'prompt' in result
    assert 'generated_text' in result
    assert 'metadata' in result
    assert len(result['generated_text']) > len(prompt)
    assert prompt in result['generated_text']

def test_generation_parameters(generator):
    result = generator.generate("كان يا ما كان", max_length=50)
    assert len(result['generated_text'].split()) < 100
    assert isinstance(result['metadata']['parameters'], dict)
