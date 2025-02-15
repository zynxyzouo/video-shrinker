import os
import sys
import subprocess

# ✅ 顯示拖曳進來的參數，確保 Python 正常接收到檔案
print(f"📌 sys.argv: {sys.argv}")

# 取得拖曳進來的檔案（sys.argv[0] 是 Python 檔案本身，所以要排除）
input_files = [arg.strip('"') for arg in sys.argv[1:] if arg.lower().endswith(".mp4")]

# 如果沒有拖曳檔案，則使用當前資料夾內的所有 .mp4 檔案
if not input_files:
    input_folder = os.getcwd()
    input_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.lower().endswith(".mp4")]

# ✅ 如果仍然沒有找到檔案，暫停視窗，讓你可以看到錯誤
if not input_files:
    print("⚠️ 找不到任何 MP4 檔案，請確認是否拖曳了檔案或放在同資料夾內！")
    os.system("pause")  # 確保視窗不會瞬間關閉
    sys.exit()

print(f"✅ 找到 {len(input_files)} 個 MP4 檔案")

# 轉換所有 MP4 影片
for input_path in input_files:
    try:
        input_folder, file_name = os.path.split(input_path)
        output_path = os.path.join(input_folder, f"{os.path.splitext(file_name)[0]}_10Mbps_H265.mp4")

        # ✅ 顯示檔案名稱，讓你確認它有被讀取
        print(f"🚀 轉換中：{file_name} → {os.path.basename(output_path)}")

        # FFmpeg 指令（支援拖曳進來的 MP4）
        command = [
            "ffmpeg", "-hwaccel", "cuda", "-i", input_path,  # 使用 CUDA 加速
            "-b:v", "10M", "-c:v", "hevc_nvenc", "-preset", "p2",  # 固定 10Mbps 編碼
            "-rc", "vbr", "-bufsize", "40M",  # 使用 VBR，確保穩定輸出
            "-pix_fmt", "yuv420p",  # 確保相容性
            "-c:a", "aac", "-b:a", "128k", "-ac", "2", "-ar", "48000",  # 音訊設定
            output_path
        ]

        # ✅ `subprocess.run` 顯示即時輸出，確保 FFmpeg 執行中
        subprocess.run(command, check=True)

        print(f"✅ 已轉換完成：{file_name}")

    except Exception as e:
        print(f"❌ 轉換失敗：{file_name}，錯誤訊息：{e}")

# ✅ 避免視窗自動關閉
print("🎉 所有 MP4 影片已轉換完成！")
os.system("pause")  # 等待使用者按下按鍵再關閉視窗
