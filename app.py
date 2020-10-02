import random

print('HI GUYS WELCOME TO PLAY AHORCADOS')
# words = ['unlucky', 'steps', 'so', 'last', 'let', 'something', 'sometimes']
words = ['unlucky','unlucky']
def draw(n=[]):
    print(['unlucky', 'steps', 'so', 'last', 'let', 'something', 'sometimes'])
    container = """\t\t\t+------------------+
    \t\t\t|               |
    \t\t\t{0}\t\t\t\t|
    \t\t  {1} {2} {3}\t\t\t\t|
    \t\t\t{4}\t\t\t\t|
    \t\t   {5} {6}\t\t\t\t|
    \t\t\t\t\t\t\t|
    \t\t\t\t\t\t\t|
    \t\t\t\t\t\t\t|
    \t\t\t\t\t\t\t|
    \t\t\t\t\t\t\t|
    \t\t\t\t\t\t\t|===================
    """.format(n[0], n[1], n[2], n[3], n[4], n[5], n[6])
    return container


def lucky(words):
    # do a random the list words
    random.shuffle(words)
    # random item from the list words
    word_random = random.choice(words)
    return word_random

def play():
    # call to the function lucky()
    word = list(lucky(words))
    # stored the body in a tupla
    failed = ('O','/','|','\\','|','/','\\')
    # assigning  values
    number_failed, parameters = 0, ["","","","","","",""]
    guess_letter = len(word) * ["(-)"]
    # print the function draw
    print(draw(parameters))
    print(guess_letter)

    for i in range(len(word)):
        # input the user for enter the letter okey
        enter_letter= input("enter the letter ok")
        # if the input of user is okey
        for j in range(len(word)):
            if enter_letter == word[j]:
                guess_letter[j] = enter_letter
                word[j] = '.'
                print(draw(parameters))
                print(guess_letter)
                break
        else:
            parameters[number_failed] = failed[number_failed]
            number_failed += 1
            print(draw(parameters))
            print(guess_letter)

    return "bye"

def main():
    begin  = play()
    print(begin)

main()
