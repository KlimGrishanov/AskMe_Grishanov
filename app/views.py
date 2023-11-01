from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse


QUESTIONS = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long lorem ipsum {i}'
        } for i in range(100)
    ]

PER_PAGE = 10

def paginate(objects, page, per_page=PER_PAGE):
    paginator = Paginator(objects, per_page)
    return paginator.page(page)

# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except Exception:
        return render(request, '404.html')

    if page < 1 or page > len(QUESTIONS) / PER_PAGE:
        return render(request, 'index.html')

    return render(request, 'index.html', {'questions': paginate(QUESTIONS, page)})


def hot(request):
    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except Exception:
        return render(request, '404.html')

    if page < 1 or page > len(QUESTIONS) / PER_PAGE:
        return render(request, 'hot.html')

    return render(request, 'hot.html', {'questions': paginate(QUESTIONS, page)})


def tag(request):
    page = 1
    # page = request.GET.get('page', 1)
    # try:
    #     page = int(page)
    # except Exception:
    #     return render(request, '404.html')
    #
    # if page < 1 or page > len(QUESTIONS) / PER_PAGE:
    #     return render(request, 'tag.html')

    return render(request, 'tag.html', {'questions': paginate(QUESTIONS, page)})


def settings(request):
    return render(request, 'settings.html')


def question(request, question_id):
    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except Exception:
        return render(request, '404.html')

    if page < 1 or page > len(QUESTIONS) / PER_PAGE:
        return render(request, 'index.html')

    question = QUESTIONS[question_id]
    answers = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long lorem ipsum {i}'
        } for i in range(100)
    ]
    return render(request, 'question.html', {'question': question, 'answers': paginate(answers, page)})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def ask(request):
    return render(request, 'ask.html')

def logout(request):
    return render(request, 'login.html')
