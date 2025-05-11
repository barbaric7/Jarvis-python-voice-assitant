🎙️ JARVIS - Python Voice Assistant
JARVIS is a Python-based voice assistant bot that can perform a variety of personalized tasks using voice commands. Inspired by the iconic AI from Iron Man, this assistant brings automation and convenience right to your desktop.

🚀 Features
🎵 Play your favorite music playlist

🗂️ Perform custom and personalized tasks

🌐 Control your browser using just your voice

📰 Get real-time news and current headlines

✅ Handle various simple day-to-day operations

🤖 Ask random question & get response from gpt-3.5 turbo

🛠️ Built With
Python

SpeechRecognition

pyttsx3 (Text-to-Speech)

webbrowser

requests

datetime, os, playsound, and more

🖥️ Setup Instructions
Clone the repository:

git clone https://github.com/barbaric7/Jarvis-python-voice-assistant.git
cd Jarvis-python-voice-assistant

Install required packages:

pip install -r requirements.txt

Run the bot:

python main.py

📁 Folder Structure
css
Copy
Edit
jarvis-python-voice-assistant/
├── main.py
├── requirements.txt
├── README.md

    
🧠 How It Works
JARVIS listens to your voice using the microphone, interprets the command using speech recognition, and then performs the mapped task. The core logic is written entirely in Python and has an integration with gpt-3.5-turbo model to give a response to random commands which aren't coded in script.

🗣️ Example Voice Commands
"Jarvis , Play music"

"Jarvis , Open YouTube"

"Jarvis , Tell me the news"

"Jarvis , What time is it?"

"Jarvis , Search for Python tutorials"

📌 Notes
Make sure your microphone is connected and working.

Edit the script to customize file paths and task behavior.

News API key may be required depending on the service used.

Use OpeniAi API 3.5-turbo keys.
