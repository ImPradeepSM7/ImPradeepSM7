'''
Almost every programming language has a concept called loop,
which helps in running a single block of code a number of times.
In programming, we often have to execute the statements more than once,
in which case a loop can be used.


Loops come in extremely handy in situations such as iterating through data structures
or traversing through large data sets in order to filter out junk data.

When using a loop within a program, you can write one set of instructions
that operates on multiple data sets.

This involves repeating a group of instructions of a program either a specified number of times
or until some logical condition is satisfied.

Most of the times, we know the number of times the loop has to be repeated,
while sometimes, it’s unknown and the loop is repeated until the condition is true.

For and While are the general loop control statements used in C programming,
along with Do-While loop.

We look at the two entry-controlled loops in detail to understand the difference between the two.


What is For Loop?
A for loop is an entry control statement used for the repeated execution of certain statements
along with the repeated testing for a definite value of expression to be either true or false.

The for loop is used for definite loops when the number of iterations are known.
Definite loops are those that will loop a specific number of times.

For loops are used only to make the code slightly shorter,
but also make it easier for other programmers to read.

It seems appropriate when the initialization and increment are logically related and are single statements.

The for statement uses a loop control variable,
providing you with three actions automatically in one compact statement:
Initialization, Evaluation and Incrementation.



What is While Loop?
Unlike for loop, while loop is used for indefinite loops where the number of iterations is not known.
This means the loop will continue to execute infinite number of times until and unless the condition is satisfied.
It is the simplest loop control statement used in programming to execute indefinite loops.

It executes a target statement repeatedly as long as the given condition is true.
It is the most basic loop in programming with only one control condition
which executes as long as the condition is met.

As soon as the condition becomes false, it stops the execution of the loop and passes
the control to the statement immediately following the while loop.
It is appropriate as you do not know exactly how many times the user wants to repeat the loop.



Difference between For and While Loop
Basics
– While both for and while are entry-control loops used to execute block(s) of code
repeatedly certain number of times, they differ in functionality.

The for loop is quite similar to the while loop in terms of memory consumption and speed.
However, the for loop is preferable when you know exactly the number of times the loop has to be repeated.
On the contrary, while loop is appropriate when the exact number of iterations is not known,
meaning you do not know how many times the loop has to be repeated.

Syntax
– The syntax for “for loop” is:



                for (Expression 1; Expression 2; Expression 3)

                               {      //statements….

                               }

Here, Expression 1 = Initialization statement;
Expression 2 = Condition for a looping; and
Expression 3 = Update Statement.

The syntax for “while loop” is”

                               while (condition)

                               {     //statement(s)…

                               }

Here, statement can be a single or a block of statements.
The loop will continue to execute until the condition is true and will terminate once the condition is false.

Use
– The for loop is used when a user wants to do something for a specific number of times.
It is an entry control statement used for the repeated execution of certain statements.
This is preferable when we know exactly how many times the loop will be repeated in advance.

The while loop, on the other hand, is used for indefinite loops,
meaning we do not have any idea on exactly how many times the loop is going to be repeated.
The while loop will continue to run infinite number of times until the condition is met.

Condition
– A for loop has a counter variable which enables the developer to specify the number of times
the loop will be executed.
In for loops can have their counter variables declared in the declaration itself.

On the contrary, there is no built-in loop control variable with a while loop.
Instead, you can specify any condition that evaluates to either a True or a False value.

If the condition is not specified for a for loop, then the loop iterates infinite number of times,
while in case of while loop, it shows a compilation error.



For vs. While Loop: Comparison Chart





Summary of For vs. While Loop
While both the entry control loops are quite similar and they serve basically the same purpose,
the anatomy of a for loop is slightly different than a while loop.
A while loop has no built-in loop control variable as there is with the for loop;
instead, an expression needs to be specified similar to a test expression specified in a for loop.

However, with a while loop, the expression is specified to evaluate the condition to a True or False value.
Unlike for loop, while loop is used when we do not have any idea about how many times the loop will be executed.



Read more: Difference Between For and While Loop | Difference Between http://www.differencebetween.net/technology/difference-between-for-and-while-loop/#ixzz7H1eLuSnQ


'''