from transformers import pipeline

def get_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(summarizer, text, max_chunk_len=1024):
    if len(text) <= max_chunk_len:
        return summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']

    # Split long texts into smaller chunks
    summaries = []
    for i in range(0, len(text), max_chunk_len):
        chunk = text[i:i + max_chunk_len]
        summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    return "\n".join(summaries)
