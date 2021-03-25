def question_choice(question, number_of_choice, no_choice = "This is not right choice, choose again"):
    print(question)
    print("{} ~ {}", format(i+1, len(number_of_choice)+1))
    answer = input()
    while True:
        if answer in range(1, number_of_choice+1):
            return = answer
            break
        else:
            print(no_choice)