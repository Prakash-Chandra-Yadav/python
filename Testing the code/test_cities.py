from city_function import get_city_name
def test_city_country():
    '''lets see if the function works correctly'''
    city_details = get_city_name('Kathmandu','Nepal')
    assert city_details == 'Nepal, Kathmandu'