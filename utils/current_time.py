from datetime import datetime


def get_current_time() -> str:
    now = datetime.now()
    current_time = now.strftime('%d-%m-%Y-%H-%M-%S')

    return current_time
