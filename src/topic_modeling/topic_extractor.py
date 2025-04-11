from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

def extract_topics(text, n_topics=5):
    # Split text into meaningful sentences (ignoring too-short ones)
    sentences = [s.strip() for s in text.split('.') if len(s.strip().split()) > 3]

    if len(sentences) < 10:
        print(f"[DEBUG] Only {len(sentences)} valid sentences. Skipping topic modeling.")
        return None

    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    topic_model = BERTopic(embedding_model=embedding_model)
    topics, _ = topic_model.fit_transform(sentences)

    return topic_model.get_topic_info().head(n_topics)
