# -*- coding: utf-8 -*-
import json
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                 Image, PageBreak, HRFlowable, KeepTogether)
from reportlab.lib.enums import TA_CENTER, TA_LEFT

from data import papers
from difficulty import rubric, comparison_notes

CHARTS = "/home/claude/charts"
OUT_PDF = "/home/claude/outputs/Question_Paper_Analytics_Report.pdf"
import os
os.makedirs("/home/claude/outputs", exist_ok=True)

with open("/home/claude/analytics.json") as f:
    analytics = json.load(f)

# ---------------------------------------------------------------------- styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleBig", fontSize=25, leading=30, alignment=TA_CENTER,
                           fontName="Helvetica-Bold", textColor=colors.HexColor("#1B2A4A"),
                           spaceAfter=6))
styles.add(ParagraphStyle(name="SubTitle", fontSize=13.5, leading=18, alignment=TA_CENTER,
                           fontName="Helvetica", textColor=colors.HexColor("#44506B"),
                           spaceAfter=4))
styles.add(ParagraphStyle(name="SectionHead", fontSize=17, leading=21, spaceBefore=6,
                           spaceAfter=10, fontName="Helvetica-Bold",
                           textColor=colors.HexColor("#1B2A4A")))
styles.add(ParagraphStyle(name="SubHead", fontSize=13, leading=16, spaceBefore=10,
                           spaceAfter=6, fontName="Helvetica-Bold",
                           textColor=colors.HexColor("#2E5EAA")))
styles.add(ParagraphStyle(name="Body", fontSize=10, leading=14.5, spaceAfter=6,
                           fontName="Helvetica", alignment=TA_LEFT))
styles.add(ParagraphStyle(name="BodyCenter", fontSize=10, leading=14.5, spaceAfter=6,
                           fontName="Helvetica", alignment=TA_CENTER))
styles.add(ParagraphStyle(name="Small", fontSize=8.3, leading=11, textColor=colors.HexColor("#666666")))
styles.add(ParagraphStyle(name="TableCell", fontSize=8.7, leading=11, fontName="Helvetica"))
styles.add(ParagraphStyle(name="TableCellBold", fontSize=8.9, leading=11, fontName="Helvetica-Bold"))

NAVY = colors.HexColor("#1B2A4A")
BLUE = colors.HexColor("#2E5EAA")
LIGHT = colors.HexColor("#EEF1F8")
GREY = colors.HexColor("#F5F5F5")

story = []

# =========================================================================
# TITLE PAGE
# =========================================================================
story.append(Spacer(1, 3.2 * cm))
story.append(Paragraph("Question Paper Analytics Report", styles["TitleBig"]))
story.append(Paragraph("Chapter-wise Weightage Analysis &amp; Difficulty Assessment", styles["SubTitle"]))
story.append(Spacer(1, 0.6 * cm))
story.append(HRFlowable(width="60%", thickness=1.2, color=BLUE, hAlign="CENTER"))
story.append(Spacer(1, 1.0 * cm))

cover_table = Table(
    [["Paper", "Year", "Total Questions", "Subjects"],
     ["AIPMT", "2014", "180", "Physics, Chemistry, Biology"],
     ["AIIMS", "2013", "200", "Physics, Chemistry, Biology, General Knowledge"]],
    colWidths=[3.2 * cm, 2.4 * cm, 3.4 * cm, 7.3 * cm])
cover_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 9.5),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
]))
story.append(cover_table)
story.append(Spacer(1, 2.0 * cm))
story.append(Paragraph(
    "This report classifies every question from the two uploaded papers against its "
    "NCERT (Class XI-XII) chapter, quantifies chapter-wise and subject-wise weightage, "
    "and closes with an evidence-based difficulty rating for each paper.",
    styles["BodyCenter"]))
story.append(Spacer(1, 3.5 * cm))
story.append(Paragraph("Prepared by Claude · Analytics based on the uploaded question papers and official answer keys",
                        styles["Small"]))
story.append(PageBreak())

# =========================================================================
# METHODOLOGY
# =========================================================================
story.append(Paragraph("Methodology", styles["SectionHead"]))
story.append(Paragraph(
    "Every question in both papers was read individually and mapped to the single NCERT "
    "chapter it most directly tests, using the official solutions printed with each paper "
    "to confirm the underlying concept. Counts were then aggregated subject-wise and "
    "chapter-wise to compute weightage (% of that subject's questions). For Biology, "
    "chapters were additionally rolled up into the 10 standard NCERT units for a "
    "higher-level view, since Biology alone spans 30+ chapters in each paper. "
    "The General Knowledge section of the AIIMS paper (non-syllabus) is reported separately "
    "by broad topic rather than NCERT chapter.", styles["Body"]))
story.append(Paragraph(
    "Difficulty was then rated out of 10 using four weighted factors — conceptual depth, "
    "numerical/calculation load, question-format trickiness (e.g. assertion-reason), and "
    "syllabus breadth relative to time available — explained in full at the end of this "
    "report.", styles["Body"]))
story.append(PageBreak())


def fmt_num(x):
    return f"{x:.1f}" if isinstance(x, float) else str(x)


def add_chapter_table(counts_items, total, title):
    data = [["#", "Chapter", "Questions", "Weightage"]]
    for i, (chap, cnt) in enumerate(counts_items, 1):
        pct = 100 * cnt / total
        data.append([str(i), Paragraph(chap, styles["TableCell"]), str(cnt), f"{pct:.1f}%"])
    t = Table(data, colWidths=[0.9 * cm, 9.6 * cm, 2.3 * cm, 2.6 * cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, GREY]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("ALIGN", (2, 0), (3, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2),
    ]))
    return t


def subject_section(paper, subject, chart_file, extra_chart=None, extra_title=None):
    total = analytics[paper]["_subject_totals"][subject]
    items = analytics[paper][subject]
    story.append(Paragraph(f"{paper} — {subject}", styles["SubHead"]))
    story.append(Paragraph(f"Total questions: <b>{total}</b> &nbsp;|&nbsp; "
                            f"Chapters touched: <b>{len(items)}</b>", styles["Body"]))
    story.append(Image(f"{CHARTS}/{chart_file}", width=16.5 * cm,
                        height=16.5 * cm * (Image(f"{CHARTS}/{chart_file}").imageHeight /
                                             Image(f"{CHARTS}/{chart_file}").imageWidth)))
    story.append(Spacer(1, 0.3 * cm))
    story.append(add_chapter_table(items, total, subject))
    if extra_chart:
        story.append(Spacer(1, 0.4 * cm))
        story.append(Paragraph(extra_title, styles["Body"]))
        story.append(Image(f"{CHARTS}/{extra_chart}", width=13 * cm,
                            height=13 * cm * (Image(f"{CHARTS}/{extra_chart}").imageHeight /
                                               Image(f"{CHARTS}/{extra_chart}").imageWidth)))
    story.append(PageBreak())


# =========================================================================
# PAPER SECTIONS
# =========================================================================
for paper in ["AIPMT 2014", "AIIMS 2013"]:
    story.append(Paragraph(f"{paper}: Chapter-wise Weightage Analysis", styles["SectionHead"]))
    story.append(Paragraph(
        f"Overall distribution across subjects for {paper}:", styles["Body"]))
    story.append(Image(f"{CHARTS}/{paper.replace(' ', '_')}_subject_split.png",
                        width=12 * cm, height=12 * cm * 4.6 / 6.4))
    story.append(PageBreak())

    subject_section(paper, "Physics", f"{paper.replace(' ', '_')}_Physics_bar.png")
    subject_section(paper, "Chemistry", f"{paper.replace(' ', '_')}_Chemistry_bar.png")
    subject_section(paper, "Biology", f"{paper.replace(' ', '_')}_Biology_bar.png",
                     extra_chart=f"{paper.replace(' ', '_')}_Biology_units_pie.png",
                     extra_title="Biology questions rolled up to NCERT Unit level (10 units):")

    if "General Knowledge" in analytics[paper]:
        subject_section(paper, "General Knowledge",
                         f"{paper.replace(' ', '_')}_General_Knowledge_bar.png")

# =========================================================================
# CROSS-PAPER COMPARISON
# =========================================================================
story.append(Paragraph("Cross-Paper Comparison", styles["SectionHead"]))
story.append(Image(f"{CHARTS}/comparison_subjects.png", width=14.5 * cm,
                    height=14.5 * cm * 4.8 / 7.5))
story.append(Spacer(1, 0.4 * cm))

comp_data = [["Aspect", "AIPMT 2014", "AIIMS 2013"]]
for row in comparison_notes:
    comp_data.append([Paragraph(row[0], styles["TableCellBold"]),
                       Paragraph(row[1], styles["TableCell"]),
                       Paragraph(row[2], styles["TableCell"])])
comp_table = Table(comp_data, colWidths=[4.6 * cm, 5.4 * cm, 5.4 * cm], repeatRows=1)
comp_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 9.5),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story.append(comp_table)
story.append(PageBreak())

# =========================================================================
# DIFFICULTY RATING
# =========================================================================
story.append(Paragraph("Difficulty Rating", styles["SectionHead"]))
story.append(Paragraph(
    "Each paper is scored out of 10 on four weighted factors (each out of 10), then "
    "averaged to an overall rating. Higher = harder.", styles["Body"]))
story.append(Spacer(1, 0.2 * cm))

for paper in ["AIPMT 2014", "AIIMS 2013"]:
    r = rubric[paper]
    story.append(Paragraph(f"{paper} — Overall Difficulty: "
                            f"<font color='#B23A48'><b>{r['overall']:.1f} / 10</b></font> "
                            f"&nbsp;({r['verdict']})", styles["SubHead"]))
    rdata = [["Factor", "Score /10", "Rationale"]]
    for name, score, note in r["params"]:
        rdata.append([Paragraph(name, styles["TableCellBold"]),
                       Paragraph(f"{score:.1f}", styles["TableCell"]),
                       Paragraph(note, styles["TableCell"])])
    rtable = Table(rdata, colWidths=[3.6 * cm, 1.9 * cm, 9.9 * cm], repeatRows=1)
    rtable.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, GREY]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("ALIGN", (1, 0), (1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(rtable)
    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph(r["summary"], styles["Body"]))
    story.append(Spacer(1, 0.5 * cm))

story.append(HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#CCCCCC")))
story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph(
    "<b>Bottom line:</b> AIPMT 2014 rates <b>6.0 / 10</b> (Moderate) — a fair, "
    "recall-and-standard-formula paper typical of NEET-pattern exams. AIIMS 2013 rates "
    "<b>7.7 / 10</b> (Difficult) — its Assertion-Reason format and broader GK component "
    "make it meaningfully harder question-for-question, even though both papers draw on "
    "the same core NCERT syllabus.", styles["Body"]))

# =========================================================================
doc = SimpleDocTemplate(OUT_PDF, pagesize=A4,
                         leftMargin=1.6 * cm, rightMargin=1.6 * cm,
                         topMargin=1.5 * cm, bottomMargin=1.5 * cm,
                         title="Question Paper Analytics Report")
doc.build(story)
print("PDF written to", OUT_PDF)