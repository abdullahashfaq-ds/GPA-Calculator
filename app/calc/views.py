import os
from django.shortcuts import render
from django.http import FileResponse, JsonResponse
from .utils import calculate_gpa, create_result_pdf


def home(request):
    if request.method == 'POST':
        context = {
            key: request.POST.get(key) for key in [
                'name', 'university', 'degree', 'semester'
            ]
        }
        return render(request, 'calculator.html', context)
    return render(request, 'home.html')


def policy(request):
    return render(request, 'policy.html')


def calculator(request):
    if request.method == 'POST':
        credit_hours = request.POST.getlist('credit_hours')
        course_titles = request.POST.getlist('course_title')
        obtained_marks = request.POST.getlist('obtained_marks')

        subjects = []

        for i in range(len(course_titles)):
            subjects.append({
                'course': course_titles[i],
                'obt_marks': float(obtained_marks[i]),
                'crd_hr': float(credit_hours[i]),
            })

        gpa, total_crd_hrs = calculate_gpa(subjects)

        student_name = f"{request.POST.get('name')}".replace(' ', '_')
        pdf_path = f'static/pdfs/{student_name}.pdf'

        pdf = create_result_pdf(
            student=request.POST.get('name'),
            institute=request.POST.get('university'),
            degree=request.POST.get('degree'),
            semester=request.POST.get('semester'),
            subjects=subjects,
            output_path=pdf_path
        )

        context = {
            'calculated_gpa': gpa,
            'total_crd_hrs': total_crd_hrs,
            'pdf_path': pdf_path,
            'pdf_result': pdf
        }

        return render(request, 'result.html', context)
    return render(request, 'calculator.html')


def download_pdf(request, pdf_path):
    if os.path.exists(pdf_path):
        return FileResponse(
            open(pdf_path, 'rb'), as_attachment=True,
            filename=os.path.basename(pdf_path)
        )
    else:
        return JsonResponse({'error': 'PDF not found.'}, status=404)
