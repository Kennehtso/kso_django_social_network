from random import randint, choice
import factory

from django.test import TestCase
from django.conf import settings
from django.core.files import File

from .models import *

class ECFactory(factory.django.DjangoModelFactory):
    ec_name = "transferase"

    class Meta:
        model = EC

class SequencingFactory(factory.django.DjangoModelFactory):
    sequencing_factory = "Sanger"
    factory_location = "UK"

    class Meta:
        model = Sequencing


class GeneFactory(factory.django.DjangoModelFactory):
    # gene_id = "GeneX"
    # entity = "Plasmid"
    # start = 12
    # stop = 100
    gene_id = factory.Sequence(lambda n: 'gene%d' % n+str(1))
    # entity = factory.Faker('sentence', nb_words=1)
    entity = choice(['Plasmid', 'Chromosome'])
    start = randint(1, 100000)
    stop = start+randint(1, 100000)

    sense = "+"
    start_codon = "M"
    sequencing = factory.SubFactory(SequencingFactory)
    ec = factory.SubFactory(ECFactory)
    access = 0

    class Meta:
        model = Gene
