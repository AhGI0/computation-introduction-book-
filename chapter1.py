# i want to make an itergraion to know how many lines i have in my file

A = open("file.txt", "rt")
tracker = 0
new = []

for i in A:

    tracker += 1
    # print(f'{tracker} {i}')

print(f'u have {tracker} lines')


# print(tracker)s
