from django.core.files.storage import FileSystemStorage
from django.conf import settings

class CustomStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = settings.MEDIA_ROOT + '/ckeditor_uploads/'
        super().__init__(*args, **kwargs)
