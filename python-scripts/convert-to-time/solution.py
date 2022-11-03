import datetime

def get_time(seconds: int):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

def main(seconds: int) -> str:
    if seconds < 0: 
      return f"-{get_time(seconds*-1)}"
    else:
      return get_time(seconds)

