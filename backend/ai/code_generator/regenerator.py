from ai.utilities.performance import check_performance
from ai.utilities.file_manager import FileManager

class CodeRegenerator:
    def __init__(self):
        self.file_manager = FileManager()
        
    def optimize(self, code):
        """
        Ottimizza il codice generato
        Args:
            code: str - Codice da ottimizzare
        Returns:
            str - Codice ottimizzato
        """
        # 1. Analisi prestazionale
        perf_report = check_performance(code)
        
        # 2. Ottimizzazione (esempio base)
        optimized = self._remove_unused_imports(code)
        
        # 3. Salvataggio storico
        self.file_manager.log_optimization(original=code, optimized=optimized)
        
        return optimized
    
    def _remove_unused_imports(self, code):
        """Esempio semplificato di ottimizzazione"""
        lines = code.split('\n')
        return '\n'.join(line for line in lines if not line.strip().startswith('import unused_lib'))
