#wrt py script for finding Permutation of a over n , r are user defined 
#wrt py script for finding Combination of a over n , r are user defined 

n=int(input("enter number N:"))
r=int(input("enter number R:"))

fact_n =1
for i in range (1,n+1):
    fact_n=fact_n*i
fact_nr =1
for j in range (1,n-r+1):
    fact_nr=fact_nr*j
fact_r=1
for k in range(1,r+1):
    fact_r=fact_r*k

denom= fact_nr*fact_r
ncr=fact_n/denom

print("Combination",ncr)
#if(r>n):
 #   print("Invalid")
#else:
 #   result=1

  #  for i in range(r):
   #     result*=n-i

#    print("Permutation",result)