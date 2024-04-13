from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ImageUploadForm
from .content.Itinerary.myapp.forms import SurveyForm
from .forms import SurveyForm
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






def generate_itinerary(request):
  # We will call Google Gemini AI here to generate the itinerary
      # Retrieve the survey response from the session
    survey_response = request.session.get('survey_response')

    print(survey_response)

    if survey_response is not None:
        # Generate the itinerary using your AI
        itinerary = generate_itinerary(survey_response)  # Replace with your AI function

        # Display the itinerary
        return render(request, 'itinerary.html', {'itinerary': itinerary})

    else:
        # If there's no survey response in the session, redirect to the survey view
        return redirect('survey')
