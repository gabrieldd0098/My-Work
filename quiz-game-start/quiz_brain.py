class QBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.score = 0
        self.q_list =q_list

    def still_has_qs(self):
        return self.q_num < len(self.q_list)

    def next_question(self):
        current_q = self.q_list[self.q_num]
        self.q_num += 1
        user_ans = input(f"Q.{self.q_num}: {current_q.text} (T/F): ")
        self.check_ans(user_ans, current_q.answer)

    def check_ans(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("✅")
        else:
            print("❎")
        print(f"The correct answer is {correct_answer}")
        print(f"The current score is {self.score}/{self.q_num}")
        print("\n")


