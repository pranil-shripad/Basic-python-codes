data = {"s1":95, "s2":68, "s3":86, "s4":52, "s5":65, "s6":98, "s7":28, "s8":45, "s9":79, "s10":84 }
avg = 0
for i in data.values():
    avg = avg+i/10
print("The average marks of students is: {}".format(avg))