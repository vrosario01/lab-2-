# lab-2-
# Lab-2
In this lab, we'll build more sophisticated functions using our new skills of conditions, recursion, currying, lambdas, and while statements.  (In case this list causes you concern, it is likely that you may not actually use all of them for this lab!)

# Directions for submission
Create a github repo called "Lab-2." Invite me as a collaborator to your repo.  Download the repo files here as a zip file.  Unzip the files and add them to your repo.  Modify the files as appropriate according to the instructions.  Do not change names.  Commit and push changes to your repo.

# Directions for solutions
Do not change any of the code given to you (other than the comments which should absolutely be removed).  I will run your code with the expected structure.  You are welcome to add any additional lines of code or functions you find necessary.  If you make changes in which your solutions do not run, you will receive no credit for that problem.  All solutions should include a docstring description.  **For this lab, I also ask that you include doctests, described below.**  Unless otherwise specified, all functions should end with a return of the appropriate type and not a print statement.

# Instructions for doctests
A docstring is a way of recording a function's purpose as well as any necessary details about expected inputs and outputs which a person using your code would need to know.  A doctest also provides additional information, giving a collection of test values which demonstrate the expected behavior of the function.  A doctest is written as a sequence of interactions in an interactive session of Python.  A good programmer should always think about a collection of cases which fully exhibit the range of input/output behaviors.  For example, in the abs function, our full docstring, including doctests might look like:\
"""\
number -> positive number \
\
abs takes in a number and returns the corresponding positive number \
\
\>>>abs(3) \
3 \
\>>>abs(-3) \
3 \
\>>>abs(0) \
0 \
"""\
The formatting here is important.  The function calls should come after the >>> which you would see in an interactive terminal.  The returns should be included without >>> preceding it.  Formatted in this way, you can check your own code using the testmod function from the doctest module.

# Problem 1
Define a function called pythagorean_triples which takes three parameters a,b,c and returns True if a^2+b^2=c^2 and False otherwise.  Make sure that you are returning the boolean values True and False and not the strings "True" and "False".

# Problem 2
Define a function called is_triangle which takes three numbers a,b,c as input and returns True if these numbers can be the side lengths of a triangle and False otherwise.  You can look up the triangle inequality to assist with the domain knowledge of this question.

# Problem 3
Define a function called print_range which will take as input three integers called start, stop, and step and will print all of the numbers starting at start and stopping at stop, where stop is not included, that are separated by step.  To simplify matters, assume that stop is greater or equal to step.  You are not permitted to use any functions not covered in class for this problem.

# Problem 4
Belle will only wear a jacket outside if it is below 60 degrees or it is raining.  Define a function called wears_jacket which takes in a number named temp and a boolean value named raining and returns True if she wears a jacket.

# Problem 5
Design a function, using recursion, which counts the number of trailing 0's of a given number.  For example, 300 returns 2 for the two zeros at the end of the number.  As a follow-up, design a function which computes the number of trailing zeros in n! for any integer n.

# Problem 6
Design a function which adds two numbers without using +, add or any arithmetic operators.  You can, however, use the successor function we used in class.

# Problem 7
Design a function sum_id which takes in a positive number n and returns the sum from 1 to n: 1+2+3+...+n.  Design a function sum_squares which takes in a positive number n and returns the sum of the square of the numbers from 1 to n: 1^2+2^2+3^2+...+n^2.  Design a function sum which takes in a positive number n and a function f and sums the values of the function applied to the numbers from 1 to n: f(1)+f(2)+f(3)+...+f(n).  Design a function product which takes in a positive number n and a function f and does exactly the same functionality of the sum function except instead of adding, we multiply terms.  Define a function to generalize your previous two functions, combine_sequence, which takes in a number n and two functions, one called combine and one called f, where f is the function as before and combine now controls the manner in which terms are combined.  If not otherwise specified, combine_sequence should default to summing the values of the function applied to the numbers from 1 to n.
