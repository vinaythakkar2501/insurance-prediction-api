from django.contrib import admin
from mlpredict.models import MedicalData,features,LifeData,CarData


class PredictionAdmin(admin.ModelAdmin):
    list_display = ('Age','sex','bmi','children','smoker','region')
class MedicalAdmin(admin.ModelAdmin):
    list_display = ('age','gender','bmi','children','smoker','region')

class LifeAdmin(admin.ModelAdmin):
    list_display = ('age','diabetes','bloodpressure','transplant','chronicdisease','height','weight','allergies','cancer','surgeries')

class CarAdmin(admin.ModelAdmin):
    list_display = ('Year','Present_Price','Kms_Driven','Fuel_Type','Seller_Type','Transmission','Owner')

# Register your models here.
admin.site.register(features,PredictionAdmin)
admin.site.register(MedicalData,MedicalAdmin)
admin.site.register(LifeData,LifeAdmin)
admin.site.register(CarData,CarAdmin)