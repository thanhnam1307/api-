from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.Book = Book.objects.create(
            title='The Test Book',
            subtitle='Test title', 
            author='Test Author',
            isbn = '1331242')
    
    def test_book_content(self):
        self.assertEqual(self.Book.title, 'The Test Book')
        self.assertEqual(self.Book.subtitle, 'Test title')
        self.assertEqual(self.Book.author, 'Test Author')
        self.assertEqual(self.Book.isbn, '1331242')

    def test_book_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Test Book')
        self.assertTemplateUsed(response, 'books/book_list.html')
        