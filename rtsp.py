import subprocess

# Define the FFmpeg command as a string
ffmpeg_command = """ffmpeg -f dshow -i video="@device_pnp_\\\\?\\usb#vid_01da&pid_5875&mi_00#6&770fab3&0&0000#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\\global" -preset medium -f rtsp rtsp://server.dsttamal.me:8554/stream1"""

# Use subprocess to run the command
# It's important to use shell=True on Windows if the command is a string
process = subprocess.run(ffmpeg_command, shell=True)

# Check if the process was successful
if process.returncode == 0:
    print("FFmpeg command executed successfully.")
else:
    print("FFmpeg command failed with return code:", process.returncode)