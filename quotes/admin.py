from django.contrib import admin
from .models import Stock #need to import the model we created

# Register your models here.
admin.site.register(Stock)
