try:
    score = float(input("enter your score: "))
    float(score)
    if (score < 0.0 or score > 1.0):
        print("please score should be between 0.0 to 1.0")
    elif score < 0.6:
        print("F")
    elif score >= 0.6:
        print("D")
    elif score >= 0.7:
        print("C")
    elif score >= 0.8:
        print("B")
    elif score >= 0.9:
        print("A")
except:
    print("Bad score")