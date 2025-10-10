# generate_report.py

import json
import yaml
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# ------------------------
# Load params
# ------------------------
params = yaml.safe_load(open("params.yaml"))["reporting"]
include_charts = params.get("include_charts", True)
currency_symbol = params.get("currency_symbol", "$")

# ------------------------
# Load metrics and insights
# ------------------------
with open("metrics/portfolio_performance.json") as f:
    performance = json.load(f)

with open("metrics/budget_adherence.json") as f:
    budget = json.load(f)

with open("data/analysis/insights.json") as f:
    insights = json.load(f)

# ------------------------
# Generate PDF
# ------------------------
report_path = Path("reports/summary_report.pdf")
report_path.parent.mkdir(parents=True, exist_ok=True)

doc = SimpleDocTemplate(str(report_path))
styles = getSampleStyleSheet()
story = []

story.append(Paragraph("Financial Analysis Report", styles["Title"]))
story.append(Spacer(1, 20))

story.append(Paragraph(f"Currency Symbol: {currency_symbol}", styles["Normal"]))
story.append(Spacer(1, 12))

# Portfolio Performance
story.append(Paragraph("Portfolio Performance:", styles["Heading2"]))
perf_table_data = [["Metric", "Value"]]
for k, v in performance.items():
    perf_table_data.append([k, v])

perf_table = Table(perf_table_data, hAlign="LEFT")
perf_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('GRID', (0,0), (-1,-1), 0.5, colors.black)
]))
story.append(perf_table)
story.append(Spacer(1, 12))

# Budget Adherence
story.append(Paragraph("Budget Adherence:", styles["Heading2"]))
adherence_table_data = [["Category", "Over/Under Budget"]]
for k, v in budget.get("category_adherence", {}).items():
    adherence_table_data.append([k, v])

adherence_table = Table(adherence_table_data, hAlign="LEFT")
adherence_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('GRID', (0,0), (-1,-1), 0.5, colors.black)
]))
story.append(adherence_table)
story.append(Spacer(1, 12))

# Insights (optional additional summary)
story.append(Paragraph("Overall Insights:", styles["Heading2"]))
for k, v in insights.items():
    story.append(Paragraph(f"{k}: {v}", styles["Normal"]))

# Placeholder for charts
if include_charts:
    story.append(Spacer(1, 12))
    story.append(Paragraph("Charts would be inserted here if implemented.", styles["Italic"]))

# Build PDF
doc.build(story)
