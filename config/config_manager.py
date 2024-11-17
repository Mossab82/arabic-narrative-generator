```python
import yaml
from pathlib import Path
from typing import Dict, Any

class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.config_path = Path(__file__).parent.parent.parent / 'config'
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        with open(self.config_path / 'default_config.yaml', 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, default)
            if value is None:
                return default
        return value
