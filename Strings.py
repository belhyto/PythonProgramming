#String functions
str1= "Hello"
str2=" World"
str3="P"
l1=["a","b","c"]
l1[1]= "d"
l2=["s","r","t"]
print(l1)
t1=("1")
print("Len:", len(l1))
#print("Merge:", )
#WAP in python to find the sum of all the integers values of a list using functions.

l3=[3,4,6,8]
def sumfunc(l3):
    sum=0
    for x in l3:
        sum=sum+x

    return(sum)
print("sum of the elements in the list:", sumfunc(l3))

n=str1.find("o")
print("Positon of 'o': ", n)
print("isDigit: ", str1.isdigit())

str4="150"
x=str4.isdigit()
print(x) 
  
if(x=="True"): 
    print("It is a digit")
else : 
    print("It is not a digit")

num2= 150
temp=num2
while temp>0:
    digit=temp%10
    sum += digit ** 3
    temp //= 10
if num2==sum :
    print("It is an armstrong number")
else :
    print("It is not an armstrong number")
 



