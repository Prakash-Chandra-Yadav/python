from survey import AnonymousSurvey
#define a question and make a survey 
question = 'what language did you first learned to speak?'
language_survey = AnonymousSurvey(question)

##show the question and show the responses to the question 
language_survey.show_questions()
print("please enter 'q' to end the survey")
while True: 
    response = input("language: ")
    if response != 'q':
        language_survey.store_responses(response)
    else: 
        break 
##show the survay result 
print("\nThankyou every one for participating in the survey")
language_survey.show_results()