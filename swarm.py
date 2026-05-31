from workers.video import VideoWorker
from workers.music import MusicWorker
from workers.voice import VoiceWorker


class Swarm:

    def __init__(self):

        self.video = VideoWorker()
        self.music = MusicWorker()
        self.voice = VoiceWorker()

    def run(self, scene):

        return {
            "video": self.video.generate(scene["visual_prompt"]),
            "music": self.music.generate(scene["music_prompt"]),
            "voice": self.voice.generate(scene["voice_script"]),
            "duration": scene["duration"]
        }
