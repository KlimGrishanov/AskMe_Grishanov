from django.core.paginator import Paginator
from django.shortcuts import render

TAGS = [{
    'id': 0,
    'name': 'Python'
}, {
    'id': 1,
    'name': 'Perl'
}, {
    'id': 2,
    'name': 'Ruby'
}]

MEMBERS = [
    {
        'id': 0,
        'name': 'Mr Horse'
    }, {
        'id': 1,
        'name': 'Mrs Horse'
    }, {
        'id': 2,
        'name': 'Mr Sheep'
    }
]

QUESTIONS = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long lorem ipsum {i}',
            'tag': TAGS[i % 3].get('name'),
            'tagId': i % 3
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

    return render(request, 'index.html', {'questions': paginate(QUESTIONS, page), 'tags': TAGS, 'members': MEMBERS})


def hot(request):
    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except Exception:
        return render(request, '404.html')

    if page < 1 or page > len(QUESTIONS) / PER_PAGE:
        return render(request, 'hot.html')

    return render(request, 'hot.html', {'questions': paginate(QUESTIONS, page), 'tags': TAGS, 'members': MEMBERS})


def tag(request):
    page = request.GET.get('page', 1)
    tag = request.GET.get('tag', 0)
    questions = []
    for i in range(0, len(QUESTIONS)):
        if QUESTIONS[i].get('tag') == TAGS[int(tag)].get('name'):
            questions.append(QUESTIONS[i])
    # page = request.GET.get('page', 1)
    # try:
    #     page = int(page)
    # except Exception:
    #     return render(request, '404.html')
    #
    # if page < 1 or page > len(QUESTIONS) / PER_PAGE:
    #     return render(request, 'tag.html')

    return render(request, 'tag.html', {'questions': paginate(questions, page), 'tags': TAGS, 'members': MEMBERS, 'curTag': TAGS[int(tag)].get('name')})


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
    return render(request, 'question.html', {'question': question, 'answers': paginate(answers, page), 'tags': TAGS, 'members': MEMBERS})


def login(request):
    return render(request, 'login.html', {'tags': TAGS, 'members': MEMBERS})


def signup(request):
    return render(request, 'signup.html', {'tags': TAGS, 'members': MEMBERS})


def ask(request):
    return render(request, 'ask.html', {'tags': TAGS, 'members': MEMBERS})

def logout(request):
    return render(request, 'login.html', {'tags': TAGS, 'members': MEMBERS})
