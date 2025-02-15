# 🎥 Video Compressor / 影片壓縮工具for 1080P

📌 **Introduction 簡介**  
This is a video compression tool using **Python** and **FFmpeg**.  
It helps people who need to back up videos but **don't want high-quality files taking up too much disk space**.  
There are **two compression methods** available:  

1️⃣ **10,000 kbps for YouTube (60fps highest quality for uploads)**  

2️⃣ **VBR (Variable Bitrate) for static footage, reducing file size without significant quality loss**  

For **dynamic videos**, I personally use **10Mbps encoding**.  
For **static recordings**, I prefer **VBR**, as it provides a **smaller file size while maintaining good quality**.

---

這是一個用Python和FFmpeg的影片壓縮工具
幫助需要備份影片 但又不需要太高畫質來佔用硬碟容量的人們
有兩種壓縮方式

1️⃣一種為10000kbps給Youtube 60fps上傳最高畫質使用

2️⃣另一種是VBR適合變動畫面比較小的靜態攝影 可以讓影片縮得更小 畫質不會相差太多

我個人在動態影片會使用10M的轉碼，靜態拍攝使用VBR

📌 Usage / 使用說明

Simply drag and drop your video file onto convert.bat, and it will prompt you to choose between 10M or VBR conversion mode.
Alternatively, you can run convert.bat directly, and it will convert all .mp4 files in the current folder after selecting a mode.

Conversion Modes:

🔹 10M: Best for YouTube uploads (1080P 60fps, maximum quality).

🔹 VBR: Ideal for videos with mostly static scenes, reducing file size while maintaining quality.

只需 將檔案拖曳到 convert.bat，系統會詢問你要選擇 10M 或 VBR 模式，然後開始轉檔。
或者你可以 直接執行 convert.bat，它會 在選擇模式後，自動轉換這個資料夾內的所有 .mp4 檔案。

轉換模式說明：

🔹 10M：適合 YouTube 1080P 60fps 上傳的最高畫質。

🔹 VBR：適合 靜態畫面較多的影片，能有效縮小容量並保持畫質。
