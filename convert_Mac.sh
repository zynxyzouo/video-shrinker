#!/bin/bash

# ✅ 檢查 FFmpeg 是否安裝
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ FFmpeg not found! Please install FFmpeg."
    exit 1
fi

# ✅ 找到當前目錄的 MP4 檔案
files=(*.mp4 *.MP4)
if [ "${#files[@]}" -eq 0 ]; then
    echo "⚠️ No MP4 files found."
    exit 1
fi

# ✅ 讓使用者選擇模式
echo "📌 **Choose Conversion Mode:**"
echo "[1] 10M - 10Mbps H265 (YouTube)"
echo "[2] VBR - Variable Bitrate (Static Videos)"
echo "[3] 4K  - 40Mbps H264 (Editing in Premiere)"
read -p "Enter mode (1/2/3): " mode

case $mode in
    1) preset="10M" ;;
    2) preset="VBR" ;;
    3) preset="4K" ;;
    *) echo "❌ Invalid input!"; exit 1 ;;
esac

echo "🚀 Starting conversion mode: $preset"

# ✅ 開始轉檔
for file in "${files[@]}"; do
    output="${file%.*}_${preset}_H264.mp4"
    echo "🔄 Converting: $file → $output"

    if [ "$preset" == "10M" ]; then
        ffmpeg -i "$file" -b:v 10M -c:v libx265 -preset fast -crf 25 -pix_fmt yuv420p -c:a aac -b:a 128k -ac 2 -ar 48000 "$output"
    elif [ "$preset" == "VBR" ]; then
        ffmpeg -i "$file" -c:v libx265 -crf 23 -preset fast -pix_fmt yuv420p -c:a aac -b:a 128k "$output"
    else
        ffmpeg -i "$file" -c:v libx264 -b:v 40M -vf scale=3840:2160 -preset slow -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -ac 2 -ar 48000 "$output"
    fi

    if [ $? -eq 0 ]; then
        echo "✅ Conversion completed: $file"
    else
        echo "❌ Conversion failed: $file"
    fi
done

echo "🎉 All conversions completed!"
