"""
untuk mengaktifkan apps yg kita buat, hrs config di settings.py
"""

from django.apps import AppConfig



# class ini secara automatis di generate oleh Django saat buat app dg cmd: python migrate startapp <app_name>
class JobsConfig(AppConfig):
    name = 'jobs'
