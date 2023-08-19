from django.shortcuts import render, get_object_or_404


def main_page(request):
    return render(request, 'main_page/index.html', {})
