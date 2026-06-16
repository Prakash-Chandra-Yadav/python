#create the new test class 
import pytest
from survey import AnonymousSurvey
@pytest.fixture
def language_survey():
    '''a survey object that will be avaliavle to all the functions'''
    question = 'what language did you first learned to speak?'
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    '''test that the single response is stored corerctly'''
    language_survey.store_responses('English')
    assert 'English' in language_survey.responses

##now lets test if the class method can take more than one values 
def test_store_three_responses(language_survey):
    responses = ['English','German','Spanish']
    for response in responses:
        language_survey.store_responses(response)
    for response in responses:
        assert response in language_survey.responses