import requests



def get_hotels(location):




    url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchFlights"

    querystring = {"sourceAirportCode":"BOM","destinationAirportCode":"DEL","date":"2024-03-12","itineraryType":"ONE_WAY","sortOrder":"PRICE","numAdults":"1","numSeniors":"0","classOfService":"ECONOMY","pageNumber":"1","currencyCode":"INR"}

    headers = {
	"X-RapidAPI-Key": "61d1deaf2bmshccfada1959a3f8fp15542djsn8e4bfad5a87f",
	"X-RapidAPI-Host": "booking-com15.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

    return(response.json())
# Add more functions for other endpoints as needed
