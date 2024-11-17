from typing import Dict, List
from ..models.rule_engine import RuleEngine
from ..models.llm_wrapper import LLMGenerator
from ..config.config import CONFIG
from ..utils.validation import validate_story_structure

class StoryPlanner:
    def __init__(self):
        self.rule_engine = RuleEngine()
        self.llm_generator = LLMGenerator()
        
    def generate_plot(self, theme: str, length: int) -> Dict:
        """Generate a complete story plot combining rule-based and LLM approaches."""
        # Get base structure from rules
        base_structure = self.rule_engine.get_narrative_structure()
        
        # Enhance with LLM
        llm_plot = self.llm_generator.enhance_plot(
            base_structure,
            theme=theme,
            length=length
        )
        
        # Validate the enhanced plot
        validated_plot = validate_story_structure(llm_plot)
        
        return validated_plot
    
    def plan_narrative_elements(self, plot: Dict) -> Dict:
        """Plan specific narrative elements based on the plot."""
        elements = {
            'characters': self._plan_characters(plot),
            'settings': self._plan_settings(plot),
            'events': self._plan_events(plot)
        }
        return elements
    
    def _plan_characters(self, plot: Dict) -> List[Dict]:
        """Plan character arcs and relationships."""
        character_templates = self.rule_engine.get_character_templates()
        characters = self.llm_generator.create_characters(
            plot,
            character_templates
        )
        return characters
    
    def _plan_settings(self, plot: Dict) -> List[Dict]:
        """Plan story settings and environments."""
        setting_rules = self.rule_engine.get_setting_rules()
        settings = self.llm_generator.create_settings(
            plot,
            setting_rules
        )
        return settings
    
    def _plan_events(self, plot: Dict) -> List[Dict]:
        """Plan sequence of events."""
        event_patterns = self.rule_engine.get_event_patterns()
        events = self.llm_generator.sequence_events(
            plot,
            event_patterns
        )
        return events
