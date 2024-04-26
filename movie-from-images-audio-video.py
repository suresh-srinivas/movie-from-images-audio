from moviepy.editor import VideoFileClip, concatenate_videoclips, ImageSequenceClip, CompositeVideoClip, AudioFileClip
from PIL import Image
import os

# Configuration
media_folder = 'path_to_your_media_folder'
desired_size = (1080, 1920)  # YouTube Shorts dimensions
max_duration = 60  # Maximum duration of the final video in seconds
images_at_start = True  # Set to False to place images at the end

# Load audio if available
audio_files = [os.path.join(media_folder, f) for f in os.listdir(media_folder) if f.endswith(('.mp3', '.m4a'))]
audio_clip = AudioFileClip(audio_files[0]) if audio_files else None

# Gather video files and calculate total video duration
video_files = [os.path.join(media_folder, f) for f in os.listdir(media_folder) if f.endswith(".mp4")]
video_clips = [VideoFileClip(f) for f in video_files]
total_video_duration = sum(clip.duration for clip in video_clips)

# Determine available duration for images
available_image_duration = max_duration - total_video_duration
if available_image_duration <= 0:
    raise ValueError("Video files already exceed the maximum duration. No time left for images.")

# Prepare images
image_files = sorted([os.path.join(media_folder, f) for f in os.listdir(media_folder) if f.endswith((".png", ".jpg", ".jpeg"))])
fps = len(image_files) / available_image_duration

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

# Load images into a video clip
clip_images = ImageSequenceClip(temp_image_files, fps=fps)

# Apply audio to the appropriate part
if audio_clip:
    if images_at_start:
        clip_images = clip_images.set_audio(audio_clip.set_duration(clip_images.duration))
    else:
        video_clips[0] = video_clips[0].set_audio(audio_clip.set_duration(video_clips[0].duration))

# Organize clips
if images_at_start:
    clips_to_concatenate = [clip_images] + video_clips
else:
    clips_to_concatenate = video_clips + [clip_images]

# Concatenate all clips
final_clip = concatenate_videoclips(clips_to_concatenate, method="compose")

# Export the final video
final_clip.write_videofile("output_video.mp4", codec="libx264", audio_codec='aac')

# Cleanup
for clip in video_clips + [clip_images]:
    clip.close()
final_clip.close()
for temp_path in temp_image_files:
    os.remove(temp_path)


