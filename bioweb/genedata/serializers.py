from rest_framework import serializers
from .models import *
"""
# Hard way
class GeneSerializer(serializers.Serializer):
    gene_id = serializers.CharField(required=True, allow_blank=False, max_length=256)
    entity = serializers.CharField(required=True, allow_blank=False, max_length=256)
    start = serializers.IntegerField()
"""
class ECSerializer(serializers.ModelSerializer):
    class Meta:
        model = EC
        fields = ['id','ec_name']

class SequencingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequencing
        fields = ['id', 'sequencing_factory','factory_location']

class GeneSerializer(serializers.ModelSerializer):
    ec = ECSerializer()
    sequencing = SequencingSerializer()

    class Meta:
        model = Gene
        fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon', 'ec', 'sequencing']

    def create(self, validated_data):
        ec_data = self.initial_data.get('ec')
        sequencing_data = self.initial_data.get('sequencing')
        gene = Gene(**{
            **validated_data,
            'ec' : EC.objects.get(pk=ec_data['id']),
            'sequencing': Sequencing.objects.get(pk=sequencing_data['id'])
        })
        gene.save()
        return gene

class GeneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon']
