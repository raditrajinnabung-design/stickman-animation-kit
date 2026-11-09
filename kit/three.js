from dataclasses import dataclass

@dataclass
class Timeline:
    fps: int = 30

    def seconds_to_frames(self, seconds: float) -> int:
        return round(seconds * self.fps)

    def frames_to_seconds(self, frames: int) -> float:
        return frames / self.fps

    def duration(self, start: int, end: int) -> float:
        return (end - start) / self.fps


def calculate_frames(duration: float, fps: int = 30) -> int:
    return round(duration * fps)
