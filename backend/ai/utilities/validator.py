import ast
import black

class CodeValidator:
    @staticmethod
    def validate_syntax(code: str) -> bool:
        try:
            ast.parse(code)
            return True
        except SyntaxError:
            return False
    
    @staticmethod
    def format_code(code: str) -> str:
        try:
            return black.format_str(code, mode=black.FileMode())
        except:
            return code
