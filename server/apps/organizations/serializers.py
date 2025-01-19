from rest_framework import serializers

from apps.organizations import models


class FinancialOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FinancialOrganization
        fields = '__all__'


class FinancialOrganizationNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FinancialOrganizationNews
        fields = '__all__'
