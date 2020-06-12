def computegrade(score):
    error_msg = 'Bad score'
    try:
        score = float(score)
    except:
        return print(error_msg)
        quit()

    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            return print('A')
        elif score >= 0.8:
            return print('B')
        elif score >= 0.7:
            return print('C')
        elif score >= 0.6:
            return print('D')
        elif score < 0.6 and score >= 0.0:
            return print('F')
    else:
        return print(error_msg)

score_input = input("Enter Score between 0.0 and 1.0: ")
computegrade(score_input)
