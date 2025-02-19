🎥 Video Compressor / 影片壓縮工具 for 1080P
📌 Introduction 簡介
This is a simple video compression tool using FFmpeg, no need for Python!
It helps you reduce video file size while keeping good quality, perfect for backing up videos without taking up too much disk space.

There are two compression methods available:

1️⃣ 10,000 kbps for YouTube (60fps highest quality for uploads)
2️⃣ VBR (Variable Bitrate) for static footage, reducing file size without significant quality loss

For dynamic videos, I personally use 10Mbps encoding.
For static recordings, I prefer VBR, as it provides a smaller file size while maintaining good quality.

這是一個簡單的影片壓縮工具，現在只需要安裝FFmpeg，不再需要Python！
適合備份影片但不想佔用太多硬碟空間的使用者。

提供兩種壓縮模式：

1️⃣ 10M (10,000 kbps)：適合 YouTube 60fps 高畫質上傳
2️⃣ VBR (可變位元率)：適合 靜態畫面較多的影片，可有效縮小容量並保持畫質

我個人會在動態影片使用10M的轉碼，靜態拍攝使用VBR，因為它能大幅減小檔案大小，且畫質影響不大。

📌 Usage / 使用說明

Simply drag and drop your MP4 file onto convert.bat, and it will prompt you to choose between 10M or VBR conversion mode.

Alternatively, you can run convert.bat directly, and it will convert all .mp4 files in the current folder after selecting a mode.

Conversion Modes / 轉換模式
🔹 10M → Best for YouTube uploads (1080P 60fps, maximum quality).
🔹 VBR → Ideal for videos with mostly static scenes, reducing file size while maintaining quality.

👉 FFmpeg must be installed and added to PATH before using this tool!

🚀 Now, you don’t need Python anymore! Just install FFmpeg and use the BAT script!
