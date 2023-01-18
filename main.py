import requests as rs
import tkinter as tk
import csv
import random as rn

"""""""""""""""""
DOWNLOAD LATEST
"""""""""""""""""

URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT1aGnC0w_8tdLizE5NTXX0NI5u-shqK4qikxTqh4omMzYkVup5fx9KedGn-J4AOOuT_n3EA18maMLd/pub?gid=0&single=true&output=csv'
try:
    res=rs.get(url=URL)
    open('questions.csv', 'wb').write(res.content)
    print("Dernière version des questions téléchargée!")
except:
    print("Téléchargement de la dernière version des questions échoué")

"""""""""""""""""
OPEN CSV
"""""""""""""""""

class Question:

    def __init__(self, Q, R, M):
        self.question = Q
        self.reponse = R
        self.matiere = M

    def Q(self):
        return self.question

    def R(self):
        return self.reponse

    def M(self):
        return self.matiere

DATA = []

with open('questions.csv', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for i,row in enumerate(csv_reader):
        if i>0:
            Q, R, M = row
            DATA.append(Question(Q, R, M))
            line_count += 1
    print(f'{line_count} questions trouvées !')

"""""""""""""""""
GUI
"""""""""""""""""
if len(DATA)>0:

    root = tk.Tk()
    root.geometry("1280x720")

    frame= tk.Frame(root, relief='sunken', bg= "white")
    frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)

    DEFANSWER = "Réponse cachée"

    def fmt(t):
        words = t.split(" ")
        res = []
        for i,word in enumerate(words):
            if i%16==0 and i>0:
                res.append("\n")
            res.append(word)
        return " ".join(res)

    def getQuestion():
        global root
        if(len(DATA)==0):
            root.quit()
        newQuestion = rn.choice(DATA)
        DATA.remove(newQuestion)
        return newQuestion

    actualQuestion = getQuestion()

    Title = tk.Label(frame, text="SYSINFO Questionnaire", font=('Arial', 32), width=100, height=2, bg="white", fg="#6c5ce7")
    questionText = tk.Label(frame, text=fmt(actualQuestion.Q()), font=('Arial', 15), width=100, height=2, bg="white")
    matiereText = tk.Label(frame, text=fmt(actualQuestion.M()), font=('Arial', 12), width=100, height=2, bg="white", fg="#050505")
    answerText = tk.Label(frame, text=DEFANSWER, font=('Arial', 15), width=100, height=15, bg="white")

    def show_question():
        global actualQuestion
        global questionText
        global answerText
        actualQuestion = getQuestion()

        questionText.config(text=fmt(actualQuestion.Q()))
        matiereText.config(text=fmt(actualQuestion.M()))
        answerText.config(text=DEFANSWER)

    def show_answer():
        global actualQuestion
        global answerText
        answerText.config(text=fmt(actualQuestion.R()))

    BTN_NEXT = tk.Button(frame, text="Prochaine question", command=show_question)
    BTN_ANSWER = tk.Button(frame, text="Voir la réponse", command=show_answer)

    Title.pack()
    questionText.pack()
    matiereText.pack()
    answerText.pack()
    BTN_NEXT.pack()
    BTN_ANSWER.pack()

    root.mainloop()