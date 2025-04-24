from langchain_core.tools import BaseTool

class FollowUpTool(BaseTool):
    name: str = "FollowUpTool"
    description: str = "Ask medical follow-up questions based on initial symptoms."

    def _run(self, input: dict):
        symptoms = input["input"]
        return f"Have you experienced chest pain or shortness of breath with {symptoms}?"

    def _arun(self, input: dict):
        raise NotImplementedError("This tool does not support async.")
