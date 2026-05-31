from workers.video import VideoWorker
from workers.music import MusicWorker
from workers.voice import VoiceWorker


video = VideoWorker()
music = MusicWorker()
voice = VoiceWorker()


def process_scene(scene):

    return {
        "video": video.generate(scene["visual"]),
        "music": music.generate(scene["music"]),
        "voice": voice.generate(scene["voice"]),
        "duration": scene["duration"]
    }
