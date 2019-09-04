"""
setiap perubahan di file models.py ini hrs melakukan cmd:

python manage.py makemigrations jobs

Migrations for 'jobs':
  jobs/migrations/0001_initial.py
    - Create model Job

setelah config models.py di save dg cmd diatas lakukan cmd:
python manage.py migrate

agar terjadi update di DB


Kalau berhasil create model utk create fields/table di DB akan generate filey 0001_initial.py
di direktory 'migrations' dimana akan create fields/table yang kita ploting di class 'Job'

"""

from django.db import models


# Create your models here.
# membuat class 'Job' dimana object 'models.Model' adalah milik Django
# untuk membuat input data ke Database
class Job(models.Model):

    # upload image akan di save di directory 'images'
    image = models.ImageField(upload_to='images/')

    # ini untuk simpan data summary di home page ke DB
    # krn datanya bertipe 'text' maka di gunakan 'CharField' di DB
    summary = models.CharField(max_length=200)

    #