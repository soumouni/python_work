from survey import AnonymousSurvey
#define a question and make a survey
question='what language did you first learn to speak'
my_survey=AnonymousSurvey(question)

my_survey.show_question()
print("enter 'q' anytime you want to quit")
while True:
    response=input('language: ')
    if response =='q':
        break
    else:
        my_survey.store_responses(response)

print("Thank you for your participation, bellow are survey's responses: \n")
my_survey.show_results()
