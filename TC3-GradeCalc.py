# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    Plus = 0.3
    Minus = (-0.3)
    A = 4
    B = 3
    C = 2
    D = 1
    F = 0


    print("\nGrade Piont Calculator\n")
    print("\nValid letter grades that can be entered: A, B, C, D, F.\n")
    print("\nValid grade modifiers are +, - or nothing.\n")
    print("\nAll letter grades except F can include a + or - symbol.\n")
    print("\nCalculated grade point value cannot exceed 4.0.\n")
    
    Grade = input("Please enter a letter grade: ").upper()
    if Grade == "A":
        G = A
    elif Grade == "B":
        G = B
    elif Grade == "C":
        G = C
    elif Grade == "D":
        G = D
    elif Grade == "F":
        G = F
    else:
        print("\nYou enterned an invalid letter grad.\n")
        Grade = input("Please enter a letter grade: ").upper()
        if Grade == "A":
            G = A
        elif Grade == "B":
            G = B
        elif Grade == "C":
            G = C
        elif Grade == "D":
            G = D
        elif Grade == "F":
            G = F

    Mod = input("\nPlease enter a modifier (+, - or nothering): ")
    if Mod == "-":
        M = Minus
    elif Mod == "+":
        M = Plus
    else:
        M = 0
  
    if G == A and (Mod == "-"):
        Final = A + Minus
    elif G == A and (M == Plus):
        Final = A
    elif G == F and (M == Plus or M == Minus):
        Final = F
    else:
        Final = G + M

    print("\nThe numeric value is: {0:.1f}\n".format(Final))
        

    # YOUR CODE ENDS HERE

main()
