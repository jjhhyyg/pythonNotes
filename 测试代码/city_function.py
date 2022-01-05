def city_country(city, country, population=''):
    if population:
        string = f"{city}, {country}".title() + f" - population {population}"
    else:
        string = f"{city}, {country}".title()
    return string
