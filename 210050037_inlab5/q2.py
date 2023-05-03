# Running your solution - You can run this script in console with the command given in the next line
# python q2.py 10
# Here 10 is the input provided by the user. Hence the output should be the list of prime numbers less than or equal to 10. Your console output shpuld be:
# List of primes = [2,3,5,7]

########################################## Script starts here ########################################
import argparse
from re import L 
import matplotlib.pyplot as plt
# This python module can be used for getting the input provided by user
def div(x,y):
   if(x!=y and x%y==0):
      return False
   else:
      return True

def n_filter(i,l,num):
   if(i == num):
      print(l)
      x=l
      y=l
      plt.scatter(x,y)
      plt.show()
      return l
   l=list(filter(lambda x : div(x,i),l))
   n_filter(i+1,l,num)
 
def get_primes(num):
   # Should take an integer as input and reutrn a list of primes less than or equal to the given input
   l1=list(range(1,num+1))
   l2=n_filter(2,l1,num)
   return l2
# the variable num should be declared before the main() function as a global variable
parser = argparse.ArgumentParser()
parser.add_argument('num', type=int)
args = parser.parse_args()
if __name__ == '__main__':
    # Edit this part of the code in order to pass the argument to get_primes() function
    # num is the argument you got from command line using argparse module
    get_primes(args.num)
    
    
