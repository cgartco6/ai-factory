from workers.llm import LLMWorker
import json


class Planner:

    def __init__(self):
        self.llm = LLMWorker()

    def create_plan(self, goal: str):

        prompt = f"""
Create production JSON plan:

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

        output = self.llm.generate(prompt)

        try:
            return json.loads(output)
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
