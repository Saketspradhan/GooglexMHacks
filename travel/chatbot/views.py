from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ImageUploadForm

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def routes(request):
    # If POST request, process the form data

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)



        output_text = handle_uploaded_image(request.FILES['file'])

        # Redirect or show the result to the user
        return render(request, 'result.html', {'output_text': output_text})
    else:
      # If not a POST request, just show the empty form
      form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})


def handle_uploaded_image(image):


  processed_text = "Processed text based on the image."

  return processed_text

