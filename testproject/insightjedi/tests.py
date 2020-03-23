from rest_framework import status
from rest_framework.test import APITestCase

from model_mommy import mommy

from django.urls import reverse


class TestDocumentViewSet(APITestCase):
    def setUp(self):
        self.document = mommy.make(
            'insightjedi.Document',
            type='testtype'
        )

    def tearDown(self):
        self.document.delete()

    def get_document_list_url(self, org_id):
        return reverse('insightjedi:document-list')

    def get_document_detail_url(self, org_id, org_archive_id):
        return reverse('insightjedi:document-detail', kwargs={
            'pk': org_archive_id
        })

    def test_document_list(self):
        response = self.client.get(self.get_document_list_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 1)

    def test_document_detail(self):
        response = self.client.get(
            self.get_document_detail_url(self.document.id)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'testtype')

    def test_document_create(self):
        response = self.client.post(
            self.get_document_list_url(),
            {'type': 'testtype'}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_document_delete(self):
        response = self.client.delete(
            self.get_document_detail_url(self.document.id)
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
