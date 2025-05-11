import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import openai
import gtts


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d0b77e8572d049b88a48a04d50195d8f"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):

    openai.api_key = ""

    response = openai.Completion.create(
        model="gpt-3.5-turbo", 
        prompt="You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant. What is coding?",
        max_tokens=100
    )

    return response.choices[0].text.strip()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            
            for article in articles:
                speak(article["title"])
    else:
        #let openai handle the request
        output = aiProcess(c)
        speak(output)


if __name__ == "__main__":

    speak("Initializing Jarvis...")

    # Listen for the wake work "Jarvis"

    while True:
            r = sr.Recognizer()

            try:
                with sr.Microphone() as source:
                    print("Listening...")   
                    audio = r.listen(source,timeout=2,phrase_time_limit=1)
                jarvis = r.recognize_google(audio)
                if(jarvis.lower()=="jarvis"):
                    speak("Yes Sir")
                    #Listen for command
                    with sr.Microphone() as source:
                        print("Jarvis Activated...")   
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        processCommand(command)
                        

            except Exception as e:
                print("Error; {0}".format(e))


# Completed at 4:20 pm , 11th of May 2025