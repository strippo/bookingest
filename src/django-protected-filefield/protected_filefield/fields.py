import os
from django.contrib.formtools.tests.wizard import storage
from django.core.exceptions import SuspiciousOperation
from django.core.files.storage import DefaultStorage, FileSystemStorage, Storage
from django.db import models
from django.utils._os import safe_join
import protected_filefield.settings

 
class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name):
        name = super(CustomFileSystemStorage, self).get_available_name(name)

        return name.replace("'", "")


protected_storage = CustomFileSystemStorage(location=protected_filefield.settings.PRIVATE_ROOT,
                                            base_url=protected_filefield.settings.PRIVATE_URL)

class ProtectedFileField(models.FileField):
    def __init__(self, verbose_name=None, name=None, upload_to='', storage=None, **kwargs):
        storage = protected_storage
        super(ProtectedFileField, self).__init__(verbose_name, name, upload_to, storage, **kwargs)
    
    
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^protected_filefield\.fields\.ProtectedFileField"])
