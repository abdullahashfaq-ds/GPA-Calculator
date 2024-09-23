from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
)


def get_grade_points(obt_marks):
    grade_scale = [
        (85, 'A', 4.0), (80, 'A-', 3.70), (75, 'B+', 3.30),
        (70, 'B', 3.0), (65, 'B-', 2.70), (61, 'C+', 2.30),
        (58, 'C', 2.0), (55, 'C-', 1.70), (50, 'D', 1.0), (0, 'F', 0.0)
    ]

    for threshold, grade, point in grade_scale:
        if obt_marks >= threshold:
            return grade, point
    return 'F', 0.0


def calculate_gpa(subjects):
    total_grade_points = 0
    total_credit_hours = 0

    for subject in subjects:
        _, grade_point = get_grade_points(subject['obt_marks'])
        total_grade_points += grade_point * subject['crd_hr']
        total_credit_hours += subject['crd_hr']

    return (
        round(
            total_grade_points / total_credit_hours, 2
        ) if total_credit_hours else 0.0,
        total_credit_hours
    )


def create_result_pdf(
    student, institute, degree, semester, subjects, output_path
):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    elements = []

    document_style = ParagraphStyle(
        name='DocumentStyle',
        fontName='Times-Roman',
        fontSize=12,
        alignment=1,
        spaceAfter=6
    )

    heading_style = ParagraphStyle(
        name='HeadingStyle',
        parent=document_style,
        fontSize=20,
        spaceAfter=12
    )

    subheading_style = ParagraphStyle(
        name='SubheadingStyle',
        parent=document_style,
        fontSize=16,
        spaceAfter=6
    )

    semester = semester if 'Semester' in semester else f'Semester {semester}'

    elements.append(Paragraph(f'<b>{institute}</b>', heading_style))
    elements.append(Paragraph(f'<b>{degree}</b>', heading_style))
    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph(f'<b>{student}</b>', subheading_style))
    elements.append(Paragraph(f'<b>{semester}</b>', subheading_style))
    elements.append(Spacer(1, 0.5 * inch))

    gpa, total_credit_hours = calculate_gpa(subjects)
    table_data = [['Subject Name', 'Credit Hours', 'Total Marks', 'Grade']]

    for subject in subjects:
        grade, _ = get_grade_points(subject['obt_marks'])
        table_data.append([
            subject['course'],
            subject['crd_hr'],
            subject['obt_marks'],
            grade
        ])

    table_data.append(['', '', '', ''])
    table_data.append(['Total Crd Hrs', '--', '--', str(total_credit_hours)])
    table_data.append(['Semester GPA', '--', '--', str(gpa)])

    result_table = Table(
        table_data, colWidths=[2.5 * inch, 1.2 * inch, 1.5 * inch, 1.5 * inch]
    )

    table_style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Times-Roman'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    result_table.setStyle(table_style)

    elements.append(result_table)
    elements.append(Spacer(1, 0.5 * inch))

    doc.build(elements)
    return True
