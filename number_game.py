import random

def input_numbers():
    min = input('Please input minimum number: ')
    max = input('Please input maximum number: ')
    return min, max

def input_prediction():
    return input('Guess the random number that will be output: ')

def judge(min, max, prediction):
    answer = random.randint(min, max)
    return prediction == answer

min, max = input_numbers()
if max <= min:
    print("Please enter a maximum value equal to or greater than the minimum value.") 
else:
    for num in range(5):
        print(f"The random number will be between {min} and {max}.")
        prediction = input_prediction()
        if judge(int(min), int(max), int(prediction)):
            print("You win!!")
            break
        else:
            print("You wrong... Try again")
    if num == 4:
        print("Game Over")
