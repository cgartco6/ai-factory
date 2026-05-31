class VoiceWorker:

    def generate(self, text):

        return {
            "file": f"voice_{hash(text)}.mp3",
            "text": text
        }
