import csv
import time
from datetime import datetime, timedelta
import random
from tkinter import *
import multiprocessing as mp


def read_words(filename):     # reads words from a csv file and returns a list of words
    words_list = []
    with open('words.csv', 'r') as file:
        reader = csv.reader(file)
        fields = next(reader)
        for row in reader:
            words_list.append(row[1])
    random.shuffle(words_list)
    return words_list


class TypingTest:

    def __init__(self):
        self.window = Tk()
        self.timer_label = Label(self.window, text='01:00', fg='black')
        self.text = Entry(self.window, justify='center', fg='black')
        self.score_label = Label(self.window, text='', fg='black')
        self.characters = Label(self.window, text='', fg='black')
        self.words_list = read_words('words.csv')
        self.score = self.count = self.correctly_typed_char = self.total_char = 0
        self.time_limit = datetime.now()
        self.time_count = 59

    def timer(self):                # one minute timer for typing test
        if self.time_count >= 0:
            minutes = self.time_count // 60
            seconds = self.time_count % 60
            if minutes < 10:
                minutes = str(0) + str(minutes)
            if seconds < 10:
                seconds = str(0) + str(seconds)
            # print(f'{minutes}:{seconds}')
            self.timer_label.config(text=f'{minutes}:{seconds}')
            self.time_count -= 1
            self.timer_label.after(1000, self.timer)
        elif self.time_count == -1:
            self.text.focus_set()
            self.score_label.config(text=f"You got: {self.score}/{self.count}")
            self.characters.config(text=f'Total chars typed: {self.total_char}  Correct chars typed: {self.correctly_typed_char}')
            # print(f'Time after limit: {datetime.now()}')

    def display(self):              # displays the gui

        def space_bar(event):           # this function gets triggered when user presses space or enter
            if datetime.now() < self.time_limit:
                self.count += 1
                entered_word = self.text.get().lower()
                for _ in entered_word:
                    self.total_char += 1
                if entered_word in self.words_list:
                    self.score += 1
                    for _ in entered_word:
                        self.correctly_typed_char += 1
                    self.words_list.remove(entered_word)
                    suggestion_label.config(text=self.words_list[:5])
                self.text.delete(0, len(self.text.get()))
            else:
                self.text.focus_set()
                self.score_label.config(text=f"You got: {self.score}/{self.count}")
                self.characters.config(text=f'Total chars typed: {self.total_char}  Correct chars typed: {self.correctly_typed_char}')
                # print(f'Time after limit: {datetime.now()}')

        def start():            # when user presses start button test starts
            self.time_count = 59
            p2 = mp.Process(target=tt.timer())      # creates a second process to run simultaneously
            p2.start()                              # with the main program (it starts only
            self.text.delete(0, len(self.text.get()))       # when user presses start)
            self.score_label.config(text='')
            self.text.focus()
            self.time_limit = datetime.now() + timedelta(seconds=60)
            # print(f'Time at Start: {datetime.now()}')
            # print(f'Time Limit: {self.time_limit}')

        def reset():            # when user presses reset button all values are reset
            self.text.delete(0, len(self.text.get()))
            self.text.focus_set()
            self.score_label.config(text='')
            random.shuffle(self.words_list)
            suggestion_label.config(text=self.words_list[:5])
            self.score = self.count = self.correctly_typed_char = self.total_char = 0
            self.characters.config(text='')
            self.timer_label.config(text='01:00')
            self.time_count = -2

        # main window
        # window = Tk()
        self.window.title('Typing Test')
        self.window.geometry('700x600')

        # welcome label
        welcome_label = Label(self.window, text='Welcome to Typing Test', fg='red')
        welcome_label.pack()
        welcome_label.config(font=('Comic Sans MS', 24, 'bold'))

        # start button
        start_button = Button(self.window, text='Start', width=10, bg='yellow', fg='black', command=start)
        start_button.place(x=100, y=100)
        start_button.config(font=('Times New Roman', 20, 'bold'))

        # timer
        self.timer_label.place(x=310, y=110)
        self.timer_label.config(font=('Times New Roman', 22, 'bold'))
        # self.timer_label.after(1000, self.timer)

        # reset button
        reset_button = Button(self.window, text='Reset', width=10, bg='yellow', fg='black', command=reset)
        reset_button.place(x=420, y=100)
        reset_button.config(font=('Times New Roman', 20, 'bold'))

        # word suggestions
        suggestion_label = Label(self.window, text=self.words_list[:6], fg='black')
        suggestion_label.place(x=90, y=210)
        suggestion_label.config(font=('Comic Sans MS', 22, 'bold'))

        # user input
        # text = Entry(self.window, justify='center', fg='black')
        self.text.place(x=200, y=320)
        self.text.config(font=('Times New Roman', 22, 'normal'))

        # score
        # score_label = Label(self.window, text='', fg='black')
        self.score_label.place(x=200, y=370)
        self.score_label.config(font=('Comic Sans MS', 24, 'bold'))

        # total characters typed
        # characters = Label(self.window, text='', fg='black')
        self.characters.place(x=30, y=450)
        self.characters.config(font=('Comic Sans MS', 18, 'bold'))

        self.window.bind('<Return>', space_bar)
        self.window.bind('<space>', space_bar)
        self.window.mainloop()


tt = TypingTest()
if __name__ == '__main__':
    p1 = mp.Process(target=tt.display())        # this is the main process which runs simultaneously
    p1.start()                                  # with the timer
