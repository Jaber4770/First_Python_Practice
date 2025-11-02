#15. **Dictionary Search**
#    Create a dictionary of countries and capitals.
#    Input a country name → show its capital.

countries_capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "Japan": "Tokyo",
    "India": "New Delhi",
    "Brazil": "Brasília",
    "Australia": "Canberra",
    "Canada": "Ottawa"
}
def Search():
    country = input("enter the country name: ")
    capital = countries_capitals[country]
    print(f"capital of {country} is {capital}")

Search()