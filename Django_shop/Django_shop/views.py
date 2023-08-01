from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render


def change_table(request):
    return render(request,'table_change.html')


def fill_name_brand(request):
    return HttpResponse, "he"


def main_page(request):
    if request.method == "GET":
        # Обробка логіки та отримання результату
        change_table(request)


    return render(request, 'main_page.html')

