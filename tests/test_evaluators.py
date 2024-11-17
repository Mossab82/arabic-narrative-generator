```python
import pytest
from src.evaluators.story_evaluator import StoryEvaluator

@pytest.fixture
def evaluator():
    return StoryEvaluator()

def test_story_evaluation(evaluator):
    test_story = {
        'text': 'قال شهريار لشهرزاد: حدثيني حديثاً',
        'metadata': {'genre': 'fantasy'}
    }
   
    results = evaluator.evaluate(test_story)
   
    assert isinstance(results, dict)
    assert 'coherence' in results
    assert 'grammar' in results
    assert 'style' in results
    assert 'cultural' in results
   
    for score in results.values():
        assert 0 <= score <= 1
