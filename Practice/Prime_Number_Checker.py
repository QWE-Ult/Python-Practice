n=int(input("Enter the number"))

prime=True
for i in range(2,n):
    if n%i==0:
        prime = False
    break 
print(prime)

# def a (n):
    
#     if n <= 1:
#         print("Not Prime")
#         return
    
#     is_Prime=True
    
#     for i in range(2,n):
        
#         if n%i==0:
#             is_Prime=False
#             break
#     if is_Prime:
#         print("Prime")
#     else:
#         print("Not")
        
# a(1)


# def print_primes(start, end):

#     for num in range(start, end + 1):

#         if num <= 1:
#             continue

#         is_prime = True

#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             print(num)

# print_primes(10, 30)