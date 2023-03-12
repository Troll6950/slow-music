import os
from pydub import AudioSegment

# Get the current directory of the Python script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the directory path for the input MP3 files in the "music" folder
music_dir = os.path.join(current_dir, "music")

# Set the directory path for the output MP3 files in the "finished" folder
output_dir = os.path.join(current_dir, "finished")

# Set the speed at which you want to slow down the audio
speed = 0.8  # This will slow down the audio by 20%

# List all files in the "music" folder
files = os.listdir(music_dir)

# Filter out only the MP3 files
mp3_files = [f for f in files if f.endswith(".mp3")]

# Loop through each MP3 file and slow down the audio
for mp3_file in mp3_files:
    # Set the file path for the input MP3 file
    input_file_path = os.path.join(music_dir, mp3_file)

    # Set the file path for the output MP3 file with "(slowed)" added to the end of the file name
    output_file_name = os.path.splitext(mp3_file)[0] + "(slowed).mp3"
    output_file_path = os.path.join(output_dir, output_file_name)

    # Load the audio file using PyDub
    audio = AudioSegment.from_file(input_file_path)

    # Slow down the audio using the speed you set
    slowed_audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * speed)})

    # Export the slowed down audio as an MP3 file with the same name as the input file
    slowed_audio.export(output_file_path, format="mp3")

    # Check if the output file already exists in the "finished" folder
    if os.path.exists(output_file_path):
        print("Finished:", mp3_file)
    else:
        # Load the audio file using PyDub
        audio = AudioSegment.from_file(input_file_path)

        # Slow down the audio using the speed you set
        slowed_audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * speed)})

        # Export the slowed down audio as an MP3 file with the same name as the input file
        slowed_audio.export(output_file_path, format="mp3")
        print("Finished:", mp3_file)
