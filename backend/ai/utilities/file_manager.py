import json
import os

class FileManager:
    def save_generation_log(self, prompt: str, generated_code: str, timestamp: str):
        log_entry = {
            'timestamp': timestamp,
            'prompt': prompt,
            'code': generated_code
        }
        os.makedirs('logs', exist_ok=True)
        with open(f'logs/generation_{timestamp}.json', 'w') as f:
            json.dump(log_entry, f)
