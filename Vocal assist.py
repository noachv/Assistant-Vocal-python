import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time




import pyttsx3

def parler(texte):
    print(texte)
    engine = pyttsx3.init()
    for voice in engine.getProperty('voices'):
        if 'FR' in voice.id or 'fr' in voice.id:
            engine.setProperty('voice', voice.id)
            pass

    engine.say(texte)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.3)



def donner_heure_actuelle():
    parler("Il est " + datetime.datetime.now().strftime("%H:%M"))

def donner_date_actuelle():
    date_actuelle = datetime.datetime.now().strftime("%d %B %Y")
    parler("Nous sommes le " + date_actuelle)

def ecouter_reponse(timeout=5, phrase_time_limit=5):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            print("J'écoute...")
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            texte = r.recognize_google(audio, language="fr-FR").lower()
            print("Vous avez dit :", texte)
            return texte
        except sr.UnknownValueError:
            print("Je n'ai pas compris ce que vous avez dit.")
            return ""
        except sr.RequestError:
            print("Erreur de service Google.")
            return ""
        except sr.WaitTimeoutError:
            print("Vous n'avez pas parlé à temps.")
            return ""

def assistant_vocal():
    parler("Bonjour je suis votre assistant vocal. Comment puis je vous aider aujourd'hui?")
    
    while True:
        texte_compris = ecouter_reponse()
        if texte_compris == "":
            continue

        if "heure" in texte_compris:
            donner_heure_actuelle()
            parler("Voulez-vous connaître la date d'aujourd'hui ?")
            reponse = ecouter_reponse(timeout=5, phrase_time_limit=5)
            if any(mot in reponse.strip().lower() for mot in ["oui","oui,","oui.", "ouais", "yes"]):
                donner_date_actuelle()
            else :
                pass
        
        elif "date" in texte_compris:
            donner_date_actuelle()

        elif "au revoir" in texte_compris or "stop" in texte_compris:
            parler("Au revoir ! À bientôt.")
            exit()

        else:
            parler("Je n'ai pas compris. Pouvez-vous répéter ?")

if __name__ == "__main__":
    assistant_vocal()