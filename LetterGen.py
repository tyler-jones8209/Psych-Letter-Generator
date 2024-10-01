import random

def LetterGen():
    letter_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    with open("RandNum.txt", "w") as file:
        for i in range(10):
            random_numbers = [random.randint(0, 25) for x in range(3)]
            random_letters = []
            for num in random_numbers:
                random_letters.append(letter_list[num])
            result = "".join(random_letters) + "\n"
            file.write(result)

LetterGen()