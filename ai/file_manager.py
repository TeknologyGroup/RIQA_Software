import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"File modificato: {event.src_path}")
            self.check_file_obsolescence(event.src_path)

    def check_file_obsolescence(self, file_path):
        last_modified = os.path.getmtime(file_path)
        if (time.time() - last_modified) > 30 * 24 * 3600:  # 30 giorni
            print(f"File obsoleto: {file_path}")
            self.regenerate_file(file_path)

    def regenerate_file(self, file_path):
        from code_generator import generate_code
        with open(file_path, "r") as f:
            old_code = f.read()
        new_code = generate_code(f"Ottimizza questo codice Python:\n\n{old_code}")
        with open(file_path, "w") as f:
            f.write(new_code)
        print(f"File rigenerato: {file_path}")

observer = Observer()
observer.schedule(FileChangeHandler(), path=".", recursive=True)
observer.start()