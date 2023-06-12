import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from .serializers import *


class GeneTest(APITestCase):
    gene1 = None
    gene2 = None
    good_url = ''
    bad_url = ''

    def setUp(self):
        self.gene1 = GeneFactory.create(pk=1, gene_id="gene1")
        self.gene1 = GeneFactory.create(pk=2, gene_id="gene2")
        self.good_url = reverse('gene_api', kwargs={'pk': 1})
        self.bad_url = "/api/gene/H/"

    def tearDown(self):
        EC.objects.all().delete()
        Sequencing.objects.all().delete()
        Gene.objects.all().delete()
        ECFactory.reset_sequence(0)
        SequencingFactory.reset_sequence(0)
        GeneFactory.reset_sequence(0)

    def test_geneDetailReturnsSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('entity' in data)
        self.assertEqual(data['entity'], 'Plasmid')

    def test_geneDetailReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
    """
    def test_geneDetailReturnsSuccess(self):
        gene = GeneFactory.create(pk=1, gene_id="gene1")
        url = reverse('gene_api', kwargs={'pk': 1})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_geneDetailReturnFailOnBadPk(self):
        gene = GeneFactory.create(pk=2, gene_id="gene2")
        url = "/api/gene/H/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    """