def main():
    names = []
    toggle = True
    while toggle == True:
        N = input("Input a Name: ").lower()
        names.append(N)
        toggle = repeat() 
    insertionSortNames(names)
    search = input("What name would you like to look for? ")
    goal = find(names, search)
    if goal == True:
        print("That name is in the list")
    else:
        print("That name has not been registered")

def find(nameList, target):
    first = 0
    last = len(nameList)-1
    found = False

    while first<=last and not found:
         midpoint = (first + last)//2
         if nameList[midpoint] == target:
             found = True
         else:
             if target < nameList[midpoint]:
                 last = midpoint-1
             else:
                 first = midpoint+1

    return found


def insertionSortNames(N):
    for i in range(1,len(N)):
        key=N[i]
        j=i-1
        while j>=0 and key<N[j]:
            N[j+1]=N[j]
            j=j-1
        N[j+1]=key
    return N

def repeat():
    while True:
        repeat = input("Do you want to enter another name? Y = Yes N = No : ").upper()
        if repeat == "Y":
            return True
        elif repeat == "N":
            return False 
        else:
            print("Invalid Input")

main()