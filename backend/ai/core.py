from ai.code_generator.generator import CodeGenerator
from ai.code_generator.regenerator import CodeRegenerator
from ai.utilities.file_manager import FileManager

class RIQAAI:
    def __init__(self):
        self.generator = CodeGenerator()
        self.regenerator = CodeRegenerator()
        self.file_manager = FileManager()
        
    def generate_code(self, prompt):
        """Coordina tutta la generazione del codice"""
        raw_code = self.generator.generate(prompt)
        optimized = self.regenerator.optimize(raw_code)
        return optimized
