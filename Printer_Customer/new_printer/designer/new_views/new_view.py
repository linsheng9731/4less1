from django.http import HttpResponse

def test(request):
    return HttpResponse('new view test okay')
