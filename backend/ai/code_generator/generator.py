import os
import requests
import logging
from typing import Dict, Optional
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class CodeGenerator:
    def __init__(self):
        self.api_url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
        self.headers = {"Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}"}
        self.logger = self._setup_logger()
        self.templates_path = Path(__file__).parent / "templates"

    def _setup_logger(self):
        logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))
        return logging.getLogger(__name__)

    def _load_template(self, template_name: str) -> str:
        with open(self.templates_path / f"{template_name}.txt", "r") as f:
            return f.read()

    def generate(self, prompt: str, context: Optional[Dict] = None, template: str = "base_prompt") -> str:
        template = self._load_template(template)
        full_prompt = template.format(prompt=prompt, context=context or {})
        
        response = requests.post(
            self.api_url,
            headers=self.headers,
            json={
                "inputs": full_prompt,
                "parameters": {
                    "max_new_tokens": int(os.getenv('MAX_TOKENS', 1500)),
                    "temperature": 0.3,
                    "do_sample": True
                }
            }
        )
        response.raise_for_status()
        return self._clean_output(response.json()[0]['generated_text'])

    def _clean_output(self, raw_code: str) -> str:
        if "```python" in raw_code:
            return raw_code.split("```python")[1].split("```")[0].strip()
        return raw_code

    def generate_file(self, prompt: str, output_path: str, **kwargs):
        code = self.generate(prompt, **kwargs)
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(code)
        self.logger.info(f"File generato: {output_path}")
        return output_path
