from langchain_core.tools import BaseTool
from fpdf import FPDF
from utils.tts import speak_report


class ReportTool(BaseTool):
    name: str = "ReportTool"
    description: str = "Generate a PDF and MP3 report."

    def _run(self, input: dict):
        symptoms = input["input"]
        language = input["language"]
        report_text = f"Medical Report\n\nSymptoms: {symptoms}\nDiagnosis: Possible viral bronchitis.\nRecommendation: Consult a doctor."

        # Generate PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in report_text.split("\n"):
            pdf.cell(200, 10, txt=line, ln=True)
        pdf.output("outputs/medical_report.pdf")

        # Generate MP3
        speak_report(report_text, language=language)
        return "Report generated."

    def _arun(self, input: dict):
        raise NotImplementedError("This tool does not support async.")
