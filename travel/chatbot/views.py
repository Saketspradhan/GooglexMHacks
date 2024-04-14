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
from dotenv import load_dotenv, dotenv_values 

load_dotenv() 
 

conversation_questions =['Tell me about place you want to visit. ','What is your budget? ','What is duration of your trip? ','How many people are going for trip. ', 'Tell me about your interests. ']
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
m1 = genai.GenerativeModel('gemini-pro')
gem = m1.start_chat(history=[])
res = []
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


            location = getLoc(image_file)
            coord = get_coord(location)
            request.session['coord'] = coord
            request.session['loc'] = location
            return redirect('/map')
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

    survey_response = request.session.get('survey_response')

    print(survey_response)

    if survey_response is not None:
        itinerary = generate_itinerary(survey_response)

        return render(request, 'itinerary.html', {'itinerary': itinerary})

    else:
        return redirect('survey')
def get_bot_response(request, user_input):
    # If this is the start of the conversation, skip `Echo`
    if request.session.get('question_index') is None:
        request.session['question_index'] = 0
        return conversation_questions[0]
    else:
        # Increment the question index
        request.session['question_index'] += 1
        question_index = request.session['question_index']

        # Check if all questions have been asked; resume echoing user's input
        if question_index >= len(conversation_questions):

            return ask_gem(user_input)
        else:
            res.append(user_input)
            return conversation_questions[question_index]

def ask_gem(user_input):
    if len(res) == 5:
        s2 = "You are an extremely experienced travel guide for destinations all across the globe. Make a travel plan for" + \
             res[0] + " under " + res[1] + " since that is the user's strict budget " + \
             ". The duration of the trip is, in days, " + res[2] + ".Additionally there are " + res[
                 3] + "people going on the trip." + "The person's interests include- " + res[4] + ".\
         Please give careful consideration of the user's interests and other parameters as detailed. Output results in JSON format."
        response = gem.send_message(s2)
        res.append(1)
        return response
    s3 = "You are a travel expert that is being consulted. Make an updated travel plan that is similar to your last one, but considers the following feedback from the user: " + user_input
    ans = gem.send_message(s3)
    

    ans = str(ans._result.candidates[0].content.parts[0])[5:]
    html_r= ans.replace('\n', '<br>')
    return html_r





@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        bot_response = get_bot_response(request, user_input)
        # Here we create HTML for the bot response
        response_html = f"<div>Bot: {bot_response}</div>"
        return HttpResponse(response_html)
    else:
        request.session['question_index'] = None
        return render(request, 'chatbot.html')


def my_map_view(request):
    context = {}
    try:
        if 'coord' in request.session:
            coord = [float(n) for n in request.session['coord']]
            context['lat'] = coord[0]
            context['lon'] = coord[1]
        if 'loc' in request.session:
            context['location'] = request.session['loc']
    except Exception as e:
        request.session.flush()
        request.session['err'] = True
        return redirect('routes')

    return render(request, 'map.html',context=context)
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
