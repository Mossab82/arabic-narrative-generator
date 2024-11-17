```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from typing import Dict, Any

class StoryGenerator:
    def __init__(self, model_name: str = "aubmindlab/arabert-base"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)

    def generate(self, prompt: str, max_length: int = 1000) -> Dict[str, Any]:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
       
        outputs = self.model.generate(
            **inputs,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )

        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
       
        return {
            'prompt': prompt,
            'generated_text': generated_text,
            'metadata': {
                'model_name': self.model.config.name_or_path,
                'parameters': {
                    'max_length': max_length,
                    'temperature': 0.7,
                    'top_k': 50,
                    'top_p': 0.95
                }
            }
        }
