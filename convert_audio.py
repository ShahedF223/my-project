import os
os.environ["PATH"] += os.pathsep + r"C:\Users\zim\Documents\myproject\ffmpeg\ffmpeg-7.1.1-essentials_build\bin"

from pydub import AudioSegment

# قراءة الملف وتحويله
audio = AudioSegment.from_file("youtube_audio.webm", format="webm")
audio.export("converted_audio.wav", format="wav")
print("✅ تم تحويل الصوت إلى wav.")
