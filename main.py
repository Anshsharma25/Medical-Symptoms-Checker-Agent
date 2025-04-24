import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_community.llms import HuggingFaceHub
from tools.followup_tool import FollowUpTool
from tools.diagnosis_tool import DiagnoseTool
from tools.report_tool import ReportTool

load_dotenv()  # Load .env file
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceHub(
    repo_id="google/flan-t5-xl",
    huggingfacehub_api_token=hf_token
)

tools = [FollowUpTool(), DiagnoseTool(), ReportTool()]
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

if __name__ == "__main__":
    user_input = input("Enter your symptoms: ")
    language = input("Choose language (en for English, hi for Hindi): ")
    output = agent.run({"input": user_input, "language": language})
    print("\nReport generated! Check outputs/ folder.")


