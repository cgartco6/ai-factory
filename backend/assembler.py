import subprocess


class Assembler:

    def build_video(self, video_files, audio_files, output="final.mp4"):

        # simplified FFmpeg merge (real hook point)
        cmd = [
            "ffmpeg",
            "-y",
            "-i", video_files[0],
            "-i", audio_files[0],
            "-c:v", "copy",
            "-c:a", "aac",
            output
        ]

        try:
            subprocess.run(cmd, check=True)
        except Exception as e:
            print("FFmpeg failed:", e)

        return output
