"""
untuk bisa membuat table dan simpan data dari model class yg kita buat di fle ini

harus run command:

python manage.py migrate
python manage.py makemigrations <your_app_name>

"""

from django.db import models

# step by step crate a blog models
"""
1. Create your a blog models.
    - title
    - pub_date
    - body
    - image
    
2. add Blog app to the settings
3. crate a migration
4. migrate 
5. add blog models to the admin area
"""

# create Blog Models
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')