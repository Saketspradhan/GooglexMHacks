from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SurveyForm, ImageUploadForm
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            # Save the form data to the session
            request.session['survey_response'] = form.cleaned_data
            # Redirect to the itinerary generation view
            return redirect('generate_itinerary')
    else:
        form = SurveyForm()

    return render(request, 'survey.html', {'form': form})


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
# Basic logic for the chatbot's response
def get_bot_response(user_input):
    # This is where you'd integrate an actual chatbot service or logic
    return "Echo: " + user_input

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        bot_response = get_bot_response(user_input)
        return JsonResponse({"message": bot_response})
    return render(request, 'chatbot.html')

def my_map_view(request):
    # Prepare context data if needed
    return render(request, "map.html", {})
