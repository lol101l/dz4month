from django.http import HttpResponse

def blog(request):
    if request.method == 'GET':
        return HttpResponse('Пост о книге: «1984» Джорджа Оруэлла — классика антиутопии.')