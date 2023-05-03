#######################################

"""
Import any libraries if required
Extra functions or variables if required

"""
#######################################
def weirdProblem(L):
    
    converted_string = ""

    """
    This function takes a list of lists as input and returns a string which is a
    concatenation of elements 
    Input arguments:
    L : List of lists

    Returns: converted_string
	string

    """
################################### Add your code here ###################################

##########################################################################################
    while True:
        x=0
        for i in range(0,len(L)):
            if(L[i]!=[]):
                if converted_string!="":
                    converted_string=converted_string+" "+L[i][0]
                else:
                    converted_string=converted_string+L[i][0]
                L[i].pop(0)
            if(L[i]==[]):
                x=x+1
        if(x==len(L)):
            break
    return converted_string


if __name__ == "__main__":

    """
    Main function

    Example call:
    You can use the following list of lists "L" for testing your solution.
    For running the code, use the command "python q2.py" 
    
    L = [ ["this", "programming", "is"], ["is", "assignment", "kinda"], ["a", "which", "weird"]  ]
    converted_string = weirdProblem(L)
    print(converted_string)

    Console output should be: this is a programming assignment which is kinda weird

    """
    L = [ ["this", "programming"], ["is", "assignment", "is"], ["a", "which","kinda", "weird"]  ]
    converted_string = weirdProblem(L)
    print(converted_string)
