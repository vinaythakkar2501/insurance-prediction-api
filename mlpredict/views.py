from multiprocessing import context
from statistics import mode
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pickle
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from mlpredict.forms import medicalForm
from mlpredict.serializers import FeaturesSerializers, MedicalDataSerializaers,LifeDataSerializers,CarDataSerializers
from mlpredict.models import features,MedicalData,LifeData,CarData

def index(request):
    return render(request,'mlpredict/index.html')
def home(request):
    return render(request,'mlpredict/home.html')
def Mpredict(age,sex,bmi,children,smoker,region):
    param1 = age
    if sex == 'male':
        param2 = 0
    else:
        param2 = 1
    param3 = bmi
    param4 = children
    if smoker == 'yes':
        param5 = 0
    else:
        param5 = 1
    if region == 'southeast':
        param6 = 0
    elif region == 'southwest':
        param6 = 1
    elif region == 'northeast':
        param6 = 2
    else:
        param6 = 3
    
    with open('medical_model','rb') as f:
        model = pickle.load(f)
    amount = model.predict([[param1,param2,param3,param4,param5,param6]])
    # return amount
    if amount > 0 :
        return amount/2
    else:
        return 'Somthing is wrong'

def Lpredict(age,diabetes,bloodpressure,transplant,chronicdisease,height,weight,allergies,cancer,surgeries):
    with open('life_model','rb') as f:
        model = pickle.load(f)
    amount = model.predict([[age,diabetes,bloodpressure,transplant,chronicdisease,height,weight,allergies,cancer,surgeries]])
    if amount > 0 :
        return amount/2
    else:
        return 'Somthing is wrong'

def Cpredict(Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner):
    with open('car_model','rb') as f:
        model = pickle.load(f)
    amount = model.predict([[Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]])
    return amount
    
def medicalform(request):
    fm = medicalForm()
    amount = 0
    if request.method == 'POST':
        form = medicalForm(request.POST)
        if form.is_valid():
            amount = Mpredict(
                form.cleaned_data['Age'],
                form.cleaned_data['sex'],
                form.cleaned_data['bmi'],
                form.cleaned_data['children'],
                form.cleaned_data['smoker'],
                form.cleaned_data['region'],
            )
            form.save()
    context = {'form':fm,'amount':amount}
    return render(request,'mlpredict/medical_form.html',context)
    
# class FeatureList(APIView):
#     def get(self, request, format=None):
#          users = features.objects.all()
#          serializer = FeaturesSerializers(users, many=True)
#          return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = FeaturesSerializers(data=request.data)
#         if serializer.is_valid():
#             amount = Mpredict(
#                 serializer.validated_data['Age'],
#                 serializer.validated_data['sex'],
#                 serializer.validated_data['bmi'],
#                 serializer.validated_data['children'],
#                 serializer.validated_data['smoker'],
#                 serializer.validated_data['region'],
#             )
#             serializer.save()
#             return Response(amount, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#          user = self.get_object(pk)
#          user.delete()
#          return Response(status=status.HTTP_204_NO_CONTENT)

class MedicalDataList(APIView):
    def get( self, request, format=None):
        Mdata = MedicalData.objects.all()
        serializer = MedicalDataSerializaers(Mdata, many = True)
        return Response(serializer.data)
    def post(self, request, format = None):
        serializer = MedicalDataSerializaers(data=request.data)
        if serializer.is_valid():
            amount = Mpredict(
                serializer.validated_data['age'],
                serializer.validated_data['gender'],
                serializer.validated_data['bmi'],
                serializer.validated_data['children'],
                serializer.validated_data['smoker'],
                serializer.validated_data['region'],
            )
            # serializer.save()
            return Response([serializer.data, amount],status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LifeDataList(APIView):
    def get( self, request, format=None):
        Ldata = LifeData.objects.all()
        serializer = LifeDataSerializers(Ldata, many = True)
        return Response(serializer.data)
    def post(self, request, format = None):
        serializer = LifeDataSerializers(data=request.data)
        if serializer.is_valid():
            amount = Lpredict(
                serializer.validated_data['age'],
                serializer.validated_data['diabetes'],
                serializer.validated_data['bloodpressure'],
                serializer.validated_data['transplant'],
                serializer.validated_data['chronicdisease'],
                serializer.validated_data['height'],
                serializer.validated_data['weight'],
                serializer.validated_data['allergies'],
                serializer.validated_data['cancer'],
                serializer.validated_data['surgeries']
            )
            # serializer.save()
            return Response([serializer.data, amount],status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CarDataList(APIView):
    def get( self, request, format=None):
        Cdata = CarData.objects.all()
        serializer = CarDataSerializers(Cdata, many = True)
        return Response(serializer.data)
    def post(self, request, format = None):
        serializer = CarDataSerializers(data=request.data)
        if serializer.is_valid():
            amount = Cpredict(
                serializer.validated_data['Year'],
                serializer.validated_data['Present_Price'],
                serializer.validated_data['Kms_Driven'],
                serializer.validated_data['Fuel_Type'],
                serializer.validated_data['Seller_Type'],
                serializer.validated_data['Transmission'],
                serializer.validated_data['Owner']
            )
            # serializer.save()
            return Response([serializer.data, amount],status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# data.replace({'sex':{'male':0,'female':1}},inplace=True)
# data.replace({'smoker':{'yes':0,'no':1}},inplace=True)
# data.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}},inplace=True)
#age,sex,bmi,children,smoker,region
# age,diabetes,bloodpressure,transplant,chronicdisease,height,weight,allergies,cancer,surgeries

# {
# "age" : 19,
# "diabetes" : 0,
# "bloodpressure" :0,
# "transplant" : 0,
# "chronicdisease" :0,
# "height" : 170,
# "weight" : 46,
# "allergies" : 1,
# "cancer" : 0,
# "surgeries" : 0
# }

# { 
# "Year":2014,
# "Present_Price":5.59,
# "Kms_Driven":27000,
# "Fuel_Type":0,
# "Seller_Type":0,
# "Transmission":0,
# "Owner":0
# }