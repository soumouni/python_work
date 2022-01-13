import unittest
from survey import AnonymousSurvey

class test_one_reponse_only (unittest.TestCase):
    """testing the survey results in case there is only one answer"""
    def setUp (self):
        """creates a survey and sets up the responses to be used for testing"""
        question='what language did you first learn to speak? '
        self.my_survey=AnonymousSurvey(question)
        self.threeresponses=['english', 'french', 'spanich']

    def test_single_response (self):
        """test that a single reponse is stored properly"""
        self.my_survey.store_responses(self.threeresponses[0])
        self.assertIn(self.threeresponses[0], self.my_survey.responses)

    def test_three_responses (self):
        """test that 3 reponses are stored correctly"""
        for response in self.threeresponses:
            self.my_survey.store_responses(response)
        for response in self.threeresponses:
            self.assertIn(response, self.my_survey.responses)


if __name__=='__main__':
    unittest.main()