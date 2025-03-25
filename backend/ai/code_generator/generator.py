import os
import requests
import logging
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()  # Carica le variabili d'ambiente

class CodeGenerator:
    def __init__(self):
        self.api_url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}",
            "Content-Type": "application/json"
        }
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger(__name__)

    def _generate_from_prompt(self, prompt: str, context: Optional[Dict] = None) -> str:
        """Genera codice usando l'API di HuggingFace"""
        try:
            instruction = ("Crea un file Python completo basato sulla seguente descrizione. "
                         "Includi tutti gli import necessari e docstring. "
                         "Restituisci SOLO il codice, senza commenti aggiuntivi.")
            
            full_prompt = f"""<s>[INST] {instruction}
Descrizione: {prompt}
Contesto: {context or {}}
[/INST]```python\n"""
            
            payload = {
                "inputs": full_prompt,
                "parameters": {
                    "max_new_tokens": 1000,
                    "temperature": 0.2,
                    "do_sample": True,
                    "return_full_text": False
                }
            }
            
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            generated_code = response.json()[0]['generated_text']
            # Pulizia del risultato
            return generated_code.split("```python\n")[-1].split("```")[0].strip()
            
        except Exception as e:
            self.logger.error(f"Errore nella generazione: {str(e)}")
            raise RuntimeError(f"Generazione fallita: {str(e)}")

    def generate_file(self, prompt: str, output_path: str, context: Optional[Dict] = None):
        """Genera e salva direttamente un file Python"""
        code = self.generate(prompt, context)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(code)
        self.logger.info(f"File generato: {output_path}")
        return output_path

params = {
    "max_new_tokens": 1500,  # Lunghezza massima del codice
    "temperature": 0.3,      # 0 (deterministico) - 1 (creativo)
    "top_k": 50,             # Filtra i 50 token più probabili
    "top_p": 0.95,           # Considera solo i token con probabilità cumulativa <= 0.95
    "repetition_penalty": 1.2  # Penalizza la ripetizione di token
}
