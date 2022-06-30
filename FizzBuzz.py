
var = []

for i in range (1,100):		        #for loop for incrementing number to 100
    FIZZ = False
    BUZZ = False

    if i%3 == 0:                    #if i is divisible by 3, FIZZ
        FIZZ = True         
    if i%5 == 0:                    #if i is divisible by 5, BUZZ
        BUZZ = True

    if not FIZZ:
        if not BUZZ:
            var.append(i)           #print original number if not divisible by 3 or 5
        else:
            var.append("BUZZ")
    else:
        if not BUZZ:
            var.append("FIZZ")
        else:
            var.append("FIZZBUZZ")  #print FIZZBUZZ if divisible by both 3 and 5
        
print(var)