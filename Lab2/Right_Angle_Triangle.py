#Aim = Take the number of rows as input and print a right-angle triangle pattern using stars
#Logic = Take the number of rows as input and use a for loop to increase the number of stars by one in each row.

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print("* " * i)

# output to be recived for sample i =5
#*
#**
#***
#****
#*****