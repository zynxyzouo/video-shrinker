import os
import sys
import subprocess
import platform

# ✅ Detect OS (Windows or Mac)
is_mac = platform.system() == "Darwin"

# ✅ Display detected OS
print(f"🖥️ Detected OS: {'Mac' if is_mac else 'Windows'}")

# ✅ Display the dragged-in files to ensure Python receives them correctly
print(f"📌 sys.argv: {sys.argv}")

# Get the dragged-in files (sys.argv[0] is the script itself, so we exclude it)
input_files = [
    arg.strip('"') for arg in sys.argv[1:]
    if arg.lower().endswith(".mp4")  # ✅ 支援大小寫 MP4
]

# If no files are dragged in, scan the current folder for MP4 files
if not input_files:
    input_folder = os.getcwd()
    input_files = [
        os.path.join(input_folder, file)
        for file in os.listdir(input_folder)
        if file.lower().endswith(".mp4")  # ✅ 確保 Mac 也能找到 .MP4
    ]

# ✅ If no files are found, pause so the user can see the error
if not input_files:
    print("⚠️ No MP4 files found. Please drag files in or place them in the same folder.")
    os.system("pause") if not is_mac else input("Press Enter to exit...")
    sys.exit()

# ✅ Display found MP4 files
print("\n🎥 Found the following MP4 files:")
for idx, file in enumerate(input_files, start=1):
    print(f"{idx}. {os.path.basename(file)}")

# ✅ Provide recommendations before user selection
print("\n📌 **Recommended settings:**")
print("🔹 **10M**: Best for **YouTube uploads** (1080P 60fps, maximum quality).")
print("🔹 **VBR**: Ideal for **videos with mostly static scenes**, reducing file size while maintaining quality.")

# ✅ Ask the user for the conversion mode
mode = input("\nPlease choose the conversion mode (Enter '10M' or 'VBR'): ").strip().upper()

if mode not in ["10M", "VBR"]:
    print("❌ Error: Please enter '10M' or 'VBR'.")
    os.system("pause") if not is_mac else input("Press Enter to exit...")
    sys.exit()

print(f"\n🚀 Starting conversion mode: {mode}")

# ✅ Convert all MP4 files
for input_path in input_files:
    try:
        input_folder, file_name = os.path.split(input_path)
        output_filename = f"{os.path.splitext(file_name)[0]}_{mode}_H265.mp4"
        output_path = os.path.join(input_folder, output_filename)

        print(f"🔄 Converting: {file_name} → {output_filename}")

        # Select the appropriate FFmpeg parameters
        if mode == "10M":
            command = [
                "ffmpeg", "-i", input_path,
                "-b:v", "10M", "-c:v", "hevc_nvenc" if not is_mac else "libx265",  # ✅ Windows: NVIDIA | Mac: libx265
                "-preset", "p2" if not is_mac else "fast",
                "-rc", "vbr" if not is_mac else "crf",
                "-bufsize", "40M",
                "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "128k", "-ac", "2", "-ar", "48000",
                output_path
            ]
        else:  # VBR mode
            command = [
                "ffmpeg", "-i", input_path,
                "-c:v", "hevc_nvenc" if not is_mac else "libx265",
                "-rc", "vbr" if not is_mac else "crf",
                "-b:v", "2M", "-maxrate", "8M", "-bufsize", "15M",
                "-preset", "p1" if not is_mac else "fast",
                "-tune", "hq",
                "-rc-lookahead", "32" if not is_mac else "28",
                "-c:a", "aac", "-b:a", "128k",
                output_path
            ]

        # ✅ Run FFmpeg conversion
        subprocess.run(command, check=True)

        print(f"✅ Conversion completed: {file_name}")

    except Exception as e:
        print(f"❌ Conversion failed: {file_name}, Error: {e}")

# ✅ Prevent the window from closing automatically
print("\n🎉 All MP4 files have been converted!")
os.system("pause") if not is_mac else input("Press Enter to exit...")
