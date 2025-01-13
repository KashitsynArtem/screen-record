# Screen Recorder

A simple code for recording screen video for Windows, without sound

## Requirements:

```git clone https://github.com/yourusername/screen-recorder.git```

You can install the required packages using pip:

```bash
pip install opencv-python numpy mss
```

You can install the required packages using poetry:

```bash
pip install poetry
poetry install
```

### Minimal Usage:

```python
from recorder import ScreenRecorder

record = ScreenRecorder()
record.start_record()
# Key to stop recording - q
```

### Base Usage:

```python
from recorder import Recorder

# Create a Recorder instance
recorder = Recorder(
    screen_width=1920,
    screen_height=1080,
    top_capture_area=0,
    left_capture_area=0,
    fps=30,
    video_codec='XVID',
    video_format='avi',
    output_path='output/',
    stop_record_key='q',
    imshow_mode=True
)

# Start recording
recorder.start_record()
# Key to stop recording - q
```

### Parameters:

`screen_width`: Width of the screen to capture (default: None - auto-detect).

`screen_height`: Height of the screen to capture (default: None - auto-detect).

`top_capture_area`: Top boundary of the capture area (default: 0).

`left_capture_area`: Left boundary of the capture area (default: 0).

`fps`: Frames per second for video recording (default: 30).

`video_codec`: Codec for video compression (e.g., 'XVID') (default: 'XVID').

`video_format`: Output video format (e.g., 'avi') (default: 'avi').

`output_path`: Path for saving the output video (default: '').

`stop_record_key`: Key to stop recording (e.g., 'q') (default: 'q').

`imshow_mode`: Display mode for showing captured video in a window (default: True).
