from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SurveyForm, ImageUploadForm
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import subprocess
from .models import ImageModel
import json
from .utils import handle_uploaded_image
import PIL
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyAQ96EkKc8hKij32Q3kgHc7G3I0xBCEf0Q"
genai.configure(api_key=GOOGLE_API_KEY)
def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def routes(request):
    # If POST request, process the form data

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            image_file = form.cleaned_data['image']

            # Process the image (e.g. resizing, converting to grayscale, etc.)

            # Now you can use the processed image to create a new ImageModel instance,
            # or whatever else you need to do with it.
            # For example, assuming your ImageModel has an ImageField or FileField called image:
            # new_image = ImageModel(image=processed_image)
            # new_image.save()
            location = getLoc(image_file)
            coord = get_coord(location)

            return render(request, 'map.html', {"coord":coord})
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


def my_map_view(response):
    return render(response, 'map.html')
def get_coord(location):
    curl_command = [
        'curl',
        '-X',
        'POST',
        '-H',
        'Content-Type: application/json',
        '-d',
        f'{{"location": "{location}"}}',
        'https://saketspradhan--googlexmhacks-location-to-coordinates-loc-fd4653.modal.run'
    ]
    response = None
    try:
        output = subprocess.check_output(curl_command, stderr=subprocess.STDOUT, text=True)
        last_line = output.strip().split('\n')[-1]

        # Parse the last line as JSON to extract the coordinates
        coordinates = json.loads(last_line)
        latitude = coordinates[0]
        longitude = coordinates[1]
        response = [latitude,longitude]
    except subprocess.CalledProcessError as e:
        response = None

    return response

def getLoc(img):
    model = genai.GenerativeModel(model_name='gemini-pro-vision')


    #image = Image.open(BytesIO(aws_url_response.content))
    image = PIL.Image.open(img)
    prompt = "What is the address of the place in the image?"
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt, image])
    return response.text