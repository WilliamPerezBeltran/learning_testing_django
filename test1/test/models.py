from django.test import TestCase
from test1.models import Author, Book


class TestModels(TestCase):
    def test_book_has_an_author(self):
        print("=========test_book_has_an_author=========")
        book = Book.objects.create(title="The man in the high castle")
        philip = Author.objects.create(first_name="philip", last_name="Dickertsron")
        juliana = Author.objects.create(first_name="juliana", last_name="Gonzales")
        book.authors.set([philip.pk, juliana.pk])
        self.assertEqual(book.authors.count(), 2)
