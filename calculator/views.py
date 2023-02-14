from django.shortcuts import render, reverse
from django.http import HttpResponse
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    template_name = 'calculator/home.html'

    pages = {
        'Omlet': reverse(omlet),
        'Pasta': reverse(pasta),
        'Buter': reverse(buter)
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def omlet(request):
    serving = int(request.GET.get('serving',1))
    #context = {'recipe': DATA['omlet']}
    context = {'recipe': {k: round((v * serving),2) for k, v in DATA['omlet'].items()}}
    return render(request, 'calculator/index.html', context)

def pasta(request):
    serving = int(request.GET.get('serving',1))
    #context = {'recipe': DATA['omlet']}
    context = {'recipe': {k: round((v * serving),2) for k, v in DATA['pasta'].items()}}
    return render(request, 'calculator/index.html', context)

def buter(request):
    serving = int(request.GET.get('serving', 1))
    # context = {'recipe': DATA['omlet']}
    context = {'recipe': {k: round((v * serving),2) for k, v in DATA['buter'].items()}}
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
