from django.db import models
import os
from pdf2image import convert_from_path
from io import BytesIO
from django.core.files import File
from PIL import Image

class EBook(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='ebooks/')
    thumbnail = models.CharField(max_length=10, blank=True, null=True)
    file_extension = models.CharField(max_length=10, blank=True, null=True)  # New field for file extension

    def save(self, *args, **kwargs):
        # Populate file extension
        if self.file:
            self.file_extension = os.path.splitext(self.file.name)[1][1:].lower()  # Extract the extension without the dot

        # Generate thumbnail from the first page of the PDF if applicable
        if self.file and self.file_extension == 'pdf' and not self.thumbnail:
            poppler_path = r'C:\Program Files\poppler-24.07.0\Library\bin'  # Adjust this to your Poppler path
            file_path = self.file.path
            try:
                pdf_pages = convert_from_path(file_path, first_page=1, last_page=1, poppler_path=poppler_path)
                if pdf_pages:
                    first_page = pdf_pages[0]
                    thumb_io = BytesIO()
                    first_page.save(thumb_io, format='JPEG')
                    thumbnail = File(thumb_io, name=f'{self.file.name}_thumbnail.jpg')
                    self.thumbnail.save(thumbnail.name, thumbnail, save=False)
            except Exception as e:
                print(f"Error generating thumbnail: {e}")

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        if self.thumbnail:
            if os.path.isfile(self.thumbnail.path):
                os.remove(self.thumbnail.path)
        super().delete(*args, **kwargs)

    @property
    def thumbnail_url(self):
        """Returns the URL of the thumbnail or a default image based on file extension."""
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return f'/static/images/{self.file_extension}_logo.png'  # Default image based on extension

    def __str__(self):
        return self.title
