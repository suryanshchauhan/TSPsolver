# TSPsolver

<h3>Description:</h3>
The Traveling Salesman problem (TSP) is a famous problem in Computer Science, both because it is a very hard problem to solve (one of a class called NP-complete), and because there are many approximation algorithms to find a decent solution to it. TSP can be quickly summarized by assuming that there are N cities, with a cost of travel from every city to every other city defined. TSP asks us to find the lowest cost path from a given city back to that city that passes through every other city once and only once.
One way of obtaining a solution to a TSP problem is to use a genetic algorithm. I have implemented a genetic algorithm to find a solution to TSP problems.


<h3>The Program:</h3>
When the program is run, it does the following:
<li> Prompts the user to enter a file name. </li>
<li> Opens the file and read in the information about the TSP. If the file doesn’t exist, it prints an appropriate error message and exits the program. If it does, it prints the information from the file (the list of names and grid of costs). </li> 
<li> Runs a genetic algorithm to find the best path for the TSP. While running, the program prints the cost of the best tour it has found during each generation.</li>
<li> When the program is finished, it prints the best path found, and the resulting path cost. </li>

<h3>File Format:</h3>
<li> The first line of the file is an integer N. This number is the number of cities in the problem.</li>
<li> The next N lines will each contain one string, representing the name of the city. You can assume that this name will contain no spaces. The name on the i-th line is the name of the i- th city. </li>
<li> The next N lines will each contain N integers. This will create an N x N grid which gives the costs to travel between cities. In particular, the number in the j-th column of the i-th row is the cost to travel from city i to city j. You cannot assume that the cost from i to j will be the same as the cost from j to i. The element in the i-th row and i-th column should be 0. </li>
