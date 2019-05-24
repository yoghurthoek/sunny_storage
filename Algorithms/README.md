# Algorithms

In this folder are the scripts of the algorithms we implemented for every part of the assignment.

1. Connecting the houses with batteries:
    * **averagefit:** this algorithm fills batteries by getting a house with the highest and lowest output and putting them together in a battery
    * **decreasingfirstfit:** this algorithm fills batteries by getting houses from a sorted list (high to low capacity) and starts with houses with the highest capacity.


2. Calculate the total costs of the neighborhood and try to optimize:
    * **bfs:** this algorithm creates a queue with all possible configurations. It is an exhaustive algorithm and uses a lot of memory.
        * Since this algorithm uses so much memory, it can only be runned with neighborhood 4
    * **branchnbound:** this algorithm creates a stack with all possible configurations. It is also an exhaustive algorithm with a (very) long runtime. We tried to prune the stack, making it a branch 'n bound algorithm.
        * Since the runningtime is still long, it can only be runned with neighborhood 4
    * **greedy:** this algorithm chooses randomly a house and connects it to a battery based on best (shortest) distance.
    * **hillclimber:** this algorithm starts with a greedy or random base and tries to find a better solution by  switching houses.
    * **randclimber:** this algorithm connects houses and batteries randomly and tries to optimize by switching houses.
    * **random:** this algorithm connects houses and batteries randomly


3. Optimization of the total costs by moving the batteries:
    * **battery_optimization:** this algorithm moves the location of the batteries after connections with houses have been established. It garantees that the sum of the manhatandistance of a battery to all the connected houses is minimalized.


4. Optimization of the total costs by moving and using other batteries:
    * **KmeansClusterdistance:** this algorithm takes the desired amount of clusters between 5 and 17 as input. The capacity of available batteries and the maximal output of the houses on the grid makes the minimum amount of clusters necessary 5. More then 17 clusters will very likely, not give a better solution then one with less clusters. The algorithm returns a grid with the desired amount of clusters on (local) optimal positions.   
