from employee import Employeee
import pytest 

def test_give_defualt_raise():
    '''test if the default raise is being added in the annual salary'''
    emp1 = Employeee('Prakash','Chandra',10000)
    emp1.give_raise()
    assert emp1.annual_salary == 15000
def test_give_custom_raise():
    '''test if the custom raise is being added in the annual salary'''
    emp1 = Employeee('Prakash','Chandra',10000)
    emp1.give_raise(8000)
    assert emp1.annual_salary == 18000
