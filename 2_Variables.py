'''
IDENTIFIER
Any name given by the programmer to variable, function, class or method is called an identifier. 
Its not a py terminology. Actually it is a general programming term.
An identifier can be 
    - Variable Name 
    - Function Name 
    - Parameter Name 
    - Method Name 
    - Class Name 
'''

'''
Rules for Python Identifiers 
1. Identifers should have only 
    Alphabets ( Lower and Upper )
    Digits ( 0 to 9 )
    Underscore ( _ )
    or combination of all. 
Below are some of the examples. 
'''

name = 'Micheal'
EmployeeName = "obama"
dob2Age = '24-Nov-1900'
USA2Europe_TripFare = '900005'
manager_name = "Amstrong"
_manager_name = 'Boycott'

# RULE 02 : identifiers shouldn't start with number.

Total2 = 44
2Total == 44  # Wrong


# RULE 03 : Identifiers shouldn't have any special symbols ~!@#$%^&*(). Only underscores are allowed.

employeee@Name = 'Aswin'  # Wrong
employee$Name = 'Aswin'  # Wrong
employee_name = 'Aswin'  # Correct
