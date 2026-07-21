import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.graphics.shapes import Drawing, Line

def build_pdf(filename=r"c:\Users\AIO-ELIB-02\portfolio-site\resume.pdf"):
    # Target page layout
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Palette - Classic Corporate
    PRIMARY_COLOR = colors.HexColor("#000000")
    TEXT_COLOR = colors.HexColor("#333333")
    ACCENT_COLOR = colors.HexColor("#666666")
    
    # Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=PRIMARY_COLOR,
        alignment=1 # Centered
    )
    
    contact_style = ParagraphStyle(
        'DocContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=ACCENT_COLOR,
        alignment=1 # Centered
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=PRIMARY_COLOR,
        spaceBefore=8,
        spaceAfter=3
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=12.5,
        textColor=TEXT_COLOR
    )
    
    bullet_style = ParagraphStyle(
        'BulletText',
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2
    )
    
    header_left = ParagraphStyle(
        'HeaderLeft',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=TEXT_COLOR
    )
    
    header_right = ParagraphStyle(
        'HeaderRight',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=ACCENT_COLOR,
        alignment=2 # Right aligned
    )

    story = []
    
    # --- HEADER / CONTACT INFO ---
    story.append(Paragraph("DIVYANSHU YADAV", title_style))
    story.append(Spacer(1, 4))
    
    contact_text = (
        "Jaipur, India  |  +91 9351532707  |  "
        "<a href='mailto:yadavdavid382@gmail.com'><font color='#000000'>yadavdavid382@gmail.com</font></a>  |  "
        "<a href='https://in.linkedin.com/in/divyanshu-yadav-dk1'><font color='#000000'>LinkedIn</font></a>  |  "
        "<a href='https://github.com/david1-max'><font color='#000000'>GitHub</font></a>  |  "
        "<a href='https://david1-max.github.io'><font color='#000000'>Portfolio</font></a>"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 8))
    
    def add_section_divider(title):
        story.append(Paragraph(title.upper(), section_heading))
        # Draw a horizontal line
        d = Drawing(doc.width, 3)
        d.add(Line(0, 1, doc.width, 1, strokeColor=PRIMARY_COLOR, strokeWidth=1))
        story.append(d)
        story.append(Spacer(1, 4))
        
    # --- SUMMARY ---
    add_section_divider("Professional Summary")
    summary_text = (
        "Results-driven Computer Science and Artificial Intelligence student at JK Lakshmipat University "
        "with a strong foundation in full-stack web development, machine learning, and core programming. "
        "Experienced in building production-ready portals and appraisal platforms during university internships. "
        "Demonstrates leadership and communication skills developed through teaching assistantships in C and Python. "
        "Eager to leverage strong technical capabilities to drive impact as a Full-Stack Developer or Machine Learning intern."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 6))
    
    # --- EDUCATION ---
    add_section_divider("Education")
    edu_table_data = [
        [
            Paragraph("<b>JK Lakshmipat University</b>", header_left),
            Paragraph("Jaipur, India", header_right)
        ],
        [
            Paragraph("<i>Bachelor of Technology in Computer Science & Engineering (Specialization: AI)</i>", body_style),
            Paragraph("Expected 2028", header_right)
        ],
        [
            Paragraph("Academic Standing: Honors List", body_style),
            Paragraph("", header_right)
        ]
    ]
    t = Table(edu_table_data, colWidths=[doc.width*0.75, doc.width*0.25])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t)
    story.append(Spacer(1, 6))
    
    # --- SKILLS ---
    add_section_divider("Core Technical Skills")
    skills_text = (
        "<b>Programming Languages:</b> Python, JavaScript (ES6+), C, C++, SQL (SQLite, MySQL)<br/>"
        "<b>Web Development & Frameworks:</b> React, Node.js, Express, Flask (Python), HTML5, CSS3<br/>"
        "<b>Machine Learning & Data Science:</b> Pandas, NumPy, Scikit-learn, TensorFlow/PyTorch, Computer Vision (OpenCV), NLP<br/>"
        "<b>Web Technologies & Protocols:</b> WebSockets, WebRTC, REST APIs, JSON<br/>"
        "<b>Developer Tools & Databases:</b> Git/GitHub, SQLite, MySQL, VS Code, Docker, Git"
    )
    story.append(Paragraph(skills_text, body_style))
    story.append(Spacer(1, 6))
    
    # --- EXPERIENCE ---
    add_section_divider("Professional Experience & Internships")
    
    # Summer Intern
    exp1_header = [
        [
            Paragraph("<b>JK Lakshmipat University</b> — <i>Full-Stack Summer Intern</i>", header_left),
            Paragraph("May 2026 – July 2026", header_right)
        ]
    ]
    t_exp1 = Table(exp1_header, colWidths=[doc.width*0.75, doc.width*0.25])
    t_exp1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_exp1)
    
    story.append(Paragraph("&bull; Solely architected and developed <b>Samiksha</b>, a student-centered feedback mechanism and appraisal portal to aid teaching processes.", bullet_style))
    story.append(Paragraph("&bull; Designed intuitive dashboards for student input and administrative reporting, improving system transparency.", bullet_style))
    story.append(Paragraph("&bull; Optimized backend database queries, reducing data retrieval and feedback-processing time by 30%.", bullet_style))
    story.append(Spacer(1, 4))
    
    # TA
    exp2_header = [
        [
            Paragraph("<b>JK Lakshmipat University</b> — <i>Teaching Assistant (Python & C)</i>", header_left),
            Paragraph("Aug 2025 – Present", header_right)
        ]
    ]
    t_exp2 = Table(exp2_header, colWidths=[doc.width*0.75, doc.width*0.25])
    t_exp2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_exp2)
    story.append(Paragraph("&bull; Instructed lab sessions and debugged foundational code for a batch of 60+ undergraduate students.", bullet_style))
    story.append(Paragraph("&bull; Evaluated student assignments and designed comprehensive programming exercises under the professor's guidance.", bullet_style))
    
    story.append(Spacer(1, 6))
    
    # --- PROJECTS ---
    add_section_divider("Projects")
    
    # BubbleID
    p1_header = [
        [
            Paragraph("<b>BubbleID-Reproduction</b> — <i>Deep Learning & Computer Vision</i>", header_left),
            Paragraph("<a href='https://github.com/david1-max/BubbleID-Reproduction'><font color='#000000'>GitHub Link</font></a>", header_right)
        ]
    ]
    t_p1 = Table(p1_header, colWidths=[doc.width*0.75, doc.width*0.25])
    t_p1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_p1)
    story.append(Paragraph("&bull; Replicated and benchmarked the state-of-the-art BubbleID deep learning framework designed to study pool boiling heat transfer processes.", bullet_style))
    story.append(Paragraph("&bull; Built a high-performance image processing pipeline utilizing Mask R-CNN for pixel-level semantic segmentation of vapor bubbles.", bullet_style))
    story.append(Paragraph("&bull; Integrated OC-SORT (Observation-Centric SORT) to track bubble trajectories, nucleation, and departure events across high-speed video frames.", bullet_style))
    story.append(Spacer(1, 4))
    
    # vibe-chat
    p2_header = [
        [
            Paragraph("<b>vibe-chat</b> — <i>Real-time Messaging & Video Calling Platform</i>", header_left),
            Paragraph("<a href='https://github.com/david1-max/vibe-chat'><font color='#000000'>GitHub Link</font></a>", header_right)
        ]
    ]
    t_p2 = Table(p2_header, colWidths=[doc.width*0.75, doc.width*0.25])
    t_p2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_p2)
    story.append(Paragraph("&bull; Engineered a responsive, full-featured web communication platform allowing users to interact via real-time messaging and peer video rooms.", bullet_style))
    story.append(Paragraph("&bull; Designed a bi-directional event-driven signaling channel using Socket.io to enable instant text messaging and room synchronizations.", bullet_style))
    story.append(Paragraph("&bull; Implemented low-latency audio/video calling using WebRTC peer-to-peer protocols and STUN/TURN servers to establish secure connections.", bullet_style))
    story.append(Spacer(1, 4))
    
    # LeetCode Solutions
    p_lc_header = [
        [
            Paragraph("<b>LeetCode Solutions</b> — <i>Data Structures & Algorithms</i>", header_left),
            Paragraph("<a href='https://github.com/david1-max/leetcode-solutions'><font color='#000000'>GitHub Link</font></a>", header_right)
        ]
    ]
    t_plc = Table(p_lc_header, colWidths=[doc.width*0.75, doc.width*0.25])
    t_plc.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_plc)
    story.append(Paragraph("&bull; Created a personal repository for daily problem-solving to master advanced algorithm designs and computational efficiency.", bullet_style))
    story.append(Paragraph("&bull; Solved multiple complexity levels using optimal time/space methods (e.g. Binary Search, Two-pointers, HashMaps).", bullet_style))
    story.append(Paragraph("&bull; Documented complexity analysis (Big-O notation) and mathematical optimizations for every solution.", bullet_style))
    story.append(Spacer(1, 4))
    
    # Appraisal System
    p3_header = [
        [
            Paragraph("<b>JKLU Appraisal System</b> — <i>Full-Stack Performance Portal</i>", header_left),
            Paragraph("Private Repository", header_right)
        ]
    ]
    t_p3 = Table(p3_header, colWidths=[doc.width*0.75, doc.width*0.25])
    t_p3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_p3)
    story.append(Paragraph("&bull; Developed key modules of an enterprise performance appraisal system designed to digitize academic and administrative evaluations.", bullet_style))
    story.append(Paragraph("&bull; Designed relational database models using Flask-SQLAlchemy to capture publications, patents, and teaching feedback.", bullet_style))
    story.append(Paragraph("&bull; Programmed the appraisal scoring engine to compute points based on publication indexes and author order; built custom PDF/Excel exporters.", bullet_style))
    
    story.append(Spacer(1, 6))

    # --- CERTIFICATIONS ---
    add_section_divider("Certifications")

    certs = [
        {
            "name": "Problem Solving (Basic) Skill Certification",
            "issuer": "HackerRank",
            "date": "Jul 2026",
            "url": "https://www.hackerrank.com/certificates/c4a79f66666b",
            "cid": "c4a79f66666b"
        },
        {
            "name": "SQL (Basic) Skill Certification",
            "issuer": "HackerRank",
            "date": "Jul 2026",
            "url": "https://www.hackerrank.com/certificates/bbf6076ae8f9",
            "cid": "bbf6076ae8f9"
        },
        {
            "name": "Python (Basic) Skill Certification",
            "issuer": "HackerRank",
            "date": "Jul 2026",
            "url": "https://www.hackerrank.com/certificates/7fdc5f0187af",
            "cid": "7fdc5f0187af"
        },
        {
            "name": "Programming with C++",
            "issuer": "Simplilearn (Coursera)",
            "date": "Jun 2025",
            "url": "https://coursera.org/verify/XEBPREKSD9H2",
            "cid": "XEBPREKSD9H2"
        },
        {
            "name": "Python Data Structures",
            "issuer": "University of Michigan (Coursera)",
            "date": "Dec 2024",
            "url": "https://coursera.org/verify/1VDHAXLCXG9R",
            "cid": "1VDHAXLCXG9R"
        },
        {
            "name": "Programming for Everybody (Getting Started with Python)",
            "issuer": "University of Michigan (Coursera)",
            "date": "Dec 2024",
            "url": "https://coursera.org/verify/02EE3KE7V869",
            "cid": "02EE3KE7V869"
        },
    ]

    for cert in certs:
        cert_row = [[
            Paragraph(f"<b>{cert['name']}</b> — <i>{cert['issuer']}</i>", header_left),
            Paragraph(cert['date'], header_right)
        ]]
        t_cert = Table(cert_row, colWidths=[doc.width * 0.75, doc.width * 0.25])
        t_cert.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ]))
        story.append(t_cert)
        story.append(Paragraph(
            f"&bull; Credential ID: <a href='{cert['url']}'><font color='#000000'>{cert['cid']}</font></a>",
            bullet_style
        ))
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 4))

    # --- ACTIVITIES ---
    add_section_divider("Awards & Activities")
    story.append(Paragraph("&bull; <b>Academic Honors:</b> Consistently recognized on the Dean's List / Honors List for outstanding academic performance.", bullet_style))
    story.append(Paragraph("&bull; <b>Extracurriculars:</b> Active squad player for the JKLU Cricket Team, competing in inter-university tournaments.", bullet_style))
    
    doc.build(story)
    print("PDF Generation complete.")

if __name__ == "__main__":
    build_pdf()
