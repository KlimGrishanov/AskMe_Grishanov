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

def paginate(objects, request, per_page=PER_PAGE):
    page = int(request.GET.get('page', 1))
    paginator = Paginator(objects, per_page)
    if page > len(objects) / per_page or page < 1:
        return paginator.page(1), 1
    return paginator.page(page), page

# Create your views here.
def index(request):
    currentPage, pageNum = paginate(QUESTIONS, request)
    return render(request, 'index.html', {'questions': currentPage, 'tags': TAGS, 'members': MEMBERS, 'curPage': pageNum, 'prevPage': pageNum-1, 'nextPage': pageNum+1, 'symbolRoute': "?"})


def hot(request):
    currentPage, pageNum = paginate(QUESTIONS, request)
    return render(request, 'hot.html', {'questions': currentPage, 'tags': TAGS, 'members': MEMBERS, 'curPage': pageNum, 'prevPage': pageNum-1, 'nextPage': pageNum+1, 'route': "hot", 'symbolRoute': "?"})


def tag(request):
    tag = request.GET.get('tag', 0)
    questions = []
    for i in range(0, len(QUESTIONS)):
        if QUESTIONS[i].get('tag') == TAGS[int(tag)].get('name'):
            questions.append(QUESTIONS[i])
    currentPage, pageNum = paginate(questions, request)
    return render(request, 'tag.html', {'questions': currentPage, 'tags': TAGS, 'members': MEMBERS, 'curTag': TAGS[int(tag)].get('name'), 'curPage': pageNum, 'prevPage': pageNum-1, 'nextPage': pageNum+1, 'route':  "tags/?tag=" + str(tag), 'symbolRoute': "&"})


def settings(request):
    return render(request, 'settings.html')


def question(request, question_id):
    question = QUESTIONS[question_id]
    answers = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long lorem ipsum {i}'
        } for i in range(100)
    ]
    currentPage, pageNum = paginate(answers, request)
    return render(request, 'question.html', {'question': question, 'answers': currentPage, 'tags': TAGS, 'members': MEMBERS, 'curPage': pageNum, 'prevPage': pageNum-1, 'nextPage': pageNum+1, 'route': "question/" + str(question_id), 'symbolRoute': "?"})


def login(request):
    return render(request, 'login.html', {'tags': TAGS, 'members': MEMBERS})


def signup(request):
    return render(request, 'signup.html', {'tags': TAGS, 'members': MEMBERS})


def ask(request):
    return render(request, 'ask.html', {'tags': TAGS, 'members': MEMBERS})

def logout(request):
    return render(request, 'login.html', {'tags': TAGS, 'members': MEMBERS})
