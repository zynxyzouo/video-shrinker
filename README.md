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

## 📌 Usage / 使用說明

Simply **drag and drop** your video file onto `10M.bat` or `VBR.bat`, and it will be automatically converted.  
Alternatively, you can **run `10M.bat` or `VBR.bat` directly**, and it will **convert all `.mp4` files in the current folder**.  

---

只需 **將檔案拖曳到 `10M.bat` 或 `VBR.bat`**，影片就會自動進行轉換。  
或者你可以 **直接執行 `10M.bat` 或 `VBR.bat`**，它會 **自動轉換這個資料夾內的所有 `.mp4` 檔案**。
