def city_country(city, country, population=15):
    if population:
        full_name = f"{city}, {country} population-{population}"
    else:
        full_name = f"{city}, {country}"
    return full_name.title()

# city_country('virginia beach', 'united states')