from typing import Dict, List
from ..models.llm_wrapper import LLMGenerator
from ..utils.arabic_utils import ArabicTextProcessor
from ..config.config import CONFIG

class NarrativeGenerator:
    def __init__(self):
        self.llm_generator = LLMGenerator()
        self.text_processor = ArabicTextProcessor()
        
    def generate_narrative(self, plot: Dict, elements: Dict) -> str:
        """Generate the complete narrative text."""
        # Generate initial narrative
        narrative = self._generate_base_narrative(plot, elements)
        
        # Enhance with literary elements
        narrative = self._add_literary_elements(narrative)
        
        # Apply classical Arabic style
        narrative = self._apply_classical_style(narrative)
        
        return narrative
    
    def _generate_base_narrative(self, plot: Dict, elements: Dict) -> str:
        """Generate the base narrative structure."""
        narrative_sections = []
        
        # Generate opening
        opening = self.llm_generator.generate_opening(
            plot['opening'],
            elements['settings'][0]
        )
        narrative_sections.append(opening)
        
        # Generate main story sections
        for event in elements['events']:
            section = self.llm_generator.generate_section(
                event,
                elements['characters'],
                elements['settings']
            )
            narrative_sections.append(section)
        
        # Generate closing
        closing = self.llm_generator.generate_closing(
            plot['closing'],
            elements['characters']
        )
        narrative_sections.append(closing)
        
        return "\n\n".join(narrative_sections)
    
    def _add_literary_elements(self, narrative: str) -> str:
        """Add classical Arabic literary devices."""
        enhanced = narrative
        
        # Add metaphors and similes
        enhanced = self.llm_generator.add_literary_devices(enhanced)
        
        # Add poetic elements
        enhanced = self.llm_generator.add_poetic_elements(enhanced)
        
        return enhanced
    
    def _apply_classical_style(self, narrative: str) -> str:
        """Apply classical Arabic narrative style."""
        styled = self.text_processor.apply_classical_style(narrative)
        styled = self.text_processor.add_traditional_markers(styled)
        return styled
