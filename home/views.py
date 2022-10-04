from django.shortcuts import render
from datetime import datetime
import requests
from home.models import Home


## function that gets the random quote
def get_random_quote():
	try:
		## making the get request
		response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
		if response.status_code == 200:
			## extracting the core data
			json_data = response.json()
			data = json_data['data']

			## getting the quote from the data
			return data[0]['quoteText']
		else:
			return "Error while getting quote"
	except:
		return "Something went wrong! Try Again!"
        
Quote = { "first":get_random_quote(),
"second":get_random_quote(),
"third":get_random_quote()
}

# Create your views here.
def index(request):
	if request.method == "POST":
		email = request.POST.get('email')
		desc = request.POST.get('desc')
		contact = Home(email = email, desc=desc, date=datetime.today())
		contact.save
	return render(request, 'home.html', Quote)
