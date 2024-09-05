from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EBook
from pdf2image import convert_from_path
from .forms import EBookForm

def student_database(request):
    std_links = {
        '1st': 'https://docs.google.com/spreadsheets/d/13mzbxjSHssrCUeRCgYLBv3ixAJX_UYk8/edit?usp=sharing&ouid=117687025981177099460&rtpof=true&sd=true',
        '2nd': 'https://docs.google.com/spreadsheets/d/1s3rbcl24JsoG4QSVV_UaB8a6glwJ4Avg/edit?usp=sharing&ouid=117687025981177099460&rtpof=true&sd=true',
        '3rd': 'https://docs.google.com/spreadsheets/d/13elDb6lGVCiBm0Xjppy_yNGPmZl660bs/edit?usp=sharing&ouid=117687025981177099460&rtpof=true&sd=true',
        '4th': 'https://docs.google.com/spreadsheets/d/1o0uhT2qs_Rwg4HHFz-juHyGq-Rh1apIH/edit?usp=sharing&ouid=117687025981177099460&rtpof=true&sd=true',
        '5th': 'https://docs.google.com/spreadsheets/d/1J_Q_Py2nXxb1a-W8JXhsQThRyR6DcSTI/edit?usp=sharing&ouid=117687025981177099460&rtpof=true&sd=true',
        '6th': 'https://docs.google.com/spreadsheets/d/1sRI3GM0QHEEg8QoLeDjm5QI4rAO3VUfF/edit?usp=sharing&ouid=117687025981177099460&rtpof=true&sd=true',
        '7th': 'https://docs.google.com/spreadsheets/d/1R9HU2GFN88S2ObwIPhSzpUJFUH8-86Xz/edit?usp=sharing&ouid=117687025981177099460&rtpof=true&sd=true',
    }
    return render(request, 'student_database/template/student_database.html', {'std_links': std_links})

def ebook_list(request):
    ebooks = EBook.objects.all()
    return render(request, 'student_database/template/ebook_list.html', {'ebooks': ebooks})


def ebook_upload(request):
    if request.method == 'POST':
        form = EBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ebook_list')
    else:
        form = EBookForm()
    return render(request, 'student_database/template/ebook_upload.html', {'form': form})


def ebook_delete(request, ebook_id):
    ebook = get_object_or_404(EBook, id=ebook_id)
    if request.method == 'POST':
        ebook.delete()
        return redirect('ebook_list')
    return render(request, 'student_database/template/ebook_delete_confirm.html', {'ebook': ebook})


def test_pdf_conversion():
    poppler_path = r'C:\Program Files\poppler-24.07.0\Library\bin'
    pdf_path = r'C:\Users\Shivkumar Hegonde\PycharmProjects\schoolsystem\sms\media\Mukhyamantri mazi shala.pdf'
    try:
        pdf_pages = convert_from_path(pdf_path, first_page=1, last_page=1, poppler_path=poppler_path)
        print(f"Number of pages: {len(pdf_pages)}")
    except Exception as e:
        print(f"Error: {e}")

test_pdf_conversion()