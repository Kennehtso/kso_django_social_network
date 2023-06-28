import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status

from .model_factories import *
from .serializers import *

class GeneSerialiserTest(APITestCase):
    gene1 = None
    geneserializer = None

    def setUp(self):
        self.gene1 = GeneFactory.create(pk=1, gene_id="gene1")
        self.geneserializer = GeneSerializer(instance=self.gene1)

    def tearDown(self):
        EC.objects.all().delete()
        Sequencing.objects.all().delete()
        Gene.objects.all().delete()
        ECFactory.reset_sequence(0)
        SequencingFactory.reset_sequence(0)
        GeneFactory.reset_sequence(0)
    
    def test_genSerializer(self):
        data = self.geneserializer.data
        self.assertEqual(set(data.keys()), set(['gene_id', 'sequencing',
                                        'sense', 'start', 'stop',
                                        'entity', 'ec',
                                        'start_codon']))
	

    def test_geneSerilaiserGeneIDIsHasCorrectData(self):
        data = self.geneserializer.data
        self.assertEqual(data['gene_id'], "gene1")

class GeneTest(APITestCase):
    gene1 = None
    gene2 = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    def setUp(self):
        self.gene1 = GeneFactory.create(pk=1, gene_id="gene1")
        self.gene1 = GeneFactory.create(pk=2, gene_id="gene2")
        self.gene3 = GeneFactory.create(pk=3, gene_id="gene3")
        self.good_url = reverse('gene_api', kwargs={'pk': 1})
        self.bad_url = "/api/gene/H/"
        self.delete_url = reverse('gene_api', kwargs={'pk': 3})

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
        
    def test_geneDetailDeleteIsSuccessful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)

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
    
 
class GeneListTest(APITestCase):
    def test_geneListReturnsSuccess(self):
        GeneFactory.create_batch(3)

        url = '/api/genes'  
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = GeneListSerializer(instance=response.data, many=True)
        self.assertEqual(serializer.data, [{'gene_id': 'gene1', 'entity': 'Plasmid', 'start': 12, 'stop': 100, 'sense': '+', 'start_codon': 'M'},
                                            {'gene_id': 'gene2', 'entity': 'Plasmid', 'start': 34, 'stop': 67, 'sense': '+', 'start_codon': 'M'},
                                            {'gene_id': 'gene3', 'entity': 'Chromosome', 'start': 56, 'stop': 89, 'sense': '-', 'start_codon': 'M'}])

    def test_geneListReturnsEmpty(self):
        url = '/api/genes'  
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_geneListCreateNewGene(self):
        new_gene_data = {
            'gene_id': 'gene4',
            'entity': 'Plasmid',
            'start': 90,
            'stop': 120,
            'sense': '+',
            'start_codon': 'M',
        }

        url = '/api/genes' 
        response = self.client.post(url, data=new_gene_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, new_gene_data)
        self.assertEqual(Gene.objects.filter(gene_id='gene4').count(), 1)

    def test_geneListCreateNewGeneMissingRequiredField(self):
        new_gene_data = {
            'gene_id': 'gene4',
            'entity': 'Plasmid',
            'stop': 120,
            'sense': '+',
            'start_codon': 'M',
        }

        url = '/api/genes'  
        response = self.client.post(url, data=new_gene_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'start': ['This field is required.']})

        
class ECTest(APITestCase):
    ec1 = None
    ec2 = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    def setUp(self):
        self.ec1 = ECFactory.create(pk=1, ec_name="EC 1")
        self.ec2 = ECFactory.create(pk=2, ec_name="EC 2")
        self.good_url = reverse('ec_api', kwargs={'pk': 1})
        self.bad_url = "/api/ec/H/"
        self.delete_url = reverse('ec_api', kwargs={'pk': 2})

    def tearDown(self):
        EC.objects.all().delete()
        ECFactory.reset_sequence(0)

    def test_ecetailReturnsSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue('ec_name' in data)
        self.assertEqual(data['ec_name'], 'EC 1')

    def test_ecDetailReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
        
    def test_ecDetailDeleteIsSuccessful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)
