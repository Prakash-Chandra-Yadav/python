from name_function import get_formatted_name
def test_first_last_name():
    '''does names like prakash chandra works'''
    formatted_name = get_formatted_name('prakash','chandra')
    assert formatted_name == 'Prakash Chandra'
def test_first_middle_last():
    '''does names like prakash chandra yadav works'''
    formatted_name = get_formatted_name('Prakash','Yadav',middle='Chandra')
    assert formatted_name == 'Prakash Chandra Yadav'