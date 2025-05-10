import os
os.environ["PATH"] += os.pathsep + r"C:\Users\zim\Documents\myproject\ffmpeg\ffmpeg-7.1.1-essentials_build\bin"

import whisper

# تحميل نموذج Whisper
model = whisper.load_model("base")

# تحويل الصوت إلى نص
result = model.transcribe("converted_audio.wav", language="ar")

# طباعة النص
print("📜 النص المستخرج:")
print(result["text"])
