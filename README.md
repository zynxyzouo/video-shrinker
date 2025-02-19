🎥 1080P 影片壓縮工具

📌 簡介
這是一款 基於 FFmpeg 的簡單影片壓縮工具，無需 Python！
適合備份影片但不想佔用太多硬碟空間的使用者。

提供兩種壓縮模式：

🔹 10M (10,000 kbps) → 適合 1080P 60fps 高畫質上傳 (如 YouTube)

🔹 VBR (可變位元率) → 適合 靜態畫面較多的影片，有效縮小容量並保持畫質

👉 動態影片建議 10M，靜態拍攝建議 VBR，可大幅減小檔案大小且畫質影響不大。

📌 使用方式

拖曳 MP4 檔案 到 convert.bat，選擇 10M 或 VBR 模式後開始轉檔
直接執行 convert.bat，會批次轉換資料夾內所有 .mp4 檔案

📌 新增功能：ConvertToH264 模式
部分影片在 Premiere 匯入時卡頓？
→ 使用 ConvertToH264 轉檔後再試試看！

🚀 現在只需 FFmpeg + BAT 腳本，即可快速壓縮影片！

==============================================================
🎥 1080P Video Compression Tool

📌 Introduction
A simple video compression tool using FFmpeg, no Python required!
Perfect for backing up videos without taking up too much storage space.

Two compression modes available:

🔹 10M (10,000 kbps) → Best for 1080P 60fps high-quality uploads (e.g., YouTube)

🔹 VBR (Variable Bitrate) → Ideal for videos with mostly static scenes, reducing file size while maintaining quality

👉 Use 10M for dynamic videos and VBR for static recordings to achieve the best balance between quality and file size.

📌 How to Use

Drag and drop an MP4 file onto convert.bat, select 10M or VBR, and the conversion will start.
Run convert.bat directly, and it will batch convert all .mp4 files in the current folder.
📌 Requirements

⚠️ FFmpeg must be installed and added to PATH!

📌 New Feature: ConvertToH264 Mode
Experiencing lag in Premiere Pro when importing videos?
→ Use ConvertToH264 mode and try again!

🚀 Now, just FFmpeg + BAT script = Quick and easy video compression!
