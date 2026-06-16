class AnonymousSurvey:
    '''collect the anonuymous ansewer to the survay question.'''
    def __init__(self,question):
        '''setting the default attributes'''
        self.question = question 
        self.responses = []
    def show_questions(self):
        '''shows the survay questions'''
        print(self.question)
    def store_responses(self,new_response):
        '''stpre the single response to the survay'''
        self.responses.append(new_response)
    def show_results(self):
        '''show all the responses that have been given'''
        print("survay response")
        for response in self.responses:
            print(response)