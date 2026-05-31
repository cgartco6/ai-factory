class VideoWorker:

    def generate(self, prompt):

        return {
            "file": f"video_{hash(prompt)}.mp4",
            "prompt": prompt
        }
