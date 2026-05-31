class MusicWorker:

    def generate(self, prompt):

        return {
            "file": f"music_{hash(prompt)}.mp3",
            "prompt": prompt
        }
