import mlflow

def log_podcast_results(file_name, transcript, summary, sentiment):
    mlflow.set_experiment("PodSage-PodcastSummarizer")

    with mlflow.start_run():
        mlflow.log_param("File Name", file_name)
        mlflow.log_metric("Transcript Length", len(transcript.split()))
        mlflow.log_metric("Sentiment Score", sentiment["Polarity"])
        mlflow.log_param("Sentiment", sentiment["Sentiment"])
        mlflow.log_text(transcript, "transcript.txt")
        mlflow.log_text(summary, "summary.txt")
