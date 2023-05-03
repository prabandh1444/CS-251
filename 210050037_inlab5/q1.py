import json
from student import Student
from exception import Lab5Exception
lp=[]
def check(t):
         for i in lp:
           if t==i:
            return False
         lp.append(t)
         print(lp)
         return True 
class StudentBuilder:
    r"""
        You are expected to define a static method
        by the name build_student_object. It should take in 
        path to a json file and read the contents of the file.

        You are also expected to validate the contents read from 
        the JSON file and raise Exception accordingly
    """
    def build_student_object(json_file_path):
        f=open(json_file_path)
        your_json = json.load(f)
        s = Student(**your_json)
        if s.name=='':
            raise Lab5Exception('Your name is  registered as EMpty')
        if s.home_town=='':
            raise Lab5Exception('Empty Hometown registered')
        if s.age>35 or s.age<0:
            raise Lab5Exception("Invalid Age for a Student")
        if s.cgpa<0 or s.cgpa>10:
            raise Lab5Exception("LOL,How did u get that kind of cgpa")
        g1='Male'
        g2='Female'
        g3='Non-Binary'
        g4='Prefer Not To Say'
        if not(s.gender == g1 or s.gender == g2 or s.gender == g3 or s.gender == g4):
            raise Lab5Exception("Thats not a gender in our database")
        if(check(json_file_path)==False):
            raise Lab5Exception("Already exists")
        return s
   
    