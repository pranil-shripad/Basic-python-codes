#Average of list
lst = [1,2,3,4,5,6,7,8,9,10]
avg = 0
print(len(lst))

for i in range(len(lst)+1):
    avg += i/len(lst)
    
print(avg)