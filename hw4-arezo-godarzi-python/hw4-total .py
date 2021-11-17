import csv
import random
'''Define the class Quiz to build the quiz'''
class Quiz:
    def __init__(self,question,answer):
       self.question=question
       self.answer=answer
       self.score = 0
       self.question_number = 0

    def check_user_answer(self):
        user_answer = input("")
        if user_answer == self.answer:

            print("Correct answer!!")
            return True
        else:
            print('wrong answer!!')
            return False

    def __str__(self):
        return f"Qestion No:{self.question}"
'''Define a class TrueFalse to build a quiz that inherits from the main class'''
 class TrueFalse(Quiz):
    pass


'''Define a class Multiple_choice to build a quiz that inherits from the main class'''
 class Multiple_choice(Quiz):
     pass
'''Define a class ShortAnswer to build a quiz that inherits from the main class'''
class ShortAnswer(Quiz):
    def check_answers(self):
        user_answer = input("").lower().lower()

        if user_answer == self.answer:

            print("Correct answer!!")
            return True
        elif user_answer != self.answer:
            print('wrong answer!!')
            return False
'''Check Scores'''
 class Score:
     def __init__(self,score,winner,loser):
        self.score=score

        '''use the file'''
        def file(q, correct, wrong, score, remaining):

            with open('result.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)


with open('new.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
