fish-sat
=========
# Getting Started


Hello, and welcome to my Fish-Sat program. To get started, clone the repository to your computer. Once you have cloned, open "cmd" 
(or some equivalent shell). Change directory to the fish-sat repository. Now, to test my program, choose a sample input. I recommend 
starting with input322.csv). "322" means there are 3 variables, 2 expressions, and 2 constraints. Type:
python sat_fish.py ".\\input322.csv"

# Creating Config File
To create your own config file:
1. Create a new csv file

2. Open the csv file in a text editor

3. First line: define the variables in alphabetical order (any order works but alphabetical order is easiest to process)

4. Second line: [number of variables],[number of expressions]

5. Define each expression, the first number is the min value of the expression, the last number is the max value of an expression. In between the first and last number you will define the coefficient of each term in the 2 degree polynomial in the variables provided at line 1. The terms are ordered alhabetically, then by degree. So for variables x, y and z, the order will be: x^2, xy, xz, x, y^2, yx, yz, y, z^2, z, 1 (constant term). The constant term is defined last. For n variables, there will be n + 2 choose n terms in the polynomial. Use the coefficient "0" if the term is not needed. You cannot use the "c" character for a variable. This letter is reserved.


# Sample Output
A sample output is given below. The model number tells you which of the 3 expressions are optimized. There is a "minimization" routine and a maximization routine for each expression (corresponding to the min and max values in the corresponding config file). If you open input322.csv, you will see the first and last numbers of lines 3 and 4 give the min and max for the objective function defined at those lines. The pysmt program applies the given constraints, then finds the minmum and maximum value for the defined objective functions. If the min of the objective function is greater than the first number and the max is less than the last number, the result is "satisfiable". If all the objective functions are satisfiable, then the input is satisfiable, otherwise it is not satisfiable.
```
        Defined Variables from input.txt:
                 x0
                 x1
                 x2
        number of variables: 3
        number of expressions: 2
        Model 0 min satisfiability: 
                Serialization of the formula:
                        ((-0.483 <= ((x0 * x0 * -0.806) + (x0 * x1 * 0.55) + (x0 * x2 * -0.899) + (x0 * 0.761) + (x1 * x1 * -0.269) + (x1 * x2 * 0.084) + (x1 * -0.949) + (x2 * x2 * -0.853) + (x2 * 0.136) + -0.498)) 
                        & (((x0 * 0.429) + (x1 * -0.319) + (x2 * -0.644) + -0.235) < 0.075)
                        & (-0.805 <= ((x0 * 0.429) + (x1 * -0.319) + (x2 * -0.644) + -0.235))
                        & (((x0 * -0.104) + (x1 * -0.009) + (x2 * -0.513) + -0.125) < 0.331)
                        & (-0.062 <= ((x0 * -0.104) + (x1 * -0.009) + (x2 * -0.513) + -0.125)))
                Solution:
                        x0 := 1/8
                        x1 := 0.0
                        x2 := -1/4
        Model 0 max satisfiability:
                Serialization of the formula:
                        ((((x0 * x0 * -0.806) + (x0 * x1 * 0.55) + (x0 * x2 * -0.899) + (x0 * 0.761) + (x1 * x1 * -0.269) + (x1 * x2 * 0.084) + (x1 * -0.949) + (x2 * x2 * -0.853) + (x2 * 0.136) + -0.498) < 0.087)
                        & (((x0 * 0.429) + (x1 * -0.319) + (x2 * -0.644) + -0.235) < 0.075)
                        & (-0.805 <= ((x0 * 0.429) + (x1 * -0.319) + (x2 * -0.644) + -0.235))
                        & (((x0 * -0.104) + (x1 * -0.009) + (x2 * -0.513) + -0.125) < 0.331)
                        & (-0.062 <= ((x0 * -0.104) + (x1 * -0.009) + (x2 * -0.513) + -0.125)))
                Solution:
                        x0 := 1/8
                        x1 := 1/2
                        x2 := -1/2
        Model 1 min satisfiability:
                Serialization of the formula:
                        ((((x0 * 0.429) + (x1 * -0.319) + (x2 * -0.644) + -0.235) < 0.075)
                        & (-0.805 <= ((x0 * 0.429) + (x1 * -0.319) + (x2 * -0.644) + -0.235))
                        & (-0.238 <= ((x0 * x0 * 0.544) + (x0 * x1 * -0.606) + (x0 * x2 * -0.529) + (x0 * 0.87) + (x1 * x1 * 0.815) + (x1 * x2 * 0.96) + (x1 * -0.366) + (x2 * x2 * 0.117) + (x2 * 0.213) + -0.808))
                        & (((x0 * -0.104) + (x1 * -0.009) + (x2 * -0.513) + -0.125) < 0.331)
                        & (-0.062 <= ((x0 * -0.104) + (x1 * -0.009) + (x2 * -0.513) + -0.125)))
                Solution:
                        x0 := 1/8
                        x1 := 3.0
                        x2 := -3/4
        Model 1 max satisfiability:
                Serialization of the formula:
                        ((((x0 * 0.429) + (x1 * -0.319) + (x2 * -0.644) + -0.235) < 0.075)
                        & (-0.805 <= ((x0 * 0.429) + (x1 * -0.319) + (x2 * -0.644) + -0.235))
                        & (((x0 * x0 * 0.544) + (x0 * x1 * -0.606) + (x0 * x2 * -0.529) + (x0 * 0.87) + (x1 * x1 * 0.815) + (x1 * x2 * 0.96) + (x1 * -0.366) + (x2 * x2 * 0.117) + (x2 * 0.213) + -0.808) < 0.545)
                        & (((x0 * -0.104) + (x1 * -0.009) + (x2 * -0.513) + -0.125) < 0.331)
                        & (-0.062 <= ((x0 * -0.104) + (x1 * -0.009) + (x2 * -0.513) + -0.125)))
                Solution:
                        x0 := 1/8
                        x1 := 1/2
                        x2 := -1/2
        Result:
                The problem is satisfiable using the solutions given.
```
