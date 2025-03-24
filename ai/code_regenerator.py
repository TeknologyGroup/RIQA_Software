from code_generator import generate_code
import os

def regenerate_file(file_path):
    with open(file_path, "r") as f:
        old_code = f.read()
    
    prompt = f"""
    Ottimizza questo codice Python, rimuovendo inefficienze e aggiornando le librerie:
    ```python
    {old_code}
    ```
    """
    new_code = generate_code(prompt)
    
    with open(file_path, "w") as f:
        f.write(new_code)
    print(f"✅ File rigenerato: {file_path}")