import os
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def generate_company_profile_pdf(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40
    )

    styles = getSampleStyleSheet()

    # Custom Brand Colors
    c_navy = colors.HexColor('#0A192F')
    c_amber = colors.HexColor('#D97706')
    c_charcoal = colors.HexColor('#1E293B')
    c_grey = colors.HexColor('#64748B')
    c_light = colors.HexColor('#F8FAFC')

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=c_navy,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=c_amber,
        spaceAfter=15
    )

    h2_style = ParagraphStyle(
        'Heading2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=c_navy,
        spaceBefore=12,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=c_charcoal,
        spaceAfter=8
    )

    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=c_charcoal,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    disclaimer_style = ParagraphStyle(
        'Disclaimer',
        parent=styles['Italic'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11,
        textColor=c_grey,
        spaceAfter=10
    )

    story = []

    # Header Banner / Title
    story.append(Paragraph("PRIMECORE ENGINEERING & INDUSTRIAL SERVICES", title_style))
    story.append(Paragraph("TECHNICAL CAPABILITY & COMPANY PROFILE — DEMO DOCUMENT", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=c_amber, spaceBefore=0, spaceAfter=15))

    # Disclaimer Box
    disclaimer_text = "<b>DEMO PORTFOLIO NOTICE:</b> PrimeCore Engineering & Industrial Services is a fictional demo entity created specifically for AfixTech's agency development portfolio. All operational metrics, project case studies, and corporate details within this profile represent illustrative capability samples."
    story.append(Paragraph(disclaimer_text, disclaimer_style))
    story.append(Spacer(1, 8))

    # Company Overview
    story.append(Paragraph("1. EXECUTIVE SUMMARY & POSITIONING", h2_style))
    overview_p = ("PrimeCore provides specialized engineering, industrial maintenance, technical procurement, "
                  "installation, and project support for organizations operating across infrastructure and industrial environments. "
                  "Our core focus is delivering practical, high-precision technical solutions that maximize uptime, ensure operational safety, "
                  "and safeguard capital investment in critical mechanical and electrical assets.")
    story.append(Paragraph(overview_p, body_style))

    # Core Services
    story.append(Paragraph("2. CORE CAPABILITIES & SERVICES", h2_style))
    services_data = [
        ["Service Discipline", "Core Focus Area", "Primary Deliverables"],
        ["01. Engineering Services", "Structural, Mechanical & Piping FEED", "3D CAD/BIM, Integrity Audits, HAZOP Studies"],
        ["02. Industrial Maintenance", "Predictive & Overhaul Maintenance", "Vibration Analysis, CMMS Setup, Shutdown Management"],
        ["03. Technical Procurement", "Global OEM Sourcing & Quality Control", "API/ISO Certified Valves, Pumps & Equipment Sourcing"],
        ["04. Installation & Commissioning", "Heavy Rigging & Electrical Integration", "Laser Alignment, Hydro-testing, SAT Execution"],
        ["05. Project Support", "On-site Supervision & HSE Monitoring", "QA/QC Auditing, Milestone Progress Verification"]
    ]

    t_services = Table(services_data, colWidths=[2.2*inch, 2.5*inch, 2.5*inch])
    t_services.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_navy),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8.5),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BACKGROUND', (0,1), (-1,-1), c_light),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,1), (-1,-1), 5),
        ('BOTTOMPADDING', (0,1), (-1,-1), 5),
    ]))
    story.append(t_services)
    story.append(Spacer(1, 10))

    # Our 6-Step Project Approach
    story.append(Paragraph("3. SYSTEMATIC PROJECT EXECUTION METHODOLOGY", h2_style))
    approach_p = ("PrimeCore operates under a rigorous six-stage delivery model designed to eliminate project risk "
                  "and enforce high safety and technical quality standards:")
    story.append(Paragraph(approach_p, body_style))

    steps = [
        "<b>01 — Understand:</b> Rapid site assessment, client requirement mapping, and risk analysis.",
        "<b>02 — Plan:</b> Front-End Engineering Design (FEED), resource allocation, and timeline scheduling.",
        "<b>03 — Execute:</b> Supervised technical installation, overhaul, or procurement execution.",
        "<b>04 — Test:</b> Non-destructive testing (NDT), loop testing, and hydrostatic pressure testing.",
        "<b>05 — Handover:</b> Site Acceptance Testing (SAT), client sign-off, and as-built documentation delivery.",
        "<b>06 — Support:</b> Post-installation warranty support, preventive maintenance, and spare parts management."
    ]
    for step in steps:
        story.append(Paragraph(f"• {step}", bullet_style))

    story.append(Spacer(1, 10))

    # Contact & Information Box
    story.append(Paragraph("4. CONTACT & DEMO ENQUIRIES", h2_style))
    contact_info = [
        ["Primary Address:", "Industrial Zone, Ikeja, Lagos State, Nigeria (Demo Location)"],
        ["General Inquiries:", "contact@primecore-demo.com"],
        ["Telephone / Direct:", "+234 (0) 1 234 5678 / +234 (0) 800 PRIMECORE"],
        ["AfixTech Portfolio Web:", "https://afixtech.vercel.app/"]
    ]
    t_contact = Table(contact_info, colWidths=[2.0*inch, 5.2*inch])
    t_contact.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('TEXTCOLOR', (0,0), (-1,-1), c_charcoal),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
    ]))
    story.append(t_contact)

    doc.build(story)

if __name__ == '__main__':
    target = Path(__file__).resolve().parent / 'app' / 'static' / 'documents' / 'primecore-company-profile.pdf'
    generate_company_profile_pdf(str(target))
    print(f"Company profile PDF generated successfully at: {target}")
