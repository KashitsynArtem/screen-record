import ctypes
from typing import Any


def get_current_monitor() -> tuple[Any, int]:
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    return screensize
