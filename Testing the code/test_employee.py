from employee import Employeee
import pytest 
@pytest.fixture
def emp1():
    '''create one objet for all the test functions'''
    emp1 = Employeee('Prakash','Chandra',10000)
    return emp1

def test_give_defualt_raise(emp1):
    '''test if the default raise is being added in the annual salary'''
    emp1.give_raise()
    assert emp1.annual_salary == 15000
def test_give_custom_raise(emp1):
    '''test if the custom raise is being added in the annual salary'''
    emp1.give_raise(8000)
    assert emp1.annual_salary == 18000
