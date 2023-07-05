from rest_framework import serializers


try:

    from blood.models import Stock
    from blood.models import BloodRequest
    from patient.models import Patient
    from donor.models import Donor
    from donor.models import BloodDonate

except:
    pass 

class StockSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Stock
        except:
            pass    
        fields = '__all__'

class BloodRequestSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = BloodRequest
        except:
            pass    
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Patient
        except:
            pass    
        fields = '__all__'

class DonorSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Donor
        except:
            pass    
        fields = '__all__'

class BloodDonateSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = BloodDonate
        except:
            pass    
        fields = '__all__'

