import csv

navne = []

with open('navne.txt', newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        navne = row


navne.sort(key=lambda x: (x[0], len(x)))

print(navne)

letters = {}
for navn in navne:
    for letter in navn:
        if letter in letters:
            letters[letter] += 1

        else:
            letters[letter] = 1


print(letters)
