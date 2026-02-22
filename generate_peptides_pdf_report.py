#!/usr/bin/env python3
"""
Generate a comprehensive peptide business strategy PDF.
"""

from datetime import date
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUTPUT_PATH = "/workspace/peptides-business-country-market-report-2026.pdf"


def difficulty_color(score: int):
    if score <= 2:
        return colors.HexColor("#D5F5E3")  # green-ish
    if score == 3:
        return colors.HexColor("#FCF3CF")  # yellow-ish
    if score == 4:
        return colors.HexColor("#FAD7A0")  # orange-ish
    return colors.HexColor("#F5B7B1")  # red-ish


def attractiveness_color(score: float):
    if score >= 4.2:
        return colors.HexColor("#D5F5E3")
    if score >= 3.8:
        return colors.HexColor("#E8F8F5")
    if score >= 3.5:
        return colors.HexColor("#FCF3CF")
    return colors.HexColor("#FDEDEC")


def score_bar(score: float, max_score: int = 5) -> str:
    filled = int(round(score))
    filled = max(0, min(max_score, filled))
    return "#" * filled + "-" * (max_score - filled)


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text, style)


def main():
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleCustom",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=19,
        leading=22,
        textColor=colors.HexColor("#0B3C5D"),
        spaceAfter=8,
    )
    h1 = ParagraphStyle(
        "H1",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#0B3C5D"),
        spaceBefore=8,
        spaceAfter=6,
    )
    h2 = ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#1F618D"),
        spaceBefore=6,
        spaceAfter=4,
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13,
        spaceAfter=3,
    )
    body_small = ParagraphStyle(
        "BodySmall",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.4,
        leading=11,
        spaceAfter=2,
    )

    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        rightMargin=1.2 * cm,
        leftMargin=1.2 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
        title="High-Tech Peptide Lab Strategy Report 2026",
        author="AI Research Synthesis",
    )

    story = []
    story.append(p("High-Tech Peptide Lab Strategy Report (2026)", title_style))
    story.append(
        p(
            "Comprehensive format: business models, product ranges, regulatory difficulty map, "
            "best countries, and market projections.",
            body,
        )
    )
    story.append(p(f"Generated: {date.today().isoformat()}", body_small))
    story.append(Spacer(1, 10))

    story.append(p("Executive Recommendation", h1))
    story.append(
        p(
            "Best risk-adjusted positioning: <b>Compliance-first peptide infrastructure lab (B2B)</b> "
            "combining peptide CMC support, analytical method validation, impurity profiling, "
            "reference standards, and supply assurance services.",
            body,
        )
    )
    story.append(
        p(
            "Reason: this captures peptide market growth while avoiding the highest-risk zone "
            "(copy-compounding and gray-market direct-to-consumer peptide sales).",
            body,
        )
    )
    story.append(Spacer(1, 8))

    story.append(p("How to read this report", h2))
    story.append(p("Regulatory Difficulty Scale: 1 Low, 2 Medium-Low, 3 Medium, 4 High, 5 Very High.", body))
    story.append(p("Attractiveness Score: 1 (weak) to 5 (excellent), using demand, access, and risk factors.", body))

    story.append(Spacer(1, 10))
    story.append(p("Business Model Comparison", h1))

    business_models = [
        {
            "model": "Custom Research Reagents Lab",
            "products": "Custom peptides, labeled peptides, libraries, oligos, proteins",
            "range": "High",
            "reg": 2,
            "time": "2-4 months",
            "margin": "Medium-High",
            "rec": "Strong secondary pillar",
        },
        {
            "model": "Analytical Standards + QC Controls",
            "products": "Impurity standards, reference materials, LC-MS controls",
            "range": "Medium-High",
            "reg": 3,
            "time": "4-8 months",
            "margin": "High",
            "rec": "Strong secondary pillar",
        },
        {
            "model": "Peptide CMC + Analytics Platform",
            "products": "CMC packages, validated methods, release testing",
            "range": "High",
            "reg": 4,
            "time": "3-6 months",
            "margin": "High",
            "rec": "BEST PRIMARY MODEL",
        },
        {
            "model": "Diagnostic Reagent Lab",
            "products": "Peptide antigens, assay reagents, biomarker kits",
            "range": "Medium",
            "reg": 4,
            "time": "6-12 months",
            "margin": "Medium-High",
            "rec": "Good expansion option",
        },
        {
            "model": "Cosmetic Peptide Ingredient Supplier",
            "products": "Cosmetic-grade peptide actives and blends",
            "range": "Medium",
            "reg": 3,
            "time": "3-8 months",
            "margin": "Medium",
            "rec": "Optional; crowded segment",
        },
        {
            "model": "Compounded GLP-1 Copy Retail Model",
            "products": "Compounded semaglutide/tirzepatide-like offerings",
            "range": "Narrow",
            "reg": 5,
            "time": "Fast",
            "margin": "Unstable",
            "rec": "AVOID AS CORE",
        },
        {
            "model": "Novel Peptide Drug Developer",
            "products": "Proprietary therapeutic assets",
            "range": "Very High",
            "reg": 5,
            "time": "7-12 years",
            "margin": "Very High if successful",
            "rec": "High risk; long horizon",
        },
    ]

    b_header = [
        p("<b>Business Model</b>", body_small),
        p("<b>Products</b>", body_small),
        p("<b>Range</b>", body_small),
        p("<b>Reg Difficulty</b>", body_small),
        p("<b>Time to Revenue</b>", body_small),
        p("<b>Margin</b>", body_small),
        p("<b>Recommendation</b>", body_small),
    ]
    b_rows = [b_header]
    for row in business_models:
        b_rows.append(
            [
                p(row["model"], body_small),
                p(row["products"], body_small),
                p(row["range"], body_small),
                p(f'{row["reg"]}/5', body_small),
                p(row["time"], body_small),
                p(row["margin"], body_small),
                p(row["rec"], body_small),
            ]
        )

    b_table = Table(
        b_rows,
        colWidths=[4.0 * cm, 5.1 * cm, 1.8 * cm, 1.9 * cm, 2.2 * cm, 2.2 * cm, 3.1 * cm],
        repeatRows=1,
    )
    b_style = TableStyle(
        [
            ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#7B7D7D")),
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F618D")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ]
    )
    for idx, row in enumerate(business_models, start=1):
        b_style.add("BACKGROUND", (3, idx), (3, idx), difficulty_color(row["reg"]))
        if "BEST" in row["rec"]:
            b_style.add("BACKGROUND", (6, idx), (6, idx), colors.HexColor("#D5F5E3"))
        if "AVOID" in row["rec"]:
            b_style.add("BACKGROUND", (6, idx), (6, idx), colors.HexColor("#F5B7B1"))
    b_table.setStyle(b_style)
    story.append(b_table)

    story.append(Spacer(1, 10))
    story.append(p("Product Range Architecture (12-Month Buildout)", h1))

    product_rows = [
        [
            p("<b>Segment</b>", body_small),
            p("<b>Examples</b>", body_small),
            p("<b>Initial SKU / Offer Range</b>", body_small),
            p("<b>Reg Difficulty</b>", body_small),
            p("<b>Visual</b>", body_small),
        ],
        [
            p("Research-grade products", body_small),
            p("Custom peptides, labeled peptides, libraries, oligos, proteins", body_small),
            p("20-40 catalog SKUs + custom synthesis in first 3 months", body_small),
            p("2/5", body_small),
            p("##---", body_small),
        ],
        [
            p("Analytical/QC products", body_small),
            p("Reference standards, impurity standards, LC-MS suitability controls", body_small),
            p("Add 30-60 SKUs by month 6", body_small),
            p("3/5", body_small),
            p("###--", body_small),
        ],
        [
            p("Service products (B2B recurring)", body_small),
            p("CMC readiness, method validation, release/stability support", body_small),
            p("2 fixed packages by month 6, then custom contracts", body_small),
            p("4/5", body_small),
            p("####-", body_small),
        ],
        [
            p("Diagnostic reagents (expansion)", body_small),
            p("Peptide antigens, assay reagents, biomarker support kits", body_small),
            p("Pilot line by month 12-18", body_small),
            p("4/5", body_small),
            p("####-", body_small),
        ],
    ]
    product_table = Table(
        product_rows,
        colWidths=[3.6 * cm, 6.0 * cm, 4.9 * cm, 1.9 * cm, 1.8 * cm],
        repeatRows=1,
    )
    product_style = TableStyle(
        [
            ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#7B7D7D")),
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#117A65")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]
    )
    for r in range(1, len(product_rows)):
        reg_value = int(product_rows[r][3].text.split("/")[0])
        product_style.add("BACKGROUND", (3, r), (3, r), difficulty_color(reg_value))
    product_table.setStyle(product_style)
    story.append(product_table)

    story.append(PageBreak())
    story.append(p("Country Priority Matrix and Projections", h1))
    story.append(
        p(
            "These are strategic planning ranges for 2026-2030, triangulated from WHO/IDF disease trends, "
            "Reuters market/launch signals, and market-growth scenarios.",
            body,
        )
    )

    countries = [
        ("United States", "Largest high-value peptide market", "12-18%", 4, 5, 4.4, "Tier 1"),
        ("China", "Large obesity/diabetes base; strong launch momentum", "18-25%", 4, 4, 4.2, "Tier 1"),
        ("India", "Rapid volume growth from lower base", "25-40% volume-led", 3, 3, 4.2, "Tier 1"),
        ("Germany", "High technical buying power in EU", "10-15%", 4, 4, 3.7, "Tier 2"),
        ("United Kingdom", "Strong R&D and payer infrastructure", "8-14%", 4, 4, 3.6, "Tier 2"),
        ("Japan", "Premium market with aging population", "8-12%", 4, 3, 3.5, "Tier 2"),
        ("Saudi Arabia", "High obesity prevalence; premium private segment", "15-25%", 3, 2, 3.8, "Tier 2"),
        ("UAE", "Fast private-market adoption", "15-22%", 3, 2, 3.7, "Tier 2"),
        ("Brazil", "Large disease burden; price-sensitive", "10-18%", 3, 3, 3.4, "Tier 3"),
    ]

    c_rows = [
        [
            p("<b>Country</b>", body_small),
            p("<b>Demand / Market Signal</b>", body_small),
            p("<b>2026-2030 Growth</b>", body_small),
            p("<b>Reg Complexity</b>", body_small),
            p("<b>Competition</b>", body_small),
            p("<b>Attractiveness</b>", body_small),
            p("<b>Priority</b>", body_small),
        ]
    ]
    for country in countries:
        c_rows.append(
            [
                p(country[0], body_small),
                p(country[1], body_small),
                p(country[2], body_small),
                p(f"{country[3]}/5", body_small),
                p(f"{country[4]}/5", body_small),
                p(f'{country[5]:.1f}/5 {score_bar(country[5])}', body_small),
                p(country[6], body_small),
            ]
        )

    c_table = Table(
        c_rows,
        colWidths=[2.6 * cm, 5.4 * cm, 2.2 * cm, 1.7 * cm, 1.7 * cm, 3.3 * cm, 1.7 * cm],
        repeatRows=1,
    )
    c_style = TableStyle(
        [
            ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#7B7D7D")),
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7D3C98")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]
    )
    for idx, country in enumerate(countries, start=1):
        c_style.add("BACKGROUND", (5, idx), (5, idx), attractiveness_color(country[5]))
        c_style.add("BACKGROUND", (3, idx), (3, idx), difficulty_color(country[3]))
    c_table.setStyle(c_style)
    story.append(c_table)

    story.append(Spacer(1, 10))
    story.append(p("Global Projection Snapshot", h2))

    proj_rows = [
        [p("<b>Theme</b>", body_small), p("<b>Current Signal</b>", body_small), p("<b>Forward Signal</b>", body_small)],
        [
            p("Global obesity-drug spending", body_small),
            p("Approx USD 24B in recent base year", body_small),
            p("Scenario up to approx USD 131B by 2028; up to approx USD 150B in early 2030s", body_small),
        ],
        [
            p("Peptide therapeutics", body_small),
            p("Large, expanding base driven by metabolic disease", body_small),
            p("Mid/high single-digit to low double-digit CAGR range depending on segment scope", body_small),
        ],
        [
            p("Market geography", body_small),
            p("US currently dominates value capture", body_small),
            p("Fast expansion in China, India, and selective GCC private markets", body_small),
        ],
    ]
    proj_table = Table(proj_rows, colWidths=[4.0 * cm, 5.0 * cm, 8.6 * cm], repeatRows=1)
    proj_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#7B7D7D")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1A5276")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(proj_table)

    story.append(Spacer(1, 10))
    story.append(p("Recommended Execution Sequence", h2))
    bullets = [
        "Stage 1 (0-6 months): launch custom peptides + analytical standards and build quality systems.",
        "Stage 2 (6-18 months): add CMC/method-validation service packages and recurring B2B contracts.",
        "Stage 3 (18-36 months): selective GMP-adjacent expansion, diagnostic reagents, and country scaling.",
        "Avoid dependency on shortage-driven compounding arbitrage as a core model.",
    ]
    for item in bullets:
        story.append(p(f"- {item}", body))

    story.append(Spacer(1, 8))
    story.append(p("Key Sources", h2))
    sources = [
        "WHO obesity and overweight fact sheet and 2024 obesity update.",
        "IDF Diabetes Atlas 11th Edition (2025).",
        "KFF GLP-1 public-use polling.",
        "Reuters coverage on GLP-1 forecasts, launch dynamics, and country expansion.",
        "FDA shortage determinations and compounding policy clarifications.",
        "FTC actions on deceptive GLP-1 telehealth advertising.",
    ]
    for src in sources:
        story.append(p(f"- {src}", body_small))

    doc.build(story)
    print(f"Created PDF: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
