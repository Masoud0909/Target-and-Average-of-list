#Create a list containing the following integers L = [9,6,-8,4,6,23,9,6]. Write a python program that:
#a.	Reads a target and find how many times it is present in the list
#b.	Calculates the average of the elements

L = [9,6,-8,4,6,23,9,6]
i = 0
n =len(L)
count =0
target= input("Enter your target in the list: ")
sum=0
while i<n:
    if(L[i]== float (target)):
        count=count+1
    sum=sum+L[i]
    i=i+1
print ("the target is found ",count ,"times")
average = sum/n
print ("the average is : " , float(average))
