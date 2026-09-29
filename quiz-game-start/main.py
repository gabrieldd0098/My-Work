from question_model import QModel
from quiz_brain import QBrain
from data import QData

QBank = []
for Qs in QData:
    QText = Qs["text"]
    QAns = Qs["answer"]
    new_Q = QModel(text=QText, answer=QAns)
    QBank.append(new_Q)

QZ = QBrain(q_list=QBank)

while QZ.still_has_qs():
    QZ.next_question()

print("The Quiz has come to a conclusion!")
print(f"The FINAL SCORE was: {QZ.score}/{QZ.q_num}")
