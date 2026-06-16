def get_city_name(city,country,population=0):
    '''return the name of the city along with the country'''
    if population:
        city_info = f'{country.title()}, {city.title()} -population {population}'
    else: 
        city_info = f'{country.title()}, {city.title()}'
    return city_info
