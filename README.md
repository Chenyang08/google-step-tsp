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
  
  IDEA:
  
  | Challenge | Number of cities(N) | Total Distance |
 |:---------: |    :----------:     |  :----------:  |
 |      0     |         5           |    **3291.62**     |
 | 1|8|**3778.72**|
 |2 | 16 | **4494.42**|
 |3|64 |8303.81|
 |4|128|11261.35|
 
  
  
----
### Solver:  [2Opt_greedy.py](https://github.com/Chenyang08/google-step-tsp/blob/master/2Opt_greedy.py "") 
  IDEA: 
 
 | Challenge | Number of cities(N) | Total Distance |
 |:---------: |    :----------:     |  :----------:  |
 |      0     |         5           |    3418.10     |
 | 1|8|3832.29|
 |2 | 16 | **4494.42**|
 |3|64 |8290.23|
 |4 | 128 |**11120.04**|
 |5 | 512|**21701.12**|
 |6 | 2048|46883.97|
-----
