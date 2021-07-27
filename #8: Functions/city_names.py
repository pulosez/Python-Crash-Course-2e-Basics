# 8.6.
def city_country(city, country):
    line = f"{city}, {country}"
    return line.title()

print(city_country("lviv", "ukraine"))
print(city_country("tokio", "japan"))
print(city_country("london", "england"))
