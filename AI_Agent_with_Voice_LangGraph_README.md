
# AI Agent with Voice LangGraph

## Overview
This project implements an AI agent equipped with a voice-enabled interface and a language graph (LangGraph) for multilingual natural language understanding. The system supports seamless speech-to-text (STT) and text-to-speech (TTS) conversions, multilingual interactions, and context-aware responses.

---

## Features
- **Voice Input and Output**: Users can interact with the AI agent using voice.
- **Multilingual Support**: Real-time translation and language understanding.
- **LangGraph Integration**: Structured language representation for intent recognition and semantic linking.
- **Context Awareness**: Retains user query history to manage multi-turn conversations.
- **Text-Based Fallback**: Provides a text interface for accessibility.

---

## Requirements

### Backend:
- Python 3.8+
- Libraries:
  - `openai`
  - `SpeechRecognition`
  - `pytesseract`
  - `gTTS` or `pyttsx3`
  - `networkx`
  - `Flask`
  - `Neo4j` (for LangGraph)

### Frontend:
- HTML, CSS, JavaScript
- Web Speech API (for browser-based voice interactions)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ShraddhaAbhang/ai_agent.git
   cd voice-langgraph-agent
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up LangGraph**:
   - Install Neo4j:
     [Download Neo4j](https://neo4j.com/download/)
   - Create a new database for LangGraph.

5. **Run the Application**:
   ```bash
   flask run
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Usage

### Interacting with the Agent
- **Voice**: Use a microphone to ask queries.
- **Text**: Type queries into the provided text box.

### Supported Languages
- English
- Spanish
- French
- German
- More languages can be added via LangGraph.

---

## File Structure
```
voice-langgraph-agent/
├── app/
│   ├── static/          # Frontend assets
│   ├── templates/       # HTML templates
│   └── main.py         # Flask application
├── langgraph/
│   └── graph_utils.py  # LangGraph utilities
├── requirements.txt
└── README.md
```

---

## Future Improvements
- **Voice Personalization**: Adapt the voice output based on user preferences.
- **Enhanced LangGraph**: Introduce deep semantic linking and knowledge graphs.
- **Mobile Support**: Extend the application to mobile platforms.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributors
- [Shraddha Abhang](https://github.com/ShraddhaAbhang)

Feel free to contribute by submitting issues or pull requests.

Thank You!!

