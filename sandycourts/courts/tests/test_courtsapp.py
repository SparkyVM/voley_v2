from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from ..forms import AddNewsForm
from ..models import News
#from django.test import Client


class CourtTestCase(TestCase):
    def test_status_code(self):
        '''
        Получение кода 200 при переходе на существующий url
        '''

        url = reverse('courts')
        response = self.client.get(url).status_code
        self.assertEqual(HttpResponse.status_code, response)

    def test_used_template(self):
        '''
        Проверка, что при рендере страницы использовался указанный шаблон
        '''

        url = reverse('contacts')
        response = self.client.get(url)
        template_name = 'courts/locations.html'
        self.assertTemplateUsed(response, template_name)

    def test_redirect(self):
        '''
        Проверка переадресации. Для добавления новости требуется авторизация.
        '''
        
        url = reverse('news_add')
        response = self.client.get(url)
        expected_url = '/users/login/?next=/news_add/'
        self.assertRedirects(response, expected_url, status_code=302, target_status_code=200)
  
    def test_title(self):
        '''
        Проверка полученного контекста
        '''
        url = reverse('contacts')
        response = self.client.get(url)
        expected_context = 'Локации'
        self.assertEqual(response.context['title'], expected_context)

"""

    def test_form(self):
        '''
        пока не работает
        '''
        test_news = News()
        test_news.title = 'jsdgsadfgnasdg;kanjd;knjgkajsndfgknjaksfbnkabfkjbgakbvkabjkfvdjjanbdfkvnjakfjnvkjnafdkvnjakfjnvkajfnvknjafkvnjakdfnvkandfvknafkjvnkfjnvkdfgdfnjafknvakjnfv'
        expected_exception = ValidationError
        expected_message = "Длина превышает 150 символов"
        check_title = 'jsdgsadfgnasdg;kanjd;knjgkajsndfgknjaksfbnkabfkjbgakbvkabjkfvdjjanbdfkvnjakfjnvkjnafdkvnjakfjnvkajfnvknjafkvnjakdfnvkandfvknafkjvnkfjnvkdfgdfnjafknvakjnfv'

        print(f'----- {test_news.title}')
        form_class = AddNewsForm
        self.assertRaisesMessage(expected_exception, expected_message, AddNewsForm.clean_title(), title = check_title)
        
        
"""

        '''
        assertFormError(response, form, field, errors): 
            Проверяет наличие определенных ошибок формы в ответе.

        assertRaisesMessage(expected_exception, expected_message, callable, *args, **kwargs): 
            Проверяет, что сообщение об исключении, вызванное callable, соответствует ожидаемому сообщению.

        self.assertFieldOutput(EmailField, {'a@a.com': 'a@a.com'}, {'aaa': [u'Enter a valid email address.']})
        
        #c = Client()
        #print(f'login is---{c.login()}')
        '''
      