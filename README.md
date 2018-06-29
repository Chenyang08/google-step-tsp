Travelling Salesman Problem Challenges
======

Problem Descripton: [This page](https://github.com/Chenyang08/google-step-tsp/blob/master/README_Original.md "")

Result of challenge: [Scoreboard](https://docs.google.com/spreadsheets/d/1Aa_NNQf7sFANuHKt0FTvUBQ83QO3OOKZjifhsmjOxqc/edit#gid=0 "")

Description of solver
---------
### Solver: [cy.py](https://github.com/Chenyang08/google-step-tsp/blob/master/cy.py "")
  
  IDEA: Using dynamics programming but only avaiable for n <= 16
  
 | Challenge | Number of cities(N) | Total Distance |
 |:---------: |    :----------:     |  :----------:  |
 |      0     |         5           |    **3291.62**     |
 | 1|8|**3778.72**|
 |2 | 16 | 4895.46|

----

 ### Solver: [2Opt.py](https://github.com/Chenyang08/google-step-tsp/blob/master/2Opt.py "")
  
  IDEA:<br> 
    In the method of 2opt.py, I used the ordered path which follows the index of the city as initial path, and then 2-opt algorithm was used to optimize the path to find the shortest path. <br> 
   2-opt algorithm basically reverses one random section of the original path to form a new one, and to see if it’s better than the original one.<br> 
    The procedures keep repeating until we find the shortest one. 
The method works well with n <= 64. 

  
  | Challenge | Number of cities(N) | Total Distance |
 |:---------: |    :----------:     |  :----------:  |
 |      0     |         5           |    **3291.62**     |
 | 1|8|**3778.72**|
 |2 | 16 | **4494.42**|
 |3|64 |8303.81|
 |4|128|11261.35|
 
  
  
----
### Solver:  [2Opt_greedy.py](https://github.com/Chenyang08/google-step-tsp/blob/master/2Opt_greedy.py "") 
  IDEA: <br>
  When n gets larger, it gets harder to find the shortest path than other algorithms, so here I optimized the pure 2opt algorithm to the one hybridized with 2-opt and greedy algorithm. <br>
  One of the greedy algorithm, which is also called nearest neighbor heuristic, was used to find the initial path. <br>
  Comparing to the ordered path, this initial path insures that it’s already one relatively short path, and this will increases the possibility the later steps to find the shorter one.<br>
  And then similar to 2opt.py, 2-opt was applied and repeated until it finds the shortest path, This method works well with n = [64, 512]. 
 
 | Challenge | Number of cities(N) | Total Distance |
 |:---------: |    :----------:     |  :----------:  |
 |      0     |         5           |    3418.10     |
 | 1|8|3832.29|
 |2 | 16 | **4494.42**|
 |3|64 |8290.23|
 |4 | 128 |**11120.04**|
 |5 | 512|**21701.12**|
 |6 | 2048|46883.97|]
 
 Comparison: <br>
 Both of the methods can find the relative shorter path within very short time, but since 2-opt and greedy are heuristic, which belongs to local search, we start with some solutions and then make local improvements, it is hard to say it’s the shortest.  <br>
 In order to find a shorter one, some other algorithms should be applied.

-----
