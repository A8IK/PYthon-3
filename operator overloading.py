class Student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
#Here "other.m1" is conenct to m2's m1  and "other.m2" is connect to m1's m2...
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)


        return s3



s1=Student(58,69)
        # m1, m2
s2=Student(60,65)
        #  m1, m2

s3=s1+s2        #   ->Sutdent.__add__(s1,s2)        [This is behind the scene.How that's work]
#if we use it only then it'll get error because fail of operand ...then we have to use "__add method__()"
print(s3.m1)
print(s3.m2)