# 6.11.
cities = {
    'lviv': {
        'country': 'ukraine',
        'population': 721_301,
        'area': 182,
        },
    'tokio': {
        'country': 'japan',
        'population': 13_185_502,
        'area': 2_194,
        },
    'prague': {
        'country': 'czech republic',
        'population': 1_272_690,
        'area': 496,
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    area = city_info['area']

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The area is {area} km2.")
