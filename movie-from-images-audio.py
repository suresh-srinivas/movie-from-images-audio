from moviepy.editor import ImageSequenceClip, AudioFileClip
from PIL import Image
import os

# Settings and paths
media_folder = 'Episode 7'
image_files = sorted([os.path.join(media_folder, f) for f in os.listdir(media_folder) if f.endswith((".png", ".jpg", ".jpeg"))])[:6]
audio_file = 'Episode7-audio.mp3'  # Example: "existing_audio.mp3"

# Load existing audio
existing_audio_clip = AudioFileClip(os.path.join(media_folder, audio_file))
print(f"Audio Duration: {existing_audio_clip.duration} seconds")

# Calculate frames per second based on the audio duration and number of images
fps = len(image_files) / existing_audio_clip.duration

# Process images
desired_size = (1080, 1920)  # YouTube Shorts dimensions
resized_images = []
for img_path in image_files:
    img = Image.open(img_path)
    img.thumbnail((desired_size[0], desired_size[1]), Image.Resampling.LANCZOS)
    img_width, img_height = img.size
    left = (img_width - desired_size[0]) / 2
    top = (img_height - desired_size[1]) / 2
    right = (img_width + desired_size[0]) / 2
    bottom = (img_height + desired_size[1]) / 2
    img = img.crop((left, top, right, bottom))
    if img.mode != 'RGB':
        img = img.convert('RGB')
    resized_images.append(img)

# Save resized images temporarily
temp_image_files = []
for idx, img in enumerate(resized_images):
    temp_path = os.path.join(media_folder, f"temp_{idx}.jpg")
    img.save(temp_path, 'JPEG')
    temp_image_files.append(temp_path)

# Create a video clip from resized images, set duration to match audio
clip = ImageSequenceClip(temp_image_files, fps=fps)

# Set the audio to the video
video = clip.set_audio(existing_audio_clip)

# Write the result to a file
video.write_videofile("output_video.mp4", codec='libx264', audio_codec='aac')

# Clean up temporary images
for temp_path in temp_image_files:
    os.remove(temp_path)


