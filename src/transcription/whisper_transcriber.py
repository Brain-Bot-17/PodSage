import whisper
import os
import tempfile
import ffmpeg

def load_model():
    return whisper.load_model("base")  # use "small" or "medium" for better accuracy

def convert_video_to_audio(input_path):
    output_path = tempfile.mktemp(suffix=".mp3")
    ffmpeg.input(input_path).output(output_path, format='mp3', acodec='mp3', ac=1, ar='16k').run(overwrite_output=True)
    return output_path

def transcribe_audio(model, file_path):
    if file_path.endswith(".mp4"):
        file_path = convert_video_to_audio(file_path)

    result = model.transcribe(file_path)
    return result["text"]
