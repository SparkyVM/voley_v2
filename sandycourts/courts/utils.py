'''
menu = [{'title': "О нас", 'url_name': 'about'},
        {'title': "Новости", 'url_name': 'news'},
        {'title': "Тренеры", 'url_name': 'trains'},
        {'title': "Турниры", 'url_name': 'tournaments'},
        {'title': "Аренда", 'url_name': 'courts'},
        #{'title': "Статистика", 'url_name': 'stat'},
        {'title': "Контакты", 'url_name': 'contacts'},
        ]  
'''

class LocationMixin:
    """Класс миксин для Местоположения"""
    paginate_by = 5         # Проверить НЕ ИСПОЛЬЗУЕТСЯ почти точно
    title_page = None
    loc_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.loc_selected is not None:
            self.extra_context['loc_selected'] = self.loc_selected

    def get_mixin_context(self, context, **kwargs):
        #context['menu'] = menu
        context['loc_selected'] = None
        context.update(kwargs)
        return context