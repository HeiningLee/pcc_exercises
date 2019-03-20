def city_function(city, country, population=0):
    if population:
        format_name = city + ', ' + country + ' - ' + str(population)
    else:
        format_name = city + ', ' + country
    return format_name.title()
