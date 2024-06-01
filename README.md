# Transportation Cost Minimization with Linear Programming

This project compares 3 papers on transportation cost minimization problems and aims to solve one of them using python and excel solver

#### Last Updated: June 1st, 2024

1. [Abstract](#abstract)
2. [Problem Formulation](#formulation)
3. [Linear Programming Model](#model)
4. [Solving Method](#solving)
5. [Benefits](#benefits)
6. [Future Enhancements](#enhancements)

<a name="abstract"></a>
## Abstract
Transportation is arguably one of the most crucial pillars of our modern-day world,
whether it’s commuting to work or having goods delivered to one’s nearby store. However,
unoptimized routes can lead to time waste and thus lead to an exponential rise in costs.
As such, minimizing transportation costs is the main area of research. Linear
programming models offer powerful tools to optimize transportation systems, addressing
problems like delivery truck scheduling, airline routing, and public transportation
optimization. This report will examine three research papers that utilize linear
programming models in different transportation problems around the world. We will
compare their approaches and how each one deals with their specific scenario and lastly
conclude on solving one of these models using simplex method and apply sensitivity
analysis accordingly.

<a name="formulation"></a>
## Problem Formulation:

- We define a transportation network with origins (suppliers) and destinations (customers).
- Each origin has a specific supply capacity, and each destination has a demand requirement for the product.
- The cost of transportation between each origin-destination pair is known (often represented as a cost matrix).

<a name="model"></a>
## Linear Programming Model:

- Decision variables `x_ij` represent the quantity shipped from origin i to destination j.
- The objective function minimizes the total transportation cost: Minimize `Z = ΣΣ (c_ij * x_ij)`, where c_ij is the cost per unit from i to j.
- Supply constraints ensure that the total amount shipped from each origin doesn't exceed its capacity: `Σx_ij ≤ S_i` for all origins i.
- Demand constraints guarantee that the total amount received by each destination meets its demand: `Σx_ij ≥ D_j` for all destinations j.
- Non-negativity constraints enforce that the shipped quantity cannot be negative: x_ij ≥ 0 for all i and j.

<a name="solving"></a>
## Solving Method:

The Simplex Method is a popular algorithm for solving linear programming problems, including transportation problems.

1. Excel Solver:

    - Build a spreadsheet with the cost matrix, supply, and demand data.
    - Define the decision variables `x_ij` in separate cells.
    - Set the objective function (Z) to the sum product of cost `c_ij` and quantity `x_ij` across all origin-destination pairs.
    - Use the Data Table or Solver add-in to define the constraints:
        - Supply constraints: Set the sum of x_ij for each origin row less than or equal to (<=) the corresponding supply (S_i).
        - Demand constraints: Set the sum of x_ij for each destination column greater than or equal to (>=) the corresponding demand (D_j).
        - Non-negativity constraints: Set a lower bound of 0 for all decision variables (x_ij).
    - Find an initial feasible solution by assigning shipments to minimize the total penalty cost.
    - Use Excel Solver to minimize the objective function (Z) subject to the defined constraints. Solver will find the optimal solution for the decision variables (x_ij) and the minimum transportation cost (Z).

<a name="benefits"></a>
## Benefits:

- Cost Savings: Identify the most cost-effective shipping strategy for minimizing overall transportation expenses.
- Improved Efficiency: Optimize resource allocation and reduce transportation bottlenecks.
- Strategic Planning: Gain insights into supply chain network performance for more informed decision-making.

<a name="enhancements"></a>
## Future Enhancements:

- Model Validation: Compare the optimal solution with real-world data to validate the model's accuracy.
- Sensitivity Analysis: Analyze how changes in supply, demand, or transportation costs affect the optimal solution.
- Scenario Planning: Develop different scenarios with varying parameters and solve the model to test its robustness.

