from django.urls import reverse
from rest_framework.test import APITestCase
from model_mommy import mommy


class ElementCreateAPITestCases(APITestCase):
    def setUp(self):
        super().setUp()
        self.view = reverse('api:list_create')

    def test_list_notes(self):
        mommy.make('notes.Note',
                   _quantity=5)

        response = self.client.get(self.view, format='json')

        self.assertEqual(200, response.status_code)
        self.assertEqual(5, len(response.data))

    def test_create_note(self):
        data = {'message': 'Some message%$@'}

        response = self.client.post(self.view, data, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(2, response.data['unique_words'])
