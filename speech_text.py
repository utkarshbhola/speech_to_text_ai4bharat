import speech_recognition as sr
import pyttsx3
import sys
from ai4bharat.transliteration import XlitEngine
import tkinter as tk
from tkinter import ttk  # For Combobox widget
import threading

# Initialize the recognizer
r = sr.Recognizer()

# Global variables
selected_language = ""
user_output = ""
user_input = ""

# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    global user_input,user_output
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            user_input = MyText
            SpeakText(user_output)
            print("Did you say:", MyText)
            # Insert the recognized text into the input text box
            text_area.delete("1.0", "end")  # Clear previous content
            text_area.insert("1.0", MyText)
            
            # Check for exit command
            if "exit" in MyText or "stop" in MyText:
                print("Exiting...")
                root.quit()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Unknown error occurred")

# Function to process input and transliterate
def process_input():
    global selected_language, user_input, user_output

    user_input = text_area.get("1.0", "end-1c")
    selected_language = language_var.get()

    # Perform transliteration
    ai4()

    # Update the output text area
    output_text.config(state="normal")  # Enable editing the output area
    output_text.delete("1.0", "end")  # Clear previous output
    output_text.insert("1.0", f"Input: {user_input}\nSelected Language: {selected_language}\nOutput: {user_output}")
    output_text.config(state="disabled")  # Disable editing the output area

# Function to perform transliteration
def ai4():
    global user_output
    language_codes = {
        "Hindi": "hi",
        "Konkani Goan": "gom",
        "Gujarati": "gu",
        "Bengali": "bn",
        "Kannada": "kn",
        "Maithili": "mai",
        "Malayalam": "ml",
        "Marathi": "mr",
        "Punjabi": "pa",
        "Sindhi": "sd",
        "Sinhala": "si",
        "Tamil": "ta",
        "Telugu": "te",
        "Urdu": "ur",
        "Oriya": "or"
    }

    if selected_language in language_codes:
        e = XlitEngine(language_codes[selected_language])
        user_output = e.translit_sentence(user_input)
    else:
        user_output = "Unsupported language"

# Function to handle speech recognition in a separate thread
def start_recognition():
    while True:
        recognize_speech()

# Create the main window
root = tk.Tk()
root.title("Input Box")

# Create input area
text_area = tk.Text(root, height=5, width=50)
text_area.pack(pady=10)

# Create output text area (initially empty)
output_text = tk.Text(root, height=5, width=50, state="disabled")
output_text.pack()

# Create dropdown for language selection
languages = ["English", "Hindi", "Sanskrit", "Oriya", "Konkani Goan", "Gujarati", "Bengali", "Kannada", "Maithili", "Malayalam", "Marathi", "Punjabi", "Sindhi", "Sinhala", "Tamil", "Telugu", "Urdu"]
language_var = tk.StringVar(root)
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=languages)
language_dropdown.pack()

# Create a button to trigger processing
process_button = tk.Button(root, text="Process", command=process_input)
process_button.pack(pady=10)

# Start speech recognition in a separate thread to keep the GUI responsive
recognition_thread = threading.Thread(target=start_recognition, daemon=True)
recognition_thread.start()

# Start the main event loop
root.mainloop()
