from django.shortcuts import render

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
