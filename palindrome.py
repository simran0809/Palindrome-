n=int(input("Enter number:")) 
temp=n 
rev=0 
while(n>0):
   dig=  n%10 
   rev=rev*10+dig # as me get one digit of palindrome then 7 step 
   n=n//10 
if(temp==rev): #check the rev palindrome we get 
 print("The number is a palindrome!") 
else:
 print("The number isn't a palindrome!") 
 
 
 #palindrome  
