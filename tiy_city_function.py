def city_country_formatting (city, country,population=''):
    """return a neatly formatted city,country name"""
    if population:
        formatted_name=f"{city.title()}, {country.title()}, population: {population}"
    else:
        formatted_name=f"{city.title()}, {country.title()}"

    return formatted_name