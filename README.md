# TSPsolver

<h3>Description:</h3>
The Traveling Salesman problem (TSP) is a famous problem in Computer Science, both because it is a very hard problem to solve (one of a class called NP-complete), and because there are many approximation algorithms to find a decent solution to it. TSP can be quickly summarized by assuming that there are N cities, with a cost of travel from every city to every other city defined. TSP asks us to find the lowest cost path from a given city back to that city that passes through every other city once and only once.
One way of obtaining a solution to a TSP problem is to use a genetic algorithm. I have implemented a genetic algorithm to find a solution to TSP problems.


<h3>The Program:</h3>
When your program is run, it should do the following:
<li> Prompt the user to enter a file name. </li>
 Open the file and read in the information about the TSP. If the file doesn’t exist, you should
print an appropriate error message and exit the program. If it does, print the information from
the file (the list of names and grid of costs, see below).
 Run a genetic algorithm to find the best path for the TSP. While running, your program
should print the cost of the best tour it has found during each generation.
 When your program is finished, print the best path found, and the resulting path cost.
You are free to store the TSP information any way you like, and to set up the genetic algorithm any way you like. It must be a genetic algorithm, though – using a population of candidate solutions, performing selection, cross-over, and mutation, etc. But the parameters and set-up are totally open. Your algorithm may not find the best solution (in fact, for larger problems it almost certainly will not), but it should “make progress” towards a solution.
