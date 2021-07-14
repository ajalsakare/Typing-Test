import csv

new_word = ''
words_list = []
to_add = []
to_add_indexed = []

with open('words.csv', 'r+', newline='') as csvfile:
    csvreader = csv.reader(csvfile)     # creates a csv reader object
    csvwriter = csv.writer(csvfile)     # created a csv writer object

    fields = next(csvreader)
    for row in csvreader:
        # rows.append(row)
        words_list.append(row[1])

    # print(rows)
    # print(words_list)

    choice = int(input('Do you want to enter paragraph or single words at a time ? Enter 1 or 2:\n'))
    length = len(words_list)
    if choice == 1:
        print("Note: While adding words using paragraph, please remove words with apostrophe like didn't, wouldn't..etc")
        words = input("Enter a paragraph to extract words from it:\n").split(' ')
        formatted_words = []
        for w in words:
            for l in w:
                if not l.isalpha():
                    w = w.replace(l, '')
            formatted_words.append(w.lower())
        print(formatted_words)
        for f in formatted_words:
            if f not in words_list:
                if f not in to_add:
                    to_add.append(f)
                    to_add_indexed.append([length + 1, f])
                    length += 1
                    print(f'{f} added!')
            else:
                print(f'{f} already exits\n')
        csvwriter.writerows(to_add_indexed)
        exit(0)

    elif choice == 2:
        while True:
            new_word = input("Enter new words:\n").lower()
            if new_word != 'stop':
                if new_word not in words_list:
                    if new_word not in to_add:
                        to_add.append(new_word)
                        to_add_indexed.append([length+1, new_word])
                        length += 1
                        print(f'{new_word} added!')
                else:
                    print(f'{new_word} already exits, please enter new word.\n')
            else:
                # print(to_add)
                csvwriter.writerows(to_add_indexed)
                exit(0)
