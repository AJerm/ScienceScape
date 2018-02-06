from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
#from .commands import UploadedFiles


def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})
