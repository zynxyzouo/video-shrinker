@echo off
setlocal enabledelayedexpansion

:: ✅ 檢查 FFmpeg 是否安裝
where ffmpeg >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ FFmpeg not found! Please install FFmpeg and add it to PATH.
    pause
    exit /b
)

:: ✅ 列出當前目錄的 MP4 檔案
echo 🔍 Scanning for MP4 files...
set files=
for %%F in (*.mp4 *.MP4) do (
    set files=1
    echo 🎥 Found: %%F
)

if not defined files (
    echo ⚠️ No MP4 files found. Place some MP4 files in this folder.
    pause
    exit /b
)

:: ✅ 讓使用者選擇模式
echo.
echo 📌 **Choose Conversion Mode:**
echo [1] 10M - 10Mbps H265 (Best for YouTube)
echo [2] VBR - Variable Bitrate (Good for Static Videos)
echo [3] 4K  - 40Mbps H264 (For Editing in Premiere)
set /p mode=Enter mode (1/2/3): 

if "%mode%"=="1" set preset=10M
if "%mode%"=="2" set preset=VBR
if "%mode%"=="3" set preset=4K
if not defined preset (
    echo ❌ Invalid input! Please enter 1, 2, or 3.
    pause
    exit /b
)

echo 🚀 Starting conversion mode: %preset%

:: ✅ 轉檔開始
for %%F in (*.mp4 *.MP4) do (
    set input=%%F
    set output=%%~nF_%preset%_H264.mp4

    echo 🔄 Converting: !input! → !output!
    
    if "%preset%"=="10M" (
        ffmpeg -i "!input!" -b:v 10M -c:v hevc_nvenc -preset p2 -rc vbr -bufsize 40M -pix_fmt yuv420p -c:a aac -b:a 128k -ac 2 -ar 48000 "!output!"
    ) else if "%preset%"=="VBR" (
        ffmpeg -i "!input!" -c:v hevc_nvenc -rc vbr -b:v 2M -maxrate 8M -bufsize 15M -preset p1 -tune hq -rc-lookahead 32 -c:a aac -b:a 128k "!output!"
    ) else if "%preset%"=="4K" (
        ffmpeg -i "!input!" -c:v libx264 -b:v 40M -vf scale=3840:2160 -preset slow -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -ac 2 -ar 48000 "!output!"
    )

    if %errorlevel% equ 0 (
        echo ✅ Conversion completed: !input!
    ) else (
        echo ❌ Conversion failed: !input!
    )
)

echo 🎉 All conversions completed!
pause
