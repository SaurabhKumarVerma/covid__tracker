from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST":
        country = request.POST['country']

        url = "https://coronavirus-19-api.herokuapp.com/countries/{}"
        search = country
        
        api  = requests.get(url.format(search)).json()
        return render(request,'home.html' , {'api':api})

    else:
        try:
            url = "https://coronavirus-19-api.herokuapp.com/countries/{}"
            search = country

            api  = requests.get(url.format(search)).json()
        except Exception as e:
            api = "Error ...!"











    return render(request,'home.html' , {'api':api})









def india(request):
    import json
    import requests

    url = 'https://api.covidindiatracker.com/total.json'
    surl = 'https://covid-india-cases.herokuapp.com/states/'
    try:
        api = requests.get(url).json()
        sapi = requests.get(surl).json()
    except Exception as e:
        api = 'Error...!'


    return render(request, 'india.html', {'api':api,'sapi':sapi})
