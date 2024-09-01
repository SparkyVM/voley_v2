menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]


class LocationMixin:
    paginate_by = 5
    title_page = None
    loc_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.loc_selected is not None:
            self.extra_context['loc_selected'] = self.loc_selected

    def get_mixin_context(self, context, **kwargs):
        context['loc_selected'] = None
        context.update(kwargs)
        return context

class StatusMixin:
    paginate_by = 5
    title_page = None
    status_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.status_selected is not None:
            self.extra_context['status_selected'] = self.status_selected

    def get_mixin_context(self, context, **kwargs):
        context['status_selected'] = None
        context.update(kwargs)
        return context