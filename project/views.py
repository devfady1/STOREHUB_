from django.shortcuts import render


def handler404(request, exception):
    return render(request, '400.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
