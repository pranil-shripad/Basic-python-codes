s = input("Enter a sentence: ")

result = s.split(" ")
fresult = ' '.join(result[::-1])   
print(fresult)
