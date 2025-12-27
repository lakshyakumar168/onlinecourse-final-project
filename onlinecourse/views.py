from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment, Question, Choice, Submission


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment = Enrollment.objects.filter(course=course).first()

    submission = Submission.objects.create(enrollment=enrollment)

    selected_choices = request.POST.getlist('choice')
    for choice_id in selected_choices:
        choice = Choice.objects.get(pk=choice_id)
        submission.choices.add(choice)

    return redirect(
        'show_exam_result',
        course_id=course.id,
        submission_id=submission.id
    )


def show_exam_result(request, course_id, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)

    total_score = 0
    possible_score = 0

    for choice in submission.choices.all():
        possible_score += 1
        if choice.is_correct:
            total_score += 1

    context = {
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score,
    }

    return render(request, 'onlinecourse/exam_result.html', context)
