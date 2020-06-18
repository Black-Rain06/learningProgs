


def colorMe():

    cnt = 0
    
    color = input("What is your favorite color?\n\n")
    while cnt != 2:
        color = input("What is your favorite color?\n\n")
        cnt +=1

def colorMe2():

    for i in range(3):
        color = str(input("What is your favorite color?\n\n"))
        print(color.count('e'))

colorMe2()
