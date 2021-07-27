# 8.5.
def describe_city(name, country='ukraine'):
    print(f"\n{name.title()} is in {country.title()}")

describe_city('lviv')
describe_city('japan', 'tokio')
describe_city(name='london', country='england')
