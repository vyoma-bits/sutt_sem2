import requests
def flights(to,date,adults):

    url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"

    querystring = {"sourceAirportCode":"DEL","destinationAirportCode":to,"date":date,"itineraryType":"ONE_WAY","sortOrder":"PRICE","numAdults":adults,"numSeniors":"0","classOfService":"BUSINESS","pageNumber":"1","currencyCode":"INR"}
    headers = {
	"X-RapidAPI-Key": "23ffcdd161msh2f900f53717411ap1b95b2jsn7386a33d5477",
	"X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)

    return(response.json())