from django.db import models
from pdf2image import convert_from_path
from io import BytesIO
from django.core.files import File
from PIL import Image

class EBook(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='ebooks/')
    thumbnail = models.ImageField(upload_to='ebook_thumbnails/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.file and not self.thumbnail:
            # Generate thumbnail
            poppler_path = r'C:\Program Files\poppler-24.07.0\Library\bin'
            file_path = self.file.path
            try:
                pdf_pages = convert_from_path(file_path, first_page=1, last_page=1, poppler_path=poppler_path)
                if pdf_pages:
                    pdf_page = pdf_pages[0]
                    thumb_io = BytesIO()
                    pdf_page.save(thumb_io, format='JPEG')
                    thumbnail = File(thumb_io, name=f'{self.file.name}.jpg')
                    self.thumbnail.save(thumbnail.name, thumbnail, save=False)
                    print(f"Thumbnail created and saved as {thumbnail.name}")
            except Exception as e:
                print(f"Error generating thumbnail: {e}")
        super().save(*args, **kwargs)

