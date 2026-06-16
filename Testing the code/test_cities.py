from city_function import get_city_name
def test_city_country():
    '''lets see if the function works correctly'''
    city_details = get_city_name('Kathmandu','Nepal')
    assert city_details == 'Nepal, Kathmandu'
def test_city_popiulation():
    '''lets check if the function accepts the population'''
    city_details = get_city_name('kathmandu','Nepal',population=10000)
    assert city_details == 'Nepal, Kathmandu -population 10000'