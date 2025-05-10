import yt_dlp

url = "https://youtu.be/g8w-XMxsLP8?si=hFVg-SLBkT4w0wfh"

ydl_opts = {
    'format': 'bestaudio',
    'outtmpl': 'youtube_audio.%(ext)s',  # ما منحول mp3، بنخليها بصيغتها
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("✅ تم تحميل الصوت بدون تحويل!")
