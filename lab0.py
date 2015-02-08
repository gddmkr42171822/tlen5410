'''
Lab 1
Description: Write a program that will calculate your final grade
in the class
'''

def totalPoints(l):
    l.append(raw_input('Enter total hw percentage earned: '))
    l.append(raw_input('Enter total lab percentage earned: '))
    l.append(raw_input('Enter total project percentage earned: '))
    l.append(raw_input('Enter total quiz percentage earned: '))
    l.append(raw_input('Enter total peer percentage points earned: '))

def calculateGrade(l):
    hw_weight = .3
    lab_weight = .3
    project_weight = .2
    quizzes_weight = .1
    peer_weight = .1

    final_score = int(l[0])*hw_weight + int(l[1])*lab_weight + \
    int(l[2])*project_weight + int(l[3])*quizzes_weight + \
    int(l[4])*peer_weight

    return final_score

def main():
    l = []
    totalPoints(l)
    print calculateGrade(l)

main()
