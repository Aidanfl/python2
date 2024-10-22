# Enter a numerical score between 0.0 and 1.0, and this script will return your corresponding letter grade (A to F).
# The grading scale is as follows:
# A: 90% and above, B: 80%-89%, C: 70%-79%, D: 60%-69%, F: below 60%.
# After you input your score, the letter grade will be displayed.


def grade(score):
    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'

score = float(input("Enter score: "))
LetterGrade = grade(score)
print(LetterGrade)
