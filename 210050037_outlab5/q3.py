from exception import Lab5Exception
def dupcheck(x):
   for elem in x:
      if x.count(elem) > 1:
         return True
      return False

def set_union(collection_one, collection_two):
    """
        This function, as the name implies, should output 
        the result of union of two sets. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    l1=list(collection_one)
    l2=list(collection_two)
    if(dupcheck(l1)==True):
        raise Lab5Exception("Not a valid set(l1)")
    if(dupcheck(l2)==True):
        raise Lab5Exception("Not a valid set(l2)")
    for element in l2:
      if element not in l1:
          l1.append(element)
    return l1

def set_intersection(collection_one, collection_two):
    """
        This function, as the name implies, should output 
        the result of intersection of two sets. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    l1=list(collection_one)
    l2=list(collection_two)
    if(dupcheck(l1)==True):
        raise Lab5Exception("Not a valid set(l1)")
    if(dupcheck(l2)==True):
        raise Lab5Exception("Not a valid set(l2)")
    l = [value for value in l1 if value in l2]
    return l

def set_equality(collection_one, collection_two):
    """
        This function, as the name implies, should check whether
        or not two sets are equal. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly. 
    """
    l1=list(collection_one)
    l2=list(collection_two)
    if(dupcheck(l1)==True):
        raise Lab5Exception("Not a valid set(l1)")
    if(dupcheck(l2)==True):
        raise Lab5Exception("Not a valid set(l2)")
    if(l1==l2):
        return True
    else:
        return False

def parse_file(file_name):
    """
        This function is expected to parse a text (.txt) file
        and extract pairs of collections from it.

        Note that the parsed collections might not be valid sets.
        Please check and accordingly raise Exception. You should also
        think about other corner cases of your code and raise the Exception
        accordingly.
    """
    f = open(file_name, "r")
    for x in f:
       print(x)
    return
