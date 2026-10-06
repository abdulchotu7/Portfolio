"""Build the two single-column resumes from the reviewed shared profile.

Run with the Codex bundled Python (reportlab and pypdf), or an environment
containing those packages. Shared facts belong in content/profile.json;
resume-only wording and achievements belong in content/resume_extras.json.
"""
from pathlib import Path
import json
from html import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Flowable
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PROFILE = json.loads((ROOT / "content/profile.json").read_text())
EXTRAS_PATH = ROOT / "content/resume_extras.json"
EXTRAS = json.loads(EXTRAS_PATH.read_text()) if EXTRAS_PATH.exists() else {}
OUT = ROOT / "output/pdf"
FONT_DIR = ROOT / "assets/fonts"
INK = colors.black
MUTED = colors.HexColor("#454545")


class DatedLine(Flowable):
    """One text row with a right-aligned date or link, without a layout table."""
    def __init__(self, left, right, left_style, right_style, right_markup=None):
        super().__init__()
        self.left = Paragraph(left, left_style)
        self.right = Paragraph(right_markup if right_markup is not None else escape(right), right_style)
        self.date_width = pdfmetrics.stringWidth(right, right_style.fontName, right_style.fontSize) + 2
        self.spaceBefore = left_style.spaceBefore
        self.spaceAfter = left_style.spaceAfter
        self.keepWithNext = True

    def wrap(self, width, height):
        self.width = width
        self.left_width = width - self.date_width - 18
        _, lh = self.left.wrap(self.left_width, height)
        _, rh = self.right.wrap(self.date_width, height)
        self.height = max(lh, rh)
        return width, self.height

    def draw(self):
        self.left.drawOn(self.canv, 0, 0)
        self.right.drawOn(self.canv, self.width - self.date_width, 0)


def setup_fonts():
    # Bundled local font copies make the PDFs reproducible on another machine.
    for suffix, filename in [("", "Carlito-Regular.ttf"), ("-Bold", "Carlito-Bold.ttf"), ("-Italic", "Carlito-Italic.ttf")]:
        pdfmetrics.registerFont(TTFont("Carlito" + suffix, str(FONT_DIR / filename)))
    registerFontFamily("Carlito", normal="Carlito", bold="Carlito-Bold", italic="Carlito-Italic", boldItalic="Carlito-Bold")


def build(focus):
    p = PROFILE
    f = p["focus"][focus]
    wording = EXTRAS.get("focus", {}).get(focus, {})
    styles = {
        "name": ParagraphStyle("name", fontName="Carlito-Bold", fontSize=25, leading=28, textColor=INK, spaceAfter=3, alignment=TA_CENTER),
        "headline": ParagraphStyle("headline", fontName="Carlito-Bold", fontSize=11.5, leading=15, textColor=INK, spaceAfter=5, alignment=TA_CENTER),
        "contact": ParagraphStyle("contact", fontName="Carlito", fontSize=9.6, leading=12.5, textColor=MUTED, alignment=TA_CENTER),
        "section": ParagraphStyle("section", fontName="Carlito-Bold", fontSize=10.5, leading=13, textColor=INK, spaceBefore=8, spaceAfter=4, keepWithNext=True),
        "body": ParagraphStyle("body", fontName="Carlito", fontSize=10.4, leading=13.3, textColor=INK, spaceAfter=3),
        "title": ParagraphStyle("title", fontName="Carlito-Bold", fontSize=11, leading=14, textColor=INK, spaceBefore=5, spaceAfter=2, keepWithNext=True),
        "meta": ParagraphStyle("meta", fontName="Carlito", fontSize=9.5, leading=12.2, textColor=MUTED, spaceAfter=2, keepWithNext=True),
        "bullet": ParagraphStyle("bullet", fontName="Carlito", fontSize=10.4, leading=13, textColor=INK, leftIndent=11, firstLineIndent=0, bulletIndent=0, spaceAfter=2.5),
        "skill": ParagraphStyle("skill", fontName="Carlito", fontSize=10.2, leading=13, textColor=INK, spaceAfter=2),
    }
    styles["date"] = ParagraphStyle("date", parent=styles["meta"], alignment=TA_RIGHT, leading=14)
    styles["project_link"] = ParagraphStyle("project_link", parent=styles["title"], fontSize=9, alignment=TA_RIGHT, spaceBefore=0, spaceAfter=0)
    if focus == "ai":
        # Keep the expanded skills on one page without reducing type size.
        styles["section"].spaceBefore = 6
        styles["title"].spaceBefore = 4
        styles["bullet"].spaceAfter = 2
    story = []
    md = [f'# {p["name"]}', f["headline"], f'{p["phone"]} | {p["email"]} | {p["location"]}', f'GitHub: {p["github"]} | LinkedIn: {p["linkedin"]}', ""]

    def para(text, kind="body"):
        return Paragraph(text, styles[kind])

    def section(label):
        story.append(para(label.upper(), "section"))
        md.extend([f"## {label}", ""])

    def bullets(items, links=None):
        for text in items:
            formatted = escape(text)
            markdown = text
            for label, url in (links or {}).items():
                formatted = formatted.replace(escape(label), f'<link href="{escape(url, quote=True)}"><u>{escape(label)}</u></link>')
                markdown = markdown.replace(label, f'[{label}]({url})')
            story.append(Paragraph(formatted, styles["bullet"], bulletText="-"))
            md.append(f"- {markdown}")
        md.append("")

    story.extend([
        para(escape(p["name"]), "name"),
        para(escape(f["headline"]), "headline"),
        para(f'{escape(p["phone"])} &nbsp;|&nbsp; <link href="mailto:{p["email"]}">{p["email"]}</link> &nbsp;|&nbsp; {p["location"]}', "contact"),
        para(f'<link href="{p["github"]}">github.com/abdulchotu7</link> &nbsp;|&nbsp; <link href="{p["linkedin"]}">linkedin.com/in/abdul-rahim-c</link>', "contact"),
        Spacer(1, 7),
        HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#333333")),
    ])
    summary = wording.get("summary", f["summary"])
    if summary:
        section("Summary")
        story.append(para(escape(summary)))
        md.extend([summary, ""])
    section("Experience")
    exp = p["experience"]
    story.append(DatedLine(f'{escape(exp["title"])} | {escape(exp["company"])}', exp["dates"], styles["title"], styles["date"]))
    story.append(para(escape(exp["location"]), "meta"))
    md.extend([f'### {exp["title"]} | {exp["company"]}', f'{exp["dates"]} | {exp["location"]}', ""])
    bullets(wording.get("experience", exp[focus]))
    section("Projects")
    for key in f["projects"]:
        project = p["projects"][key]
        # Keep the title and clickable repository link on one row.
        story.append(DatedLine(escape(project["name"]), "GitHub", styles["title"], styles["project_link"],
                               right_markup=f'<link href="{escape(project["url"], quote=True)}"><u>GitHub</u></link>'))
        story.append(para(escape(project["stack"]), "meta"))
        md.extend([f'### [{project["name"]}]({project["url"]})', project["stack"], ""])
        bullets(wording.get("projects", {}).get(key, project[focus]))
    section("Technical skills")
    for label, values in f["skills"]:
        story.append(para(f"<b>{escape(label)}:</b> {escape(values)}", "skill"))
        md.append(f"- **{label}:** {values}")
    md.append("")
    section("Education")
    e = p["education"]
    story.append(para(f'<b>{escape(e["degree"])}</b> | {escape(e["school"])}'))
    story.append(DatedLine(escape(e["detail"]), e["dates"], styles["meta"], styles["date"]))
    md.extend([f'{e["degree"]} | {e["school"]}', f'{e["detail"]} | {e["dates"]}', ""])

    if EXTRAS.get("achievements_confirmed") and EXTRAS.get("achievements"):
        section("DSA & achievements")
        bullets(EXTRAS["achievements"], EXTRAS.get("coding_profiles"))

    filename = "Abdul_Rahim_AI_Engineer.pdf" if focus == "ai" else "Abdul_Rahim_Software_Engineer.pdf"
    destination = OUT / filename
    doc = SimpleDocTemplate(str(destination), pagesize=A4, leftMargin=39, rightMargin=39, topMargin=28, bottomMargin=28,
                            title=f'{p["name"]} - {f["headline"]}', author=p["name"], subject=f["label"] + " resume")
    def page_background(canvas, document):
        canvas.saveState()
        canvas.setFillColor(colors.white)
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        canvas.restoreState()

    doc.build(story, onFirstPage=page_background, onLaterPages=page_background)
    (OUT / filename.replace(".pdf", ".md")).write_text("\n".join(md))
    reader = PdfReader(destination)
    if len(reader.pages) != 1:
        raise RuntimeError(f"{filename}: expected one page, got {len(reader.pages)}; revise spacing or content")
    text = reader.pages[0].extract_text()
    for required in [p["name"], "EXPERIENCE", "PROJECTS", "TECHNICAL SKILLS", "EDUCATION"]:
        assert required in text, f"Missing extracted content: {required}"
    assert "Kubernetes" not in text and "Jenkins" not in text
    if EXTRAS.get("achievements_confirmed"):
        for required in ["DSA & ACHIEVEMENTS", "700+", "3-star", "2nd place", "SRM CodeClash"]:
            assert required in text, f"Missing confirmed achievement: {required}"
    print(f"Built {destination}: one page, {len(text.split())} extracted words")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    setup_fonts()
    for focus in ("ai", "swe"):
        build(focus)
