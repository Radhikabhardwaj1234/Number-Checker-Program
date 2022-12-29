
a=int(input("Enter the upper value of range(A)= "))
b=int(input("Enter the lower value of range(B)= "))
count=0
count1=0
count2=0
for num in range(a,b+1):
    if (num==1) or (num==0) or (num<0):
        print(num," is not a prime and not composite number")
        count2+=1


    if num>1:
        for i in range(2,num):
            if (num%i==0):
                print(num,"is a composite number")
                count1+=1
                break

        else:
            print(num,"is a prime number")
            count+=1
print("Total prime numbers = ",count)
print("Total composite numbers = ",count1)
print("Number of neither compisite nor prime numbers = ",count2)