import json
import yaml
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Load params
params = yaml.safe_load(open("params.yaml"))["reporting"]

# Load metrics
with open("metrics/portfolio_performance.json") as f:
    performance = json.load(f)
with open("metrics/budget_adherence.json") as f:
    budget = json.load(f)

# Generate PDF
report_path = Path("reports/summary_report.pdf")
report_path.parent.mkdir(parents=True, exist_ok=True)

doc = SimpleDocTemplate(str(report_path))
styles = getSampleStyleSheet()
story = []

story.append(Paragraph("Financial Analysis Report", styles["Title"]))
story.append(Spacer(1, 20))

story.append(Paragraph(f"Currency Symbol: {params['currency_symbol']}", styles["Normal"]))
story.append(Spacer(1, 12))

story.append(Paragraph("Portfolio Performance:", styles["Heading2"]))
for k, v in performance.items():
    story.append(Paragraph(f"{k}: {v}", styles["Normal"]))

story.append(Spacer(1, 12))
story.append(Paragraph("Budget Adherence:", styles["Heading2"]))
for k, v in budget.items():
    story.append(Paragraph(f"{k}: {v}", styles["Normal"]))

doc.build(story)
