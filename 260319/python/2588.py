a = int(input())
b = int(input())

step1 = a * (b % 10)         
step2 = a * ((b // 10) % 10) 
step3 = a * (b // 100)        
final = a * b               

print(step1)
print(step2)
print(step3)
print(final)
