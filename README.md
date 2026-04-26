# Coach Sportif Inclusif

An AI-powered chatbot that acts as an inclusive and empathetic sports coach for people with disabilities. It provides adapted exercises, safety tips, and relevant YouTube video links tailored to each user's situation.

## Features

- Personalized exercise recommendations adapted to various disabilities
- Breathing, recovery, and motivation tips
- Automatic YouTube video search related to each exercise suggestion
- Runs locally via [Ollama](https://ollama.com/) (llama3 model)

## Project Structure

```
.
├── main.py          # Entry point — runs the interactive chatbot loop
├── ChatBot.py       # Generates responses using the local Ollama API
├── video.py         # Searches YouTube for relevant exercise videos
├── fill_video.py    # Injects YouTube links into the chatbot response
```

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) running locally with the `llama3` model
- A YouTube Data API v3 key (set in `video.py`)

### Install dependencies

```bash
pip install requests
```

### Start Ollama

```bash
ollama run llama3
```

## Usage

```bash
python main.py
```

The chatbot will prompt you to describe your situation or goal, then respond with adapted exercises and YouTube video links.

Type `exit`, `quit`, or `stop` to end the session.

## Example

```
👤 Toi : Je suis en fauteuil roulant et je veux travailler mes bras.

🤖 Coach :
Parfait 💪 ! Voici un exercice adapté :

**Flexions des biceps avec bouteilles d'eau**
- 3 séries de 12 répétitions.
- Garde tes coudes près du corps ...

🎥 Tu peux regarder ces vidéos :
1. https://www.youtube.com/watch?v=...
```

## Notes

- The chatbot does not make medical diagnoses and always recommends consulting a doctor when necessary.
- Responses are generated in French.
