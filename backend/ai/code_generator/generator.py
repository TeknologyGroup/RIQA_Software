import os
import logging
from datetime import datetime
from typing import Optional, Dict
from ai.utilities.file_manager import FileManager

class CodeGenerator:
    def __init__(self):
        self.file_manager = FileManager()
        self.logger = self._setup_logger()
        self.templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
        
    def _setup_logger(self):
        """Configura il sistema di logging"""
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger(__name__)
    
    def generate(self, prompt: str, context: Optional[Dict] = None) -> str:
        """
        Genera codice basato sul prompt e contesto forniti
        
        Args:
            prompt: Descrizione testuale della funzionalità richiesta
            context: Dizionario con variabili di contesto aggiuntive
        
        Returns:
            Codice generato come stringa
        """
        try:
            self.logger.info(f"Generating code for prompt: {prompt[:50]}...")
            
            # 1. Pre-processamento
            clean_prompt = self._preprocess_prompt(prompt)
            
            # 2. Generazione del codice (implementa la tua logica qui)
            generated_code = self._generate_from_prompt(clean_prompt, context or {})
            
            # 3. Salvataggio e log
            self.file_manager.save_generation_log(
                prompt=prompt,
                generated_code=generated_code,
                timestamp=datetime.now().isoformat()
            )
            
            return generated_code
            
        except Exception as e:
            self.logger.error(f"Generation failed: {str(e)}")
            raise RuntimeError(f"Code generation error: {str(e)}")

    def _preprocess_prompt(self, prompt: str) -> str:
        """Pulisce e normalizza il prompt di input"""
        return prompt.strip().replace('\t', ' ' * 4)

    def _generate_from_prompt(self, prompt: str, context: Dict) -> str:
        """
        Implementazione core della generazione del codice.
        Sostituisci con la tua logica effettiva (es: modello AI, template system, ecc.)
        """
        # Esempio base - sostituire con la tua implementazione reale
        code_template = f"""
# Generated at {datetime.now().isoformat()}
# Prompt: {prompt}

def generated_function():
    \"\"\"Funzione generata automaticamente\"\"\"
    print("Hello from generated code!")
    return 42
        """
        return code_template.strip()

    def batch_generate(self, prompts: list) -> dict:
        """Genera codice per multipli prompts"""
        return {prompt: self.generate(prompt) for prompt in prompts}
