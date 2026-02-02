#find the root of the quaderatic equation
import math

a=float(input("enter coefficient a: "))
b=float(input("enter coefficient b: "))
c=float(input("enter coefficient c: "))

disc= b**2-4*a*c

if disc>0:
    root1=(-b+math.sqrt(disc))/(2*a)
    root2=(-b-math.sqrt(disc))/(2*a)
    print(f"your root 1 :{root1}")
    print(f"your root 2 :{root2}")
elif(disc==0):
    root2=root1=(-b)/(2*a)
    print(f"your root 1 :{root1}")
    print(f"your root 2 :{root2}")
    
else:
    real=(-b)/(2*a)
    imag=math.sqrt(abs(disc))
    print(f"your root 1 :{real}+{imag}i")
    print(f"your root 2 :{real}-{imag}i")
    


