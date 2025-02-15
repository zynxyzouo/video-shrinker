import os
import sys
import subprocess

# ✅ Display the dragged-in files to ensure Python receives them correctly
print(f"📌 sys.argv: {sys.argv}")

# Get the dragged-in files (sys.argv[0] is the script itself, so we exclude it)
input_files = [arg.strip('"') for arg in sys.argv[1:] if arg.lower().endswith(".mp4")]

# If no files are dragged in, scan the current folder for MP4 files
if not input_files:
    input_folder = os.getcwd()
    input_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.lower().endswith(".mp4")]

# ✅ If no files are found, pause so the user can see the error
if not input_files:
    print("⚠️ No MP4 files found. Please drag files in or place them in the same folder.")
    os.system("pause")  # Prevents the window from closing immediately
    sys.exit()

# ✅ Display found MP4 files
print("\n🎥 Found the following MP4 files:")
for idx, file in enumerate(input_files, start=1):
    print(f"{idx}. {os.path.basename(file)}")

# ✅ Provide recommendations before user selection
print("\n📌 **Recommended settings:**")
print("🔹 **10M**: Best for **YouTube uploads** (1080P 60fps, maximum quality).")
print("🔹 **VBR**: Ideal for **videos with mostly static scenes**, reducing file size further while maintaining quality.")

# ✅ Ask the user for the conversion mode
mode = input("\nPlease choose the conversion mode (Enter '10M' or 'VBR'): ").strip().upper()

if mode not in ["10M", "VBR"]:
    print("❌ Error: Please enter '10M' or 'VBR'.")
    os.system("pause")
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
                "ffmpeg", "-hwaccel", "cuda", "-i", input_path,
                "-b:v", "10M", "-c:v", "hevc_nvenc", "-preset", "p2",
                "-rc", "vbr", "-bufsize", "40M",
                "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "128k", "-ac", "2", "-ar", "48000",
                output_path
            ]
        else:  # VBR mode
            command = [
                "ffmpeg", "-i", input_path,
                "-c:v", "hevc_nvenc", "-rc", "vbr",
                "-b:v", "2M", "-maxrate", "8M", "-bufsize", "15M",
                "-preset", "p1", "-tune", "hq",
                "-rc-lookahead", "32",
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
os.system("pause")  # Wait for user input before closing
