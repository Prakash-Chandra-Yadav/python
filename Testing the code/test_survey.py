#create the new test class 
from survey import AnonymousSurvey
def test_store_single_response():
    '''test that the single response is stored corerctly'''
    question = "what language did you first learned to speak?"
    language_survey = AnonymousSurvey(question )
    language_survey.store_responses('English')
    assert 'English' in language_survey.responses

##now lets test if the class method can take more than one values 
def test_store_three_responses():
    question = "whats the first language that you learned?"
    language_survey = AnonymousSurvey(question)
    responses = ['English','German','Spanish']
    for response in responses:
        language_survey.store_responses(response)
    for response in responses:
        assert response in language_survey.responses