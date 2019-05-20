# Algorithms

In this folder are the scripts of the algorithms we implemented.


Connecting the houses with batteries:
* **averagefit:** this algorithm fills batteries by getting a house with the highest and lowest output and putting them together in a battery
* **decreasingfirstfit:** this algorithm fills batteries by getting houses from a sorted list (high to low capacity) and starts with houses with the highest capacity.


Calculate the total costs of the neighborhood and try to optimize:
* **bfs:** this algorithm creates a queue with all possible configurations. It is an exhaustive algorithm and uses a lot of memory.
    * Since this algorithm uses so much memory, it can only be runned with neighborhood 4/5
* **branchnbound:** this algorithm creates a stack with all possible configurations. It is also an exhaustive algorithm with a (very) long runtime. We tried to prune the stack, making it a branch 'n bound algorithm.
    * Since the runningtime is still long, it can only be runned with neighborhood 4/5
* **greedy:** text
* **hillclimber:** text
* **randclimber:** text
* **random:** this algorithm connects houses and batteries randomly


Optimization of the total costs by moving the batteries:
* **battery_optimization:** text


Optimization of the total costs by moving and using other batteries:
* **KmeansClusterBatteries**
* **KmeansClusterdistance**
>text over kmean<
