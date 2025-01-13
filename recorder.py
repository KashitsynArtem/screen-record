from typing import Any

import cv2
import numpy as np
import mss

from utils.current_monitor import get_current_monitor
from utils.current_time import get_current_time


class ScreenRecorder:
    """
        A class for screen recording with customizable video parameters and capture area.
        Basic Usage::
            from recorder import ScreenRecorder

            record = ScreenRecorder()

            record.start_record()
    """
    def __init__(
            self,
            screen_width: int = None,
            screen_height: int = None,
            top_capture_area: int = 0,
            left_capture_area: int = 0,
            fps: int = 30,
            video_codec: str = 'XVID',
            video_format: str = 'avi',
            output_path: str = '',
            stop_record_key: str = 'q',
            imshow_mode: bool = True
    ):
        """
        :param screen_width: Width of the screen to capture (default: None - auto-detect).
        :param screen_height: Height of the screen to capture (default: None - auto-detect).
        :param top_capture_area: Top boundary of the capture area (default: 0).
        :param left_capture_area: Left boundary of the capture area (default: 0).
        :param fps: Frames per second for video recording (default: 30).
        :param video_codec: Codec for video compression (e.g., 'XVID') (default: 'XVID').
        :param video_format: Output video format (e.g., 'avi') (default: 'avi').
        :param output_path: Path for saving the output video (default: '').
        :param stop_record_key: Key to stop recording (e.g., 'q') (default: 'q').
        :param imshow_mode: Display mode for showing captured video in a window (default: True).
        """
        # monitor
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.monitor = None

        # video params
        self.fps = fps
        self.video_codec = video_codec
        self.video_format = video_format

        # capture area
        self.top_capture_area = top_capture_area
        self.left_capture_area = left_capture_area

        # output
        self.imshow_mode = imshow_mode
        self.output_path = output_path
        self.sct = None
        self.video_writer = None

        # keys
        self.stop_record_key = stop_record_key

    def init_monitor(self) -> dict[Any, int]:

        current_monitor = get_current_monitor()
        self.screen_width, self.screen_height = current_monitor

        monitor = {
            'top': self.top_capture_area,
            'left': self.left_capture_area,
            'width': self.screen_width,
            'height': self.screen_height
        }

        return monitor

    def init_video_writer(self) -> cv2.VideoWriter:
        # current time
        time = get_current_time()

        # screen
        self.sct = mss.mss()

        # video writer
        fourcc = cv2.VideoWriter_fourcc(*self.video_codec)
        video_writer = cv2.VideoWriter(f'{self.output_path}{time}.{self.video_format}', fourcc, self.fps, (self.screen_width, self.screen_height))

        return video_writer

    def start_record(self):
        self.monitor = self.init_monitor()
        self.video_writer = self.init_video_writer()

        while True:
            # capture screen
            img = self.sct.grab(self.monitor)

            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            self.video_writer.write(frame)

            if self.imshow_mode:
                cv2.imshow('Screen Recorder', frame)

            if cv2.waitKey(1) & 0xFF == ord(self.stop_record_key):
                break

        self.stop_record()

    def stop_record(self):
        self.video_writer.release()
        cv2.destroyAllWindows()
