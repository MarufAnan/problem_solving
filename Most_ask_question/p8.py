# Finding the Maximum Number in a List

def MaxNumInList(n):
    maxNum=n[0]
    for num in n:
        if num>maxNum:
            maxNum = num
            
    return maxNum

# Finding the Minimum Number in a List

def MinNumInList(n):
    minNum=n[0]
    for num in n:
        if num<minNum:
            minNum = num
            
    return minNum

# Finding the Middle Element in a List

def MidNumInList(n):
    
    return n[int(len(n)/2)]

#main function

numberList= list(map(int,input("Enter the numbers with space:").split()))

print("the max number in list"+MaxNumInList(numberList))

print("the Min number in list"+MinNumInList(numberList))

print("the Middle number in list"+MidNumInList(numberList))