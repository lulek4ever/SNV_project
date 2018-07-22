from django.shortcuts import render

def product_view(request):
    content_list = {'name': 'Caliban and the Witch', 'author': 'Silvia Federici', 'price': '1190', 'page_amount': 300,
                    'publisher': 'ABC', 'description': 'описание здесь', 'image_url': '../static/content/caliban.jpg',

                    'similar_book': [{'name': 'Второй пол', 'author': 'Симона де Бовуар',
                                      'price': 890, 'image_url': '../static/content/second-sex.jpg'},

                                    {'name': 'Caliban and the Witch', 'author': 'Silvia Federici',
                                     'price': 1190, 'image_url': '../static/content/caliban.jpg'},

                                    {'name': 'Записки у изголовья', 'author': 'Сэй Сенагон',
                                     'price': 450, 'image_url': '../static/content/Zapiski_u_izgolovya.jpg'},

                                    {'name': 'Под стеклянным колпаком', 'author': 'Сильвия Плат',
                                     'price': 400, 'image_url': '../static/content/glass-dome.jpg'}],

                    'links_menu': [{'href': 'philosophy', 'name': 'Фислософия'},
                                   {'href': 'economics', 'name': 'Экономика'},
                                   {'href': 'anthropology', 'name': 'Антропология'},
                                   {'href': 'history', 'name': 'История'},
                                   {'href': 'student_books', 'name': 'Учебные пособия'},
                                   {'href': 'detectives', 'name': 'Детективы'}]
                    }

    return render(request, 'book/product.html', {'content': content_list})
