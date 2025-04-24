from langchain_core.tools import BaseTool

class DiagnoseTool(BaseTool):
    name: str = "DiagnoseTool"
    description: str = "Suggest possible medical conditions."

    def _run(self, input: dict):
        symptoms = input["input"]
        return f"Based on symptoms like {symptoms}, the user might have viral bronchitis or cold."

    def _arun(self, input: dict):
        raise NotImplementedError("This tool does not support async.")
