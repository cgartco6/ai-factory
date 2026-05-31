class MusicWorker:

    def generate(self, prompt: str):

        return {
            "type": "music",
            "file": f"music_{hash(prompt)}.mp3",
            "prompt": prompt
        }
