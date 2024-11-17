```python
import asyncio
from typing import Dict, Any
from .collectors import WikiSourceCollector, ArchiveOrgCollector
from .processors import TextProcessor
from .generators import StoryGenerator
from .evaluators import StoryEvaluator
from .config import ConfigManager

class Pipeline:
    def __init__(self):
        self.config = ConfigManager()
        self.processor = TextProcessor()
        self.generator = StoryGenerator()
        self.evaluator = StoryEvaluator()

    async def run(self, prompt: str) -> Dict[str, Any]:
        # Generate story
        generation_result = self.generator.generate(
            prompt,
            max_length=self.config.get('processing.max_story_length')
        )
       
        # Process generated text
        processed_result = self.processor.process(
            generation_result['generated_text']
        )
       
        # Evaluate results
        evaluation_result = self.evaluator.evaluate({
            'text': processed_result['cleaned'],
            'metadata': generation_result['metadata']
        })
       
        return {
            'original_prompt': prompt,
            'generated_story': generation_result['generated_text'],
            'processed_story': processed_result['cleaned'],
            'evaluation_scores': evaluation_result,
            'metadata': generation_result['metadata']
        }

    async def collect_training_data(self):
        collectors = [WikiSourceCollector(), ArchiveOrgCollector()]
        results = []
       
        for collector in collectors:
            async with collector as c:
                results.extend(await c.collect())
       
        return results
