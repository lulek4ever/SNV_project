from django.shortcuts import render


def index_view(request):
    content_list = {'links_menu': [{'href': 'philosophy', 'name': 'Фислософия'},
                                   {'href': 'economics', 'name': 'Экономика'},
                                   {'href': 'anthropology', 'name': 'Антропология'},
                                   {'href': 'history', 'name': 'История'},
                                   {'href': 'student_books', 'name': 'Учебные пособия'},
                                   {'href': 'detectives', 'name': 'Детективы'}]
                    }
    return render(request, 'mainapp/index.html', {'content': content_list})


def contacts_view(request):
    content_list = {'links_menu': [{'href': 'philosophy', 'name': 'Фислософия'},
                                   {'href': 'economics', 'name': 'Экономика'},
                                   {'href': 'anthropology', 'name': 'Антропология'},
                                   {'href': 'history', 'name': 'История'},
                                   {'href': 'student_books', 'name': 'Учебные пособия'},
                                   {'href': 'detectives', 'name': 'Детективы'}]
                    }

    return render(request, 'mainapp/contacts.html', {'content': content_list})
