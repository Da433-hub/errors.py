# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# This program is now free from errors following corrections, giving the error types and reasons.

print("Welcome to the error program")
print("\n")  # syntax error; unexpected indentation; needed brackets

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = 24  # SyntaxError; Unexpected indentation. # Runtime error; Parentheses and words must be removed as strings cannot be used in calculations.
age = age_Str  # SyntaxError; Unexpected indentation. # Runtime error; casting age_str to an integer would disable string concatenation (24).
print("I'm" + " " + str(age) + " " + "years old.")  # SyntaxError; Unexpected indentation. # Runtime error; concatenation of str and int; add 2 spaces +" "+

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5  # SyntaxError; unexpected indentation. # Logical error; '3.5' not '3' years. # Runtime error: String (" ") cannot be added.  Keep as an integer.
total_years = age + years_from_now  # SyntaxError; Unexpected indentation.
print("The total number of years: " + str(total_years))  # SyntaxError; add brackets; # Runtime error; "answer_years" should be "total_years" and should be cast to str.to allow concatenation.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # Runtime error; total should be total_years.
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")  # SyntaxError; Add brackets. # Runtime error; Cast to str.'total_months'.

# HINT, 330 months is the correct answer

