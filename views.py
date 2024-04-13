from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from .content.Itinerary.myapp.forms import SurveyForm

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
