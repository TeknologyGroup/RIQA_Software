import json
from pathlib import Path
from datetime import datetime

class FileManager:
    @staticmethod
    def save_code(path: str, content: str):
        Path(path).write_text(content)
    
    @staticmethod
    def save_metadata(prompt: str, generated_code: str):
        log_dir = Path("generation_logs")
        log_dir.mkdir(exist_ok=True)
        
        metadata = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "code": generated_code
        }
        
        filename = f"gen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        (log_dir / filename).write_text(json.dumps(metadata, indent=2))
