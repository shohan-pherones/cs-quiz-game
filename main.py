import requests

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.questions = questions

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (Yes/No): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.question_number}")

res = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
question_data = res.json()["results"]

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = "Yes" if question["correct_answer"] == "True" else "No"
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz Complete!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")