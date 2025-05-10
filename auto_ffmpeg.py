import urllib.request
import zipfile
import os

url = "https://youtu.be/g8w-XMxsLP8?si=hFVg-SLBkT4w0wfh"
zip_path = "ffmpeg.zip"
extract_path = "ffmpeg"

# تحميل الملف
print("⬇️ جاري تحميل FFmpeg...")
urllib.request.urlretrieve(url, zip_path)

# فك الضغط
print("🗂️ جاري فك الضغط...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# تنظيف
os.remove(zip_path)

# طباعة المسار اللي فيه ffmpeg.exe
for root, dirs, files in os.walk(extract_path):
    for file in files:
        if file == "ffmpeg.exe":
            ffmpeg_path = os.path.join(root, file)
            print(f"\n✅ FFmpeg جاهز في: {ffmpeg_path}")
            break
