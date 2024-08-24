# Speech-to-Text Transliteration Tool

This project is a Speech-to-Text Transliteration Tool that recognizes speech in English, converts it to text, and transliterates it into various Indian languages using AI4Bharat's transliteration engine. The tool also provides a graphical user interface (GUI) using Tkinter, making it user-friendly and easy to use.

## Features

- **Speech Recognition**: Uses Google's speech recognition API to convert spoken words into text.
- **Text-to-Speech**: Converts the transliterated text back into speech using `pyttsx3`.
- **Transliteration**: Supports multiple Indian languages, including Hindi, Bengali, Tamil, Telugu, and more.
- **Graphical User Interface (GUI)**: A Tkinter-based interface for easy interaction.
- **Multi-threading**: Speech recognition runs in a separate thread, ensuring the GUI remains responsive.

## Supported Languages

The tool supports transliteration into the following languages:

- Hindi
- Konkani Goan
- Gujarati
- Bengali
- Kannada
- Maithili
- Malayalam
- Marathi
- Punjabi
- Sindhi
- Sinhala
- Tamil
- Telugu
- Urdu
- Oriya

## Installation

### Prerequisites

- Python 3.x
- Required Python libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `ai4bharat-transliteration`
  - `tkinter`

### Install the required libraries

You can install the required Python libraries using pip:

```bash
pip install speechrecognition pyttsx3 ai4bharat-transliteration
