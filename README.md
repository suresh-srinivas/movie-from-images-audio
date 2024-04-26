
# Video Concatenation and Image Handling Script

This project is designed to automate the process of creating videos by concatenating multiple MP4 files and synchronizing them with images and optional audio. The output is specifically formatted for platforms that prefer vertical video formats, such as YouTube Shorts.

## Features

- **Video Concatenation**: Combines multiple MP4 files into a single video.
- **Image Handling**: Dynamically adjusts the display time of images based on the total video duration to fit within a predefined limit (e.g., 60 seconds).
- **Audio Synchronization**: Synchronizes audio with the video, applying it over images or videos based on configuration.
- **Output Formatting**: Ensures the final video is in the vertical format (1080x1920), suitable for mobile viewing.

## Prerequisites

Before running this script, ensure you have Python installed along with the following packages:
- moviepy
- PIL (Pillow)

Install the required packages using pip:

```bash
pip install moviepy Pillow
```

## Setup

1. Clone this repository or download the scripts to your local machine.
2. Organize your media files (MP4, JPEG, MP3) in a designated media folder.

## Usage

To use this script, update the `media_folder` variable in the script to point to your media folder. Configure the script to place images at the beginning or the end of the video by setting `images_at_start` to `True` or `False`.

Run the scripts with:

```bash
python movie-from-images-audio.py # for images and audio
python movie-from-images-audio-video.py # for images, audio, and video or just video
```

## Output

The script will produce an `output_video.mp4` file in the specified format, combining all input media with optional audio synchronization.

## Contributing

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is released under the MIT License. See the LICENSE file for more details.

## Contact

For support or queries, please open an issue on the repo.

