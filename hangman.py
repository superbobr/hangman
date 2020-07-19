import random

print('H A N G M A N')
while True:
    start_game = input('Type "play" to play the game, "exit" to quit: ')
    if start_game == 'play':
        word_lst = ['python', 'java', 'kotlin', 'javascript']
        word = list(random.choice(word_lst))
        hint_word = list('-' * len(word))
        life = 8
        letters = []
        while life != 0:
            print()
            print(''.join(hint_word))
            user_input = input('Input a letter: ')
            if len(user_input) != 1:
                print('You should input a single letter')
                continue
            elif not (96 < ord(user_input) < 123):
                print('It is not an ASCII lowercase letter')
                continue
            elif user_input in letters:
                print('You already typed this letter')
                continue
            elif user_input not in word:
                letters.append(user_input)
                print('No such letter in the word')
                life -= 1
                continue
            else:
                letters.append(user_input)
                for _ in word:
                    index = word.index(user_input)
                    hint_word[index] = user_input
                if '-' not in hint_word:
                    print(word)
                    print('You guessed the word!')
                    print('You survived!/n')
                    break
        else:
            print('You are hanged!/n')
    else:
        break
