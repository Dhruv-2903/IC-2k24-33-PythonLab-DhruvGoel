#Aim = Take the number of rows as input and print a rhombus pattern using stars
#Logic = Take the number of rows as input and use a for loop to print the same number of stars in every row while adding spaces before the stars to create the rhombus shape.

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * n)

# output to be recived for sample i =5
#     * * * * *
#    * * * * *
#   * * * * *
#  * * * * *
# * * * * *