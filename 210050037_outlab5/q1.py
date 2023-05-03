##############################################
"""
Extra functions or variables if required

"""
##############################################
from exception import Lab5Exception

def rotate(arr):

    rotated_array = []

    """
    This function takes a list of lists as input and returns the rotated verion 
    (rotated 90 degrees anti-clockwise)

    Input arguments:
    arr : List of lists

    Returns: rotated_array

    """
    rows=len(arr)
    for i in range(0,len(arr)):
     cols=len(arr[i])
     if(rows!=cols):
        raise Lab5Exception("Not a Square Matrix")
################################### Add your code here ###################################

##########################################################################################
    for i in range(0,len(arr)):
        l=[]
        for j in range(0,len(arr)):
            l.append(arr[j][len(arr)-i-1])
        rotated_array.append(l)
    return rotated_array


# Use the main() function only for testing your code

if __name__ == "__main__":
    
    """
    Main function

    Example call:
    You can use the following matrix "test_arr" for testing your solution.
    For running the code, use the command "python q1.py" 
    
    test_arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotated_array = rotate(test_arr)
    print(rotated_array)

    Console output should be: [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]

    """
    

   