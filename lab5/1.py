N=int(input("Enter a number: "))
odd_sum=0
even_sum=0
even_count=0
for i in range(1,N+1):
    if i%2!=0:
        odd_sum=odd_sum+i
    elif i%2==0:
        even_sum=even_sum+i
        even_count+=1
even_average=even_sum/even_count
print("Sum of odd numbers:", odd_sum, "Average of even numbers:", even_average)
