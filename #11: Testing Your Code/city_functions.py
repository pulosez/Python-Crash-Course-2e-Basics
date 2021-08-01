def get_city_info(city, country, population=0):
    city_info = f"{city.title()}, {country.title()}"
    if population:
        city_info += f" - population {population}"
    return city_info
