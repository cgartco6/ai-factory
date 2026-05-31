class Assembler:

    def build(self, results):

        return {
            "videos": [r["video"]["file"] for r in results],
            "music": [r["music"]["file"] for r in results],
            "voice": [r["voice"]["file"] for r in results]
        }
