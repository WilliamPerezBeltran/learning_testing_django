from django.test import TestCase
from test1.models import Author, Book, Event
from model_bakery import baker


class TestModels(TestCase):

    # otra forma de testear el many to many relationsships
    # def test_book_has_an_author(self):
    # 	print("=========test_book_has_an_author=========")
    # 	book = Book.objects.create(title="The man in the high castle")
    #        philip = Author.objects.create(first_name="Philip", last_name="K. Dick")
    #        juliana = Author.objects.create(first_name="Juliana", last_name="Crain")
    #        philip.book_set.add(book)
    #        juliana.book_set.add(book)
    #        self.assertEqual(book.authors.count(), 2)

    def test_book_has_an_author(self):
        print("=========test_book_has_an_author=========")
        book = Book.objects.create(title="The man in the high castle")
        philip = Author.objects.create(first_name="philip", last_name="Dickertsron")
        juliana = Author.objects.create(first_name="juliana", last_name="Gonzales")
        book.authors.set([philip.pk, juliana.pk])
        self.assertEqual(book.authors.count(), 2)

    def test_model_str(self):
        print("=========test_model_str=========")
        book = Book.objects.create(title="The man in the high castle")
        philip = Author.objects.create(first_name="philip", last_name="Dickertsron")
        self.assertEqual(str(book), "The man in the high castle")
        self.assertEqual(str(philip), "philip Dickertsron")

    # en vez de hacer esto
    # def test_event_model(self):
    #        event = Event.objects.create(
    #            title="Some title",
    #            seo_title="Some Seo title",
    #            seo_description="Some description",
    #            abstract="The abstract",
    #            body="The body",
    #            duration=2,
    #            slug="the-slug",
    #            start_date=datetime.now(),
    #            end_date=datetime.now(),
    #            price=800,
    #            location="Rome",
    #            published=False,
    #        )
    #    se hace lo de abajo,
    #    mucho mas rapido

    def test_event_model(self):
        print("=========test_event_model=========")
        event = baker.make(Event, title="The man in the high castle presentation")
        self.assertEqual(str(event), "The man in the high castle presentation")
