from workers.llm import LLMWorker
import json


class Planner:

    def __init__(self):
        self.llm = LLMWorker()

    def create_plan(self, goal: str):

        prompt = f"""
Break into production scenes JSON:

Goal: {goal}

Return:
{{
  "scenes": [
    {{
      "id": 1,
      "visual": "",
      "music": "",
      "voice": "",
      "duration": 5
    }}
  ]
}}
"""

        out = self.llm.generate(prompt)

        try:
            return json.loads(out)
        except:
            return {
                "scenes": [
                    {
                        "id": 1,
                        "visual": goal,
                        "music": "cinematic",
                        "voice": goal,
                        "duration": 5
                    }
                ]
            }
