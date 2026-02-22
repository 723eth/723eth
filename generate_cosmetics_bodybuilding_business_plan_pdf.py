#!/usr/bin/env python3
"""
Generate a business plan PDF focused on cosmetics + bodybuilding + looksmaxing.
"""

from datetime import date
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT_PATH = "/workspace/cosmetics-bodybuilding-looksmax-business-plan-2026.pdf"


def p(text, style):
    return Paragraph(text, style)


def risk_bg(level):
    levels = {
        "Low": colors.HexColor("#D5F5E3"),
        "Medium": colors.HexColor("#FCF3CF"),
        "Medium-High": colors.HexColor("#FAD7A0"),
        "High": colors.HexColor("#F5B7B1"),
        "Very High": colors.HexColor("#E6B0AA"),
    }
    return levels.get(level, colors.white)


def make_doc():
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=23,
        textColor=colors.HexColor("#0B3C5D"),
        spaceAfter=6,
    )
    subtitle = ParagraphStyle(
        "Subtitle",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#34495E"),
        spaceAfter=8,
    )
    h1 = ParagraphStyle(
        "H1",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#1F618D"),
        spaceBefore=7,
        spaceAfter=4,
    )
    h2 = ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=13,
        textColor=colors.HexColor("#2874A6"),
        spaceBefore=5,
        spaceAfter=3,
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.3,
        leading=12.5,
        spaceAfter=2.5,
    )
    small = ParagraphStyle(
        "Small",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.2,
        leading=10.8,
        spaceAfter=2,
    )

    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        rightMargin=1.2 * cm,
        leftMargin=1.2 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
        title="Business Plan - Performance Aesthetics Lab",
        author="AI Strategy Draft",
    )

    story = []
    story.append(p("Business Plan (2026-2029)", title))
    story.append(p("Performance Aesthetics Lab", subtitle))
    story.append(p("Cosmetics + Bodybuilding + Looksmaxing", subtitle))
    story.append(p(f"Generated on: {date.today().isoformat()}", small))
    story.append(Spacer(1, 10))

    story.append(p("1. Executive Summary", h1))
    story.append(
        p(
            "Performance Aesthetics Lab is a compliance-first consumer brand at the intersection of cosmetic "
            "performance, body performance, and looks optimization. The plan focuses on legally durable product "
            "categories: topical cosmetics, sports supplements, and protocol-based bundles.",
            body,
        )
    )
    story.append(
        p(
            "<b>Core thesis:</b> Build one trusted routine ecosystem where customers buy repeatedly across skin, "
            "body, and grooming instead of one-off products.",
            body,
        )
    )

    story.append(p("2. Market Opportunity Snapshot", h1))
    market_table_data = [
        [
            p("<b>Segment</b>", small),
            p("<b>Current Scale (approx)</b>", small),
            p("<b>2030 Direction</b>", small),
            p("<b>Growth Signal</b>", small),
        ],
        [p("Beauty & personal care", small), p("USD ~530B-635B", small), p("USD ~590B+", small), p("Stable large TAM", small)],
        [p("Skincare", small), p("USD ~278B", small), p("USD ~361B", small), p("Solid expansion", small)],
        [p("Peptide skincare niche", small), p("USD ~2B-3B", small), p("USD ~4B-6B+", small), p("Faster than core skincare", small)],
        [p("Sports nutrition", small), p("USD ~46B-72B", small), p("USD ~72B-79B", small), p("High demand, broad adoption", small)],
        [p("Bodybuilding supplements", small), p("USD ~27B", small), p("USD ~36B-47B", small), p("Strong category momentum", small)],
        [p("Medical aesthetics (signal market)", small), p("USD ~20B", small), p("USD ~33B", small), p("Premium appearance spend", small)],
    ]
    market_table = Table(market_table_data, colWidths=[4.4 * cm, 4.1 * cm, 4.1 * cm, 5.2 * cm], repeatRows=1)
    market_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#7B7D7D")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#117A65")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(market_table)

    story.append(Spacer(1, 8))
    story.append(p("3. Product Portfolio", h1))
    story.append(p("Line A - Cosmetic Performance (Topicals):", h2))
    for line in [
        "Peptide repair serum",
        "Barrier recovery cream",
        "Brightening day gel",
        "Eye and fine-line complex",
        "Scalp density support serum",
    ]:
        story.append(p(f"- {line}", body))

    story.append(p("Line B - Body Performance (Supplements):", h2))
    for line in [
        "Creatine monohydrate",
        "Protein blend (whey/plant variants)",
        "Pre-workout focus blend",
        "Recovery and sleep formula",
        "Hydration electrolyte stack",
    ]:
        story.append(p(f"- {line}", body))

    story.append(p("Line C - Looksmax Systems (Bundles):", h2))
    for line in [
        "30-day Skin + Strength starter kit",
        "60-day Lean + Sharp program",
        "90-day complete looks optimization protocol",
    ]:
        story.append(p(f"- {line}", body))

    story.append(PageBreak())
    story.append(p("4. Regulatory Difficulty Map", h1))
    reg_data = [
        [
            p("<b>Category</b>", small),
            p("<b>Regulatory Difficulty</b>", small),
            p("<b>Key Compliance Points</b>", small),
            p("<b>Plan Decision</b>", small),
        ],
        [
            p("Topical cosmetics", small),
            p("Medium", small),
            p("MoCRA-style facility/product obligations, adverse event handling, compliant labeling", small),
            p("Core category", small),
        ],
        [
            p("Sports/body supplements", small),
            p("Medium-High", small),
            p("Structure/function claim rules, cGMP, substantiation discipline", small),
            p("Core category", small),
        ],
        [
            p("Clinical aesthetics products", small),
            p("High", small),
            p("Higher evidence/claims burden and jurisdiction complexity", small),
            p("Phase-2 expansion", small),
        ],
        [
            p("Injectable gray-market peptide models", small),
            p("Very High", small),
            p("Major legal exposure and enforcement risk", small),
            p("Excluded", small),
        ],
    ]
    reg_table = Table(reg_data, colWidths=[4.6 * cm, 2.8 * cm, 7.1 * cm, 3.3 * cm], repeatRows=1)
    reg_style = TableStyle(
        [
            ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#7B7D7D")),
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F618D")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]
    )
    reg_table.setStyle(reg_style)
    for i, level in enumerate(["Medium", "Medium-High", "High", "Very High"], start=1):
        reg_table.setStyle(TableStyle([("BACKGROUND", (1, i), (1, i), risk_bg(level))]))
    story.append(reg_table)

    story.append(Spacer(1, 8))
    story.append(p("5. Country Rollout Plan", h1))
    country_data = [
        [p("<b>Tier</b>", small), p("<b>Countries</b>", small), p("<b>Rationale</b>", small)],
        [p("Tier 1", small), p("United States, India", small), p("Best mix of value capture + growth velocity", small)],
        [p("Tier 2", small), p("UAE, Saudi Arabia, UK, Germany", small), p("Premium demand and scalable distribution partnerships", small)],
        [p("Tier 3", small), p("China, Brazil", small), p("Large potential with higher execution complexity", small)],
    ]
    country_table = Table(country_data, colWidths=[2.0 * cm, 6.0 * cm, 9.8 * cm], repeatRows=1)
    country_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#7B7D7D")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7D3C98")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(country_table)

    story.append(Spacer(1, 8))
    story.append(p("6. Go-to-Market Strategy", h1))
    for line in [
        "<b>Channel mix:</b> DTC first, marketplace second, selected gym/clinic/barber retail pilots.",
        "<b>Acquisition:</b> creator affiliate engine + paid social + educational content funnel.",
        "<b>Retention:</b> subscription + protocol onboarding + cross-sell by customer goal profile.",
        "<b>Positioning:</b> science-grade results without regulatory overclaiming.",
    ]:
        story.append(p(f"- {line}", body))

    story.append(PageBreak())
    story.append(p("7. Operating Model", h1))
    story.append(p("Supply and Quality", h2))
    for line in [
        "Contract manufacturing with audited partners.",
        "Dual-source critical ingredients for resilience.",
        "In-house quality documentation, lot tracing, and complaint workflow.",
    ]:
        story.append(p(f"- {line}", body))

    story.append(p("Core Team (Year 1)", h2))
    for line in [
        "General Manager / Founder",
        "Product + Quality Lead",
        "Regulatory and Claims Lead",
        "Growth and Content Lead",
        "Operations and Customer Success",
    ]:
        story.append(p(f"- {line}", body))

    story.append(p("8. Financial Plan (Illustrative)", h1))
    fin_data = [
        [p("<b>Metric</b>", small), p("<b>Year 1</b>", small), p("<b>Year 2</b>", small), p("<b>Year 3</b>", small)],
        [p("Revenue", small), p("USD 1.2M-2.5M", small), p("USD 4M-8M", small), p("USD 10M-20M", small)],
        [p("Gross Margin", small), p("55%-65%", small), p("60%-70%", small), p("62%-72%", small)],
        [p("Repeat Purchase Rate", small), p("25%-40%", small), p("35%-50%", small), p("45%-60%", small)],
        [p("Contribution Margin", small), p("Negative to breakeven", small), p("Positive", small), p("Strong positive", small)],
    ]
    fin_table = Table(fin_data, colWidths=[4.8 * cm, 4.0 * cm, 4.0 * cm, 4.0 * cm], repeatRows=1)
    fin_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#7B7D7D")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0E6655")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(fin_table)

    story.append(Spacer(1, 8))
    story.append(p("9. Milestones (First 12 Months)", h1))
    milestones = [
        "M1-M2: finalize 8-12 launch SKUs and regulatory/claims workflow.",
        "M3: launch DTC and first creator cohort.",
        "M4-M6: launch protocol bundles and subscriptions.",
        "M7-M9: marketplace expansion and first offline pilots.",
        "M10-M12: tier-2 country readiness and scale planning.",
    ]
    for item in milestones:
        story.append(p(f"- {item}", body))

    story.append(p("10. Key Risks and Controls", h1))
    risk_data = [
        [p("<b>Risk</b>", small), p("<b>Impact</b>", small), p("<b>Mitigation</b>", small)],
        [p("Regulatory claim overreach", small), p("High", small), p("Mandatory pre-publication claims review", small)],
        [p("Paid media volatility", small), p("Medium-High", small), p("Diversify with affiliates, SEO, and retention growth", small)],
        [p("Ingredient cost volatility", small), p("Medium", small), p("Dual sourcing and contract purchasing", small)],
        [p("Competitive saturation", small), p("Medium", small), p("Protocol products + trust-led content differentiation", small)],
    ]
    risk_table = Table(risk_data, colWidths=[5.2 * cm, 2.6 * cm, 9.0 * cm], repeatRows=1)
    risk_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#7B7D7D")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#B03A2E")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(risk_table)

    story.append(Spacer(1, 8))
    story.append(p("11. Funding Use (Seed Example: USD 500k-1.5M)", h1))
    for line in [
        "30% inventory and production",
        "25% customer acquisition and creator partnerships",
        "15% product development and testing",
        "15% team and operations",
        "10% compliance/legal/regulatory",
        "5% contingency",
    ]:
        story.append(p(f"- {line}", body))

    story.append(Spacer(1, 8))
    story.append(p("Final Strategy Statement", h1))
    story.append(
        p(
            "Build a cross-category <b>Performance Aesthetics Lab</b> that captures both beauty and bodybuilding "
            "demand while maintaining strict compliance discipline. This model offers high growth potential with "
            "lower legal downside than gray-market peptide approaches.",
            body,
        )
    )

    story.append(Spacer(1, 8))
    story.append(p("Source basis: WHO, IDF, Reuters, KFF, FDA/FTC references and segment-level market reports.", small))

    doc.build(story)


if __name__ == "__main__":
    make_doc()
    print(f"Created PDF: {OUTPUT_PATH}")
