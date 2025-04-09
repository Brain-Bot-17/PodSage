# 🎙️ PodSage — AI Podcast Summarizer & Topic Extractor

PodSage is an intelligent app that converts podcasts/audio into summarized insights, key topics, and sentiment analysis using state-of-the-art NLP.

## 🚀 Features
- Upload MP3/MP4 files
- Transcribe using Whisper
- Summarize using Transformers (BART)
- Topic modeling with BERTopic
- Sentiment analysis with spaCy/Transformers
- Interactive Streamlit UI
- MLflow tracking

## 📁 Project Structure
```bash
podsage/
│
├── data/                   # Sample podcast files (.mp3/.mp4) and transcripts
├── notebooks/              # Jupyter notebooks for EDA/debug
├── src/                    # Source code
│   ├── transcription/      # Whisper-based transcriber
│   ├── summarization/      # Transformer-based summarizer
│   ├── topic_modeling/     # BERTopic or LDA modules
│   ├── sentiment/          # Sentiment analyzer code
│   └── ui/                 # Streamlit app code
├── models/                 # Saved models, embeddings
├── mlruns/                 # MLflow logs
├── .gitignore
├── requirements.txt
├── README.md
├── app.py                  # Launchable Streamlit app
└── setup.sh (optional)     # Auto setup script (env, run instructions)
## ⚙️ Setup Instructions
```
```bash
git clone https://github.com/yourusername/podsage.git
cd podsage
pip install -r requirements.txt
streamlit run app.py
