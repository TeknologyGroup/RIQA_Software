from code_generator import generate_code

def optimize_code(code):
    prompt = f"Ottimizza questo codice Python:\n\n{code}"
    return generate_code(prompt)