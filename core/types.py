from dataclasses import dataclass
from typing import List


@dataclass
class Scene:
    id: int
    visual_prompt: str
    music_prompt: str
    voice_script: str
    duration: int
