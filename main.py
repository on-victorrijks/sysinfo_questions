import requests as rs
import tkinter as tk
import csv
import random as rn
import os

"""""""""""""""""
DOWNLOAD LATEST
"""""""""""""""""

URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT1aGnC0w_8tdLizE5NTXX0NI5u-shqK4qikxTqh4omMzYkVup5fx9KedGn-J4AOOuT_n3EA18maMLd/pub?gid=0&single=true&output=csv'
try:
    res=rs.get(url=URL)
    if os.path.exists("questions.csv"):
        os.remove("questions.csv")
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
            Q, R, M = row[0], row[1], row[2]
            DATA.append(Question(Q, R, M))
            line_count += 1
    print(f'{line_count} questions trouvées !')

"""""""""""""""""
GUI
"""""""""""""""""
nbQ = len(DATA)
nbQ_r = 1
if len(DATA)>0:

    root = tk.Tk()
    root.geometry("1280x720")

    frame= tk.Frame(root, relief='sunken', bg= "white")
    frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)

    DEFANSWER = "Réponse cachée"
    NEWLINE = "µ"


    def fmt(t):
        words = t.split(" ")
        counter = 0
        res = []
        for i,word in enumerate(words):
            if counter==16 and i>0:
                res.append("\n")
                counter = 0
            if word==NEWLINE:
                res.append("\n")
                counter = 0
            else:
                res.append(word)
                counter+=1
        return " ".join(res)

    def getQuestion():
        global nbQ_r
        global root
        if(len(DATA)==0):
            root.quit()
        nbQ_r+=1
        #newQuestion = DATA[len(DATA)-1]
        newQuestion = rn.choice(DATA)
        DATA.remove(newQuestion)
        return newQuestion

    actualQuestion = getQuestion()

    Title = tk.Label(frame, text=f"Question 1/{nbQ}", font=('Arial', 32), width=100, height=2, bg="white", fg="#6c5ce7")
    questionText = tk.Label(frame, text=fmt(actualQuestion.Q()), font=('Arial', 15), width=100, height=2, bg="white")
    matiereText = tk.Label(frame, text=fmt(actualQuestion.M()), font=('Arial', 12), width=100, height=2, bg="white", fg="#050505")
    answerText = tk.Label(frame, text=DEFANSWER, font=('Arial', 15), width=100, height=15, bg="white")

    def show_question():
        global Title
        global actualQuestion
        global questionText
        global answerText
        actualQuestion = getQuestion()

        Title.config(text=f"Question {nbQ_r}/{nbQ}")
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