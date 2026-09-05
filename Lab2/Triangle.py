n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
    
# output to be recived for sample i =5
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
