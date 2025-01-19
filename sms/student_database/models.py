from django.db import models
from pdf2image import convert_from_path
from io import BytesIO
from django.core.files import File
import os
from PIL import Image


class EBook(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='ebooks/')
    thumbnail = models.ImageField(upload_to='ebook_thumbnails/', blank=True, null=True)

    def save(self, *args, **kwargs):
        """Override save method to generate thumbnail from the first page of the PDF"""
        if self.file and not self.thumbnail:
            # Generate thumbnail from the first page of the PDF
            poppler_path = r'C:\Program Files\poppler-24.07.0\Library\bin'  # Adjust this to your Poppler path
            file_path = self.file.path
            try:
                # Convert the first page of the PDF to an image
                pdf_pages = convert_from_path(file_path, first_page=1, last_page=1, poppler_path=poppler_path)
                if pdf_pages:
                    first_page = pdf_pages[0]
                    thumb_io = BytesIO()
                    first_page.save(thumb_io, format='JPEG')  # Save the image as JPEG
                    thumbnail = File(thumb_io, name=f'{self.file.name}_thumbnail.jpg')
                    self.thumbnail.save(thumbnail.name, thumbnail, save=False)
                    print(f"Thumbnail created and saved as {thumbnail.name}")
            except Exception as e:
                print(f"Error generating thumbnail: {e}")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Override delete method to delete both the file and thumbnail from storage"""
        # First, delete the file from the storage
        if self.file:
            # Delete the actual file from the filesystem
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)

        if self.thumbnail:
            # Delete the thumbnail file from the filesystem
            if os.path.isfile(self.thumbnail.path):
                os.remove(self.thumbnail.path)

        # Call the superclass's delete method to delete the object
        super().delete(*args, **kwargs)

    @property
    def thumbnail_url(self):
        """Returns the URL of the thumbnail or a default image if not available"""
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return '/static/images/default_thumbnail.jpg'  # Fallback image path

    def __str__(self):
        return self.title
