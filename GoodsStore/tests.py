from django.test import TestCase, Client
from django.urls import reverse

from .models import Article


class ArticleTestCase(TestCase):

    def setUp(self):
        Article.objects.create(  # Создание товара
            title='Pen',
            description='test your might',
            price=22,
            upload_img='picture'
        )

    def test_article_exist(self):
        """Created article exist in the database"""
        article = Article.objects.get(title="Pen")
        self.assertIsNotNone(article)
        self.assertEqual(article.title, "Pen")
        self.assertEqual(article.upload_img, 'picture')

    def test_str_return_title(self):
        article = Article.objects.get(title="Pen")
        self.assertEqual(str(article), "Pen")


class ArticleCreateViewTest(TestCase):

    def setUp(self):
        self.article = Article.objects.create(

            title='Pen',
            description='test your might',
            price=22,
            upload_img='picture'
        )

    def test_status_create_page(self):
        response = self.client.get(reverse('add_article'))
        self.assertEqual(response.status_code, 200)
        print(response)

    def test_redirect(self):
        response = self.client.post(
            reverse('add_article'),
            {'title': "Blade", 'description': "test your might", 'price': 22,
             'upload_img': "picture"})

        self.assertEqual(response.status_code, 200)

class IndexViewPageTest(TestCase):

    def setUp(self):
        pass

    def test_homepage(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class ArticleViewPageTest(TestCase):

    def setUp(self):
        pass

    def test_homepage(self):
        response = self.client.get(reverse('detail_all'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_all.html')


class ArticleUpdateViewTest(TestCase):

    def setUp(self):
        self.article = Article.objects.create(

            title='Pen',
            description='test your might',
            price=22,
            upload_img='picture'
        )

    def test_update_article(self):
        response = self.client.post(reverse('update_detail', kwargs={'pk': self.article.id}),
                         {'title': "Blade", 'description': "test your might", 'price': 22, 'upload_img': "picture"})
        print("UPDATE test",response)
        self.assertEqual(Article.objects.first().title, 'Blade')
        self.assertEqual(response.status_code, 302)

class ArticleDeleteViewTest(TestCase):

    def setUp(self):
        self.article = Article.objects.create(

            title='Pen',
            description='test your might',
            price=22,
            upload_img='picture'
        )

    def test_delete_article(self):
        self.client.delete(reverse('article_delete', kwargs={'pk': self.article.id}))
        self.assertEqual(Article.objects.count(), 0)  # возвращ. кол-во элементов


class ArticleDetailViewTest(TestCase):

    def setUp(self):
        self.article = Article.objects.create(
            title='Pen',
            description='test your might',
            price=22,
            upload_img='picture'
        )

    def test_detail_page(self):
        response = self.client.get(self.article.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')
