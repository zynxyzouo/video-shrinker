🎥 影片壓縮工具 for 1080P
📌 簡介

這是一個簡單的影片壓縮工具，現在只需要安裝FFmpeg，不再需要Python！
適合備份影片但不想佔用太多硬碟空間的使用者。

提供兩種壓縮模式：

1️⃣ 10M (10,000 kbps)：適合 YouTube 60fps 高畫質上傳

2️⃣ VBR (可變位元率)：適合 靜態畫面較多的影片，可有效縮小容量並保持畫質

我個人會在動態影片使用10M的轉碼，靜態拍攝使用VBR，因為它能大幅減小檔案大小，且畫質影響不大。

📌 使用說明

將MP4檔案拖曳到 convert.bat，系統會詢問你要選擇10M 或 VBR 模式，然後開始轉檔。
或者，你也可以直接執行 convert.bat，它會在選擇模式後，自動轉換這個資料夾內的所有 .mp4 檔案。

轉換模式

🔹 10M → 適合 YouTube 1080P 60fps 上傳的最高畫質。

🔹 VBR → 適合 靜態畫面較多的影片，能有效縮小容量並保持畫質。

👉 使用前請先安裝 FFmpeg 並加入 PATH！

🚀 現在不需要 Python 了！只要安裝 FFmpeg 並使用 BAT 腳本即可！

📌 最底下新增了一個 "ConvertToH264" 模式，給匯入 Premiere 會卡頓的使用者。
請將影片和 BAT 檔案放在同一個資料夾，執行 BAT 轉檔後再試試看！

🎥 Video Compressor for 1080P

📌 Introduction

This is a simple video compression tool using FFmpeg, no need for Python!
It helps you reduce video file size while keeping good quality, perfect for backing up videos without taking up too much disk space.

There are two compression methods available:

1️⃣ 10,000 kbps for YouTube (60fps highest quality for uploads)

2️⃣ VBR (Variable Bitrate) for static footage, reducing file size without significant quality loss

For dynamic videos, I personally use 10Mbps encoding.
For static recordings, I prefer VBR, as it provides a smaller file size while maintaining good quality.

📌 Usage

Simply drag and drop your MP4 file onto convert.bat, and it will prompt you to choose between 10M or VBR conversion mode.
Alternatively, you can run convert.bat directly, and it will convert all .mp4 files in the current folder after selecting a mode.

Conversion Modes
🔹 10M → Best for YouTube uploads (1080P 60fps, maximum quality).
🔹 VBR → Ideal for videos with mostly static scenes, reducing file size while maintaining quality.

👉 FFmpeg must be installed and added to PATH before using this tool!

🚀 Now, you don’t need Python anymore! Just install FFmpeg and use the BAT script!

📌 Added a new "ConvertToH264" mode for users experiencing lag when importing videos into Premiere.
Simply place your video files and the BAT script in the same folder, run the BAT file, and try the converted video in Premiere!
