import pandas as pd
import numpy as np
def read_data(file_name):
    r"""
        This function reads the contents from the file,
        specified by the file_name into a pandas DataFrame.
    """
    df = pd.read_csv (file_name)
    return df

def compute_avg(data_frame):
    r"""
        This function takes in a DataFrame and returns another 
        DataFrame with the computed averages
    """
    pass
    cgpa_b=0
    num_b=0
    cgpa_m=0
    num_m=0
    cgpa_p=0
    num_p=0
    for index, row in data_frame.iterrows():
        if (row['programme']=='MS'):
            cgpa_m=cgpa_m+row['cgpa']
            num_m=num_m+1
        if (row['programme']=='BTech'):
            cgpa_b=cgpa_b+row['cgpa']
            num_b=num_b+1
        if (row['programme']=='PhD'):
            cgpa_p=cgpa_p+row['cgpa']
            num_p=num_p+1
    cgpa_b=cgpa_b/num_b
    cgpa_m=cgpa_m/num_m
    cgpa_p=cgpa_p/num_p
    data={
        "cgpa":[0,cgpa_b,cgpa_m,cgpa_p]
    }
    df = pd.DataFrame(data,index=["programme","Btech","MS","PhD"])
    return data_frame.groupby(["programme"]).mean(numeric_only = True)
    

if __name__ == '__main__':
    df = read_data('example_input.csv')
    print('\n=============INPUT DF=============\n')
    print(df)
    print('\n=============EXPECTED OUTPUT=============\n')
    print(compute_avg(df))
