
# Video Creation from Images and Audio

This project automates the process of creating a video from a series of images, synchronized with an audio file. The final video is tailored for platforms that support short video content, such as YouTube Shorts.

## Features

- **Image Resizing**: Automatically resizes images to fit the desired video format (1080x1920 pixels for YouTube Shorts).
- **Audio Synchronization**: Adjusts the video length to exactly match the duration of the audio.
- **Flexible Image Input**: Supports a dynamic number of images and adjusts the video duration accordingly.

## Prerequisites

Before you can run this script, you need to have Python installed along with the following packages:
- moviepy
- PIL (Pillow)

You can install these packages using pip:

\`\`\`bash
pip install moviepy Pillow
\`\`\`

## Setup

1. Clone this repository or download the files to your local machine.
2. Place your image and audio files in the designated media folder (e.g., `media_folder`).

## Usage

To run the script, navigate to the script's directory in your terminal and run:

\`\`\`bash
python script_name.py
\`\`\`

Ensure that you update the `media_folder` and `audio_file` variables in the script to point to the correct locations of your media files.

## Output

The script will output a video file named `output_video.mp4` in the same directory as the script. This video will have all images displayed for a duration that matches the audio file length, resized and formatted for optimal viewing on mobile devices in portrait orientation.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.

## License

This project is released under the MIT License. See the `LICENSE` file for more details.

## Contact

For any queries or technical support, please open an issue in the repository. 
