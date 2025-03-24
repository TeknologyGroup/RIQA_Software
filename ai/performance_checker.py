import subprocess
import ast

def is_code_inefficient(file_path):
    # Analisi statica del codice
    with open(file_path, "r") as f:
        tree = ast.parse(f.read())
    
    # Cerca pattern inefficienti (es. loop non ottimizzati)
    for node in ast.walk(tree):
        if isinstance(node, ast.For):
            print(f"Possibile inefficienza: loop in {file_path}")
            return True
    return False

def has_broken_dependencies(file_path):
    requirements = subprocess.run(
        ["pipdeptree", "--reverse"], 
        capture_output=True, 
        text=True
    )
    return "ERROR" in requirements.stdout