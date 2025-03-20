import speech_recognition as sr
import pyttsx3
import requests

class RIQAAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # VelocitC  voce
    
    def speak(self, text):
        """Parla il testo."""
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Ascolta un comando vocale."""
        with sr.Microphone() as source:
            self.speak("Pronto, dimmi cosa fare.")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                print(f"Comando: {command}")
                return command.lower()
            except sr.UnknownValueError:
                self.speak("Non ho capito, ripeti.")
                return None
    
    def process_command(self, command):
        """Elabora il comando e chiama l'API."""
        if not command:
            return
        
        if "simula wormhole" in command:
            # Estrai parametri dal comando (es. "simula wormhole con zero 2")
            zero_index = 1
            for word in command.split():
                if word.isdigit():
                    zero_index = int(word)
                    break
            
            params = {'zero_index': zero_index, 'r_range': 10, 'points': 100}
            response = requests.post('http://localhost:5000/simulate/wormhole', json=params)
            
            if response.status_code == 200:
                data = response.json()
                self.speak(f"Simulazione completata. Raggio della gola: {data['b0']:.2f}. Vuoi visualizzare?")
            else:
                self.speak("Errore nella simulazione.")
        else:
            self.speak("Comando non riconosciuto.")

def run_assistant():
    assistant = RIQAAssistant()
    while True:
        command = assistant.listen()
        assistant.process_command(command)

if __name__ == "__main__":
    run_assistant()

