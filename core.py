import numpy as np
from transformers import pipeline  # Esempio con HuggingFace

class RIQAAI:
    def __init__(self):
        self.model = self._load_model()
    
    def _load_model(self):
        """Carica il modello pre-addestrato"""
        return pipeline("text-generation", model="gpt2")  # Sostituisci con il tuo modello

    def process(self, input_text):
        """Elabora l'input con la tua logica personalizzata"""
        # Esempio: generazione testo
        output = self.model(input_text, max_length=50)
        return self._postprocess(output)

    def _postprocess(self, raw_output):
        """Pulizia dell'output"""
        return str(raw_output[0]['generated_text'])
