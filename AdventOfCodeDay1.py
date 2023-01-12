import os

def question1():
    with open('./input.txt', 'r') as file:
        dirr = file.read()
        dirrArr = list(dirr)
        answer = sum([1 if x == '(' else -1 for x in dirrArr])
        print('floor:', answer)

def question2():
    with open('./input.txt', 'r') as file:
        dirr = file.read()
        dirrArr = list(dirr)
        floor = 0
        counter = 0
        for current_item in dirrArr:
            if current_item == '(':
                floor += 1
            elif current_item == ')':
                floor -= 1
            counter += 1
            if floor < 0:
                print('Basement entered at:', counter)
                return

question2()