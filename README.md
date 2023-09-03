# Spread Points in Unit Circle
Spread K points with maximum possible distance in a unit circle using Evolutionary Strategy.

### Requirements
see [requirements.txt](https://github.com/mohammadAbbasniya/EvolutionStrategy_PointsInCircle/blob/main/requirements.txt) and use `pip install -r requirements.txt` for installation.
1. `numpy` for some calculations
2. `matplotlib` for ploting the final result
<br><br>



## About the problem
We want to place k points in a unit circle (A circle with a radius of 1) so that the minimum distance between any two points is maximized. That is to say, we want to <ins>maximize</ins> the following term:&nbsp; $\forall i,j ∶ MIN \lbrace distance ({\rm point}_i\ ,\ {\rm point}_j) \rbrace$ &nbsp;. In other words, we want to maximize the minimum distance between any two points. Some example solutions are seen in the figure below.
<p align='center'>
  <img alt="best-solutions" width="600" src="https://github.com/mohammadAbbasniya/EvolutionStrategy_PointsInCircle/blob/main/README.imgs/bests.png">
</p> 

The program will take the number of points as input and find the best position for each point using **Evolutionary Strategy**. The representation must be a list of points in polar coordinates We always consider the first point to be placed at the fixed position $(r:1\text{, }\theta:0)$. <br><br>



## About Evolutionary Strategy
In computer science, an evolution strategy (ES) is an optimization technique based on ideas of evolution. It belongs to the general class of evolutionary computation or artificial evolution methodologies. Evolution strategies use natural problem-dependent representations, so problem space and search space are identical. In common with evolutionary algorithms, the operators are applied in a loop. An iteration of the loop is called a generation. The sequence of generations is continued until a termination criterion is met [[Wiki](https://en.wikipedia.org/wiki/Evolution_strategy)]. In each generation new individuals (offspring) are created using **Recombination** or **Mutation**.
<p align='center'>
  <img alt="ES-flow" width="600" src="https://github.com/mohammadAbbasniya/EvolutionStrategy_PointsInCircle/blob/main/README.imgs/ES-flow.png">
</p>
<br><br>



## Project structure 
- ### 📄 [main.py]
  A simple driver code that employes implemented classes and saves the output as an image in `/outputs` directory.
  
- ### 📂 directory [k_points_in_circle]
  - #### 📄 [point.py]
    This file contains a class `Point` as representation of a Polar Point.
    
  - #### 📄 [solution.py]
    This file contains a class `Solution` as the representation of a solution to the problem. Each solution object contains K `Point` objects and the fitness of the solution is determined by the minimum distance between any points (the higher the value of fitness, the better the solution). 
    
  - #### 📄 [evolution_strategy.py]
    This file contains a class `NPointsES` which is the heart of the evolutionary strategy employed to solve this problem. The object of this class has a method `run` that starts with random solutions and iterates `max_iterations` times, in every iteration new solutions are created using recombination, mutation and a fixed number of best solutions in the previous generation.


- ### 📂 directory [outputs]
  directory to store the image result of execution.
<table align='center'>
  <tr style='background-color: green;'>
    <td> <img alt="solution-4" width="300" src="https://github.com/mohammadAbbasniya/EvolutionStrategy_PointsInCircle/blob/main/outputs/solution-4.png"> </td>
    <td> <img alt="solution-5" width="300" src="https://github.com/mohammadAbbasniya/EvolutionStrategy_PointsInCircle/blob/main/outputs/solution-5.png"> </td>
  </tr>
  <tr style='background-color: white;'>
    <td> <img alt="solution-6" width="300" src="https://github.com/mohammadAbbasniya/EvolutionStrategy_PointsInCircle/blob/main/outputs/solution-6.png"> </td>
    <td> <img alt="solution-7" width="300" src="https://github.com/mohammadAbbasniya/EvolutionStrategy_PointsInCircle/blob/main/outputs/solution-7.png"> </td>
  </tr>
</table>

