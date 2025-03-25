from ai.utilities.performance import check_performance
from ai.utilities.file_manager import FileManager

class CodeRegenerator:
    def __init__(self):
        self.file_manager = FileManager()
    
    @check_performance
    def optimize(self, code: str) -> str:
        """Pulizia e ottimizzazione del codice generato"""
        optimized = self._remove_comments(code)
        return self._format_code(optimized)
    
    def _remove_comments(self, code: str) -> str:
        return '\n'.join(line for line in code.split('\n') 
                        if not line.strip().startswith('#') and line.strip())
    
    def _format_code(self, code: str) -> str:
        try:
            import black
            return black.format_str(code, mode=black.FileMode())
        except ImportError:
            return code
