import whisper

# تحميل نموذج Whisper
model = whisper.load_model("base")

# تحليل الصوت من الملف اللي نزلناه سابقًا
result = model.transcribe("youtube_audio.mp4")

# طباعة النص الناتج
print("\n✅ النص المستخرج:\n")
print(result["text"])
