# GPA calculator
import array


####################### Functions #######################


# Function to convert letter grade to number
def gradeToNum(grade):
    match grade.upper():
        case "A":
            return 4.00
        case "A-":
            return 3.67
        case "B+":
            return 3.33   
        case "B":
            return 3.00
        case "B-":
            return 2.67
        case "C+":
            return 2.33
        case "C":
            return 2.00   
        case "C-":
            return 1.67
        case "D+":
            return 1.33
        case "D":
            return 1.00
        case "D-":
            return 0.67
        case _:
            return 0

# # Function to show output
# def showOutput(n, t, c, q, g):
#     print("\nOld GPA: " + "%0.2f" % g)
#     print("Old total credits: " + str(t))
#     gpa = (n + q) / (t + c)
#     print("New GPA: " + "%0.2f" % gpa)
#     print("New total credits: " + str(t + c))

    
##################### End Functions #####################

            
# Get user input
totalCredits = float(input("Enter current total credits taken: "))
oldGPA = float(input("Enter current GPA: "))
currGPA = oldGPA
numerator = totalCredits * currGPA
numClasses = int(input("Enter number of current classes: "))

semCredits = 0
semNumerator = 0
semGPA = 0.0

# Calculate GPA with each new class
for i in range(numClasses):
    credits = int(input("\nEnter class " + str(i+1) + " number of credits: "))
    semCredits += credits
    grade = input("Enter class " + str(i+1) + " letter grade (A, C+, etc.): ")
    qualityPoints = float(gradeToNum(grade)) * float(credits)
    semNumerator += qualityPoints
    #showOutput(numerator, totalCredits, credits, qualityPoints, currGPA)
    numerator += qualityPoints
    totalCredits += credits
    currGPA = numerator / totalCredits
    semGPA = semNumerator / semCredits

# Print final GPA
print("\n----------------------------")
print("\nOld GPA: " + "%0.2f" % oldGPA)
print("Old total credits: " + str(totalCredits - semCredits))
print("\nThis semester credits: " + str(semCredits))
print("This semester GPA: " + "%0.2f" % semGPA)
print("\nNew overall GPA: " + "%0.2f" % currGPA)
print("New total credits: " + str(totalCredits) + "\n")

print("\npress enter to exit")
input()