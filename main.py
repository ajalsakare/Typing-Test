import csv
import random
import time
from datetime import datetime, timedelta
import os

words_list = []
with open('words.csv', 'r') as file:    # reads a csv file and creates a list of words
    reader = csv.reader(file)
    fields = next(reader)
    for row in reader:
        words_list.append(row[1])

random.shuffle(words_list)

t = datetime.now()
# print(t)
updated_time = t + timedelta(seconds=60)
# print(updated_time)

score = count = total_chars = correctly_typed = 0

print("\n\t\t\t\tWelcome to Typing Test\n")
print("\t\t\t\tThe test will start 10 seconds after you have executed the program,\n\t\t\t\tYou have total 60 seconds\n")
print("\t\t\t\tYou have to type words from the suggessted box of words.\n\t\t\t\t(Sequence is not necessary)\n")
print("\t\t\t\tSO BE READY !!")
time.sleep(10)


while datetime.now() < updated_time:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(f'\n\n\n\n\n\n\n\n\t\t\t\t\t{words_list[:5]}\n\n')
    word = input('\t\t\t\t\t')
    count += 1
    for w in word:
        total_chars += 1
    if word in words_list:
        score += 1
        for w in word:
            correctly_typed += 1
        words_list.remove(word)

print(f'\n\n\t\t\t\t\tYou got {score}/{count}')
print(f'\n\t\t\t\t\tTotal characters typed: {total_chars}\tCorrectly typed characters: {correctly_typed}')
