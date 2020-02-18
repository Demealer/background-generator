import random
import sys

sys.argv
print("running 1game222")


def carry_me_over(num, num2):
    return num * num2


run_the_game = False
numbers_to_randomize = []
new_var = 109

while True:
    user_input1 = input('Give me a number between 1 and 100: ')
    try:
        if int(user_input1):
            print(f'You chose: ' + user_input1 +
                  ', please choose another number.')
            if numbers_to_randomize.count(user_input1):
                print("This number was already chosen :S")
            else:
                numbers_to_randomize.append(user_input1)
                if len(numbers_to_randomize) > 1:
                    print("Let's start the game now!")
                    run_the_game = True
                    break

    except:
        print("Please type a number between 1 and 100 only.")
    continue

if run_the_game:
    run_the_game = False
    numbers_to_randomize.sort()
    any_number = range(
        int(numbers_to_randomize[0]), int(numbers_to_randomize[1]))
    print(numbers_to_randomize)
    print(
        input(range(int(numbers_to_randomize[0]), int(numbers_to_randomize[1]))))
    the_number = random.choice(any_number)
    #print(f'{the_number} is the number, and it was chosen between this: {numbers_to_randomize}')

while True:
    user_input2 = input(
        f'You chose {numbers_to_randomize} as the numbers you wanted. So we chose a random number in between those numbers. \n Guess what the number is! ')
    try:
        if int(user_input2):
            print(f'You chose: {int(user_input2)}!')
            if int(user_input2) >= int(numbers_to_randomize[0]) and int(user_input2) <= int(numbers_to_randomize[1]):
                if int(user_input2) == the_number:
                    print("\nYou got it! \n  Great job! \n  ~~~Game Over~~~")
                    break
                else:
                    print("Close...! That's not the number but try again.")
            else:
                print(
                    f'Please type a number between {numbers_to_randomize} only.')
                continue
    except:  # TypeError as err:
        print(f'Please type a number betwee22n {numbers_to_randomize} only.')
    continue


print("Yup")
