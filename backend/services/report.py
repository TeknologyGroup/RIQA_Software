def generate_latex_report(data, filename):
    with open(filename, 'w') as f:
        f.write("\\\\documentclass{article}\\n")
        f.write("\\\\begin{document}\\n")
        f.write("\\\\section{Simulation Results}\\n")
        f.write(f"Time: {data['time']}\\n")
        f.write(f"Frequency: {data['frequency']}\\n")
        f.write("\\\\end{document}\\n")
