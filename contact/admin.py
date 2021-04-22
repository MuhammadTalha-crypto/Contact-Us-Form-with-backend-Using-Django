from django.contrib import admin
#Importing "data" model from the "models.py" of "contact" app
from contact.models import data
# Registering "data" model.
admin.site.register(data)