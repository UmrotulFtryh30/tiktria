from django.shortcuts import render

# Create your views here.
def kegiatan(request):
    judul = ["Program Studi Agribisnis", "Program Studi Agroeteknologi", "Program Studi Ilmu Perikanan", "Program Studi Teknologi Pangan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexkegiatan.html', konteks)