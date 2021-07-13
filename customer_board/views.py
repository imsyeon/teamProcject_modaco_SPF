from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm

def board(request):
    '''
    고객 게시판 목록 출력
    '''
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    return render(request, 'customer_board/question_list.html', context)

def detail(request, question_id):
    '''
    게시판 내용 출력
    '''

    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'customer_board/question_detail.html', context)

def answer_create(request, question_id):
    """
     게시판 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('customer_board:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'customer_board/question_detail.html', context)

def question_create(request):
    """
    게시판 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('customer_board:board')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'customer_board/question_form.html', context)