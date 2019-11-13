print("ISA GPA Calculator")
print("Enter your grade for the class (A,B,C,D,F)")

ISA= []

#ISA curriculum 
ECON3300 = input("Econ 3300: ")
ISA.append(ECON3300)
FIN3100 = input("Fin 3100: ")
ISA.append(FIN3100)
MKTG3100 = input("MKTG 3100: ")
ISA.append(MKTG3100)
MGT3100 = input("MGT 3100: ")
ISA.append(MGT3100)
MGT3200 = input("MGT 3200: ")
ISA.append(MGT3200)
MGT4190 = input("MGT 4190: ")
ISA.append(MGT4190)
IS3100 = input("IS 3100: ")
ISA.append(IS3100)
ISA3010 = input("ISA 3010: ")
ISA.append(ISA3010)
ISA3100 = input("ISA 3100: ")
ISA.append(ISA3100)
ISA3200 = input("ISA 3200: ")
ISA.append(ISA3200)
ISA3210 = input("ISA 3210: ")
ISA.append(ISA3210)
ISA3300 = input("ISA 3300: ")
ISA.append(ISA3300)
ISA4200 = input("ISA 4200: ")
ISA.append(ISA4200)
ISA4220 = input("ISA 4220: ")
ISA.append(ISA4220)
ISA4810 = input("ISA 4810: ")
ISA.append(ISA4810)
ISAEL1 = input("ISA Elective #1: ")
ISA.append(ISAEL1)
ISAEL2 = input("ISA Elective #2: ")
ISA.append(ISAEL2)
BSEL1 = input("Business Elective #1: ")
ISA.append(BSEL1)
BSEL2 = input("Business Elective #2: ")
ISA.append(BSEL2)
Elective = input("Elective: ")
ISA.append(Elective)

print(ISA)



#def calculate():
#
points = 0 
for grade in ISA:
    if grade == "A" or grade == "a":
            points += 4.0
    elif grade == "B" or grade == "b":
            points += 3.0
    elif grade == "C" or grade == "c":
            points += 2.0
    elif grade == "D" or grade == "d":
            points += 1.0
    elif grade == "F" or grade == "f":
            points += 0.0
    if grade.endswith ("+"):
       points = points + 0.3
    if grade.endswith ("-"):
       points = points - 0.3
    gpa = points / 20
    #calculate()
    print ("ISA GPA: ", gpa)