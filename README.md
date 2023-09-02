# Spread Points in Unit Circle
Spread K points with maximum possible distance in a unit circle using Evolutionary Strategy.

### Requirements
1. `numpy` for some calculations
2. `matplotlib` for ploting the final result


## About the problem
Place k points in a unit circle (A circle with the radius of 1) so that the minimum distance between any two points is maximized. That is to say, we want to maximize the following term:
```math
impurity\left(t\right)=1-\sum_{j}\left[p\left(j\middle| t\right)\right]^2
~~~~~~~~~~~
{gain}_{split} = \sum_{i=1}^{k} \frac{n_i}{n} impurity \left( i \right)
```
<p align='center'>
  <img alt="decision-tree-example" width="600" src="https://github.com/mohammadAbbasniya/EvolutionStrategy_PointsInCircle/blob/main/README.imgs/bests.png">
</p>


## About Evolutionary Strategy
In computer science, an evolution strategy (ES) is an optimization technique based on ideas of evolution. It belongs to the general class of evolutionary computation or artificial evolution methodologies. Evolution strategies use natural problem-dependent representations, so problem space and search space are identical. In common with evolutionary algorithms, the operators are applied in a loop. An iteration of the loop is called a generation. The sequence of generations is continued until a termination criterion is met [[Wiki](https://en.wikipedia.org/wiki/Evolution_strategy)]. In each generation new individuals (offspring) are created using **Recombination** or **Mutation**.
<p align='center'>
  <img alt="ES-flow" width="600" src="https://github.com/mohammadAbbasniya/EvolutionStrategy_PointsInCircle/blob/main/README.imgs/ES-flow.png">
</p>


## Project structure 
- ### 📂 directory [genetic_decision_tree]
  - #### 📄 [main.py]
  - #### 📄 [main.py]
  - #### 📄 [main.py]
- ### 📂 directory [outputs]
