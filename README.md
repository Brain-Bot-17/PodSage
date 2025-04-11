# 🎙️ PodSage - AI Podcast Summarizer & Topic Extractor

PodSage is an AI-powered tool that lets you upload podcast/video/audio files and get:

- ✅ Transcripts (via Whisper)
- ✅ Summaries (via Transformers)
- ✅ Topic Extraction (via BERTopic)
- ✅ Sentiment Analysis (via spaCy)
- ✅ All results logged with MLflow

## 🚀 Tech Stack

- **Whisper** - OpenAI speech-to-text
- **Transformers** - For BART-based summarization
- **BERTopic** - Topic modeling
- **spaCy** - Sentiment analysis
- **Streamlit** - UI
- **MLflow** - Experiment tracking

## 💻 Run Locally

```bash
git clone https://github.com/Brain-Bot-17/PodSage.git
cd PodSage
pip install -r requirements.txt
streamlit run app.py
