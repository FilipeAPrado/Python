from enum import Enum
import os 
class Situation(Enum):
    Approved = "Student is approved."
    Verification = "Student Approved under verification."
    Reproved = "Student is disapproved "

def studentIsApproved(note):
    situations={
        note == 6 or note > 6 : Situation.Approved,
        note >4 and note < 6 : Situation.Verification,
        note < 4 or note == 4 : Situation.Reproved
        }
        
    return situations[True]

def tryForInt(value):
    try:
        return int(value)
                
    except:
        print("Informed value is not accepted.")
        os._exit(0)
        pass
      
def noteStudent():
    noteAv1 = tryForInt(input("What grade of student in AV1"))
    noteAv2 = tryForInt(input("What grade of student in AV2"))
    return (noteAv1 + noteAv2)/2

result = noteStudent()
print(studentIsApproved(result).value)

    