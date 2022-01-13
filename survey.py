class AnonymousSurvey:
    """collect anonymous answers to survey questions"""
    def __init__ (self, question):
        """store a question and prepares to store answers"""
        self.question=question
        self.responses=[]
    
    def show_question(self):
        """print the question"""
        print(self.question)

    def store_responses (self, new_response):
        """store any new response"""
        self.responses.append(new_response)
    
    def show_results (self):
        """show survey's responses"""
        print('survey results:')
        for response in self.responses:
            print(f'-{response.title()}')


