import streamlit as st
from src.transcription.whisper_transcriber import load_model, transcribe_audio
from src.summarization.summarizer import get_summarizer, summarize_text
from src.topic_modeling.topic_extractor import extract_topics
from src.sentiment.sentiment_analysis import analyze_sentiment
from src.mlops.logger import log_podcast_results

import tempfile
import json

st.set_page_config(page_title="PodSage", layout="centered", page_icon="🎙️")
st.title("🎙️ PodSage - Podcast Summarizer & Transcriber")
st.caption("Upload a podcast or video file and get instant transcription, summarization, topics, and sentiment analysis!")

uploaded_file = st.file_uploader("📤 Upload an MP3 or MP4 file", type=["mp3", "mp4"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    st.info("🔁 Transcribing audio... Please wait.")
    model = load_model()
    transcription = transcribe_audio(model, file_path)

    if not transcription or len(transcription.split()) < 10:
        st.error("❌ Transcription too short for meaningful analysis. Try a longer audio/video.")
        st.stop()

    st.success("✅ Transcription complete!")

    with st.expander("📝 Show Transcript"):
        st.write(transcription)

    with st.spinner("🧠 Summarizing..."):
        summarizer = get_summarizer()
        summary = summarize_text(summarizer, transcription)
    st.success("✅ Summary complete!")

    with st.expander("🧾 Show Summary"):
        st.write(summary)

    with st.spinner("📚 Extracting Topics..."):
        topic_df = extract_topics(transcription)

    if topic_df is not None and not topic_df.empty:
        st.success("✅ Topics identified!")
        with st.expander("🏷️ Show Extracted Topics"):
            st.dataframe(topic_df)
    else:
        st.warning("⚠️ Not enough content for topic modeling. Try uploading a longer podcast/video.")

    with st.spinner("💬 Performing Sentiment Analysis..."):
        sentiment = analyze_sentiment(transcription)
    st.success("✅ Sentiment analysis complete!")

    with st.expander("📊 Show Sentiment Analysis"):
        st.json(sentiment)

    # ✅ Log everything to MLflow
    log_podcast_results(uploaded_file.name, transcription, summary, sentiment)

    # ⬇️ Download options
    st.markdown("### 📥 Download Results")
    st.download_button("📝 Transcript", transcription, file_name="transcript.txt")
    st.download_button("🧾 Summary", summary, file_name="summary.txt")
    st.download_button("📊 Sentiment (JSON)", json.dumps(sentiment, indent=2), file_name="sentiment.json")
