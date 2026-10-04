# 📋🖊️ Gist — AI Text Summarizer

Gist reads your text and gives you back exactly what matters. Paste an article, a report, or your notes, and choose a quick overview or a fuller, more detailed breakdown — all in seconds, powered by AI.

**Live demo:** [Try it here](https://gist-ai-text-summarizer-btkz7czzm7pqrasujnv7me.streamlit.app/)

## What it does

- Condenses long text into a short, essential summary, or expands it into a detailed breakdown with added context and elaboration
- Scales the summary length relative to the input — a short summary targets roughly 35% of the original word count, a detailed summary targets roughly 130%, so results stay sensible whether the input is 20 words or 2,000
- Accepts text pasted directly, or a `.txt` file upload
- Tracks word count on both the input and output sides
- One-click copy of the generated summary
- One-click clear to reset the input and start a new summary
- Shows a friendly message instead of crashing if the AI service fails

## Tech stack

- **Python**
- **Streamlit** for the web interface
- **Google Gemini API** for generating summaries
- **python-dotenv** for keeping the API key out of the code

## How it works

1. The user pastes text or uploads a `.txt` file into the input box.
2. On clicking "Short Summary" or "Detailed Summary," the app calculates a target word count relative to the input length.
3. That target is sent to the Gemini model along with the text, instructing it to condense or expand accordingly.
4. The result appears in the output box, ready to copy.

## Run it locally

1. Clone the repository and open the folder.
2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Create a file named `.env` in the project folder and add your Gemini API key (free from Google AI Studio):

```
GEMINI_API_KEY=your_key_here
```

4. Start the app:

```
streamlit run app.py
```

## Project structure

```
gist-ai-text-summarizer/
├── app.py             # Streamlit app: UI and summarization logic
├── requirements.txt   # Python dependencies
└── .gitignore         # Keeps the API key out of GitHub
```

## Author

Alisha Tabassum, Computer Engineer

[LinkedIn](https://www.linkedin.com/in/alisha-tabassum-2230452b0)