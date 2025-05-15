# Largest Connected Cluster of 1s in a Binary Grid
Problem:
Given a matrix (2D grid) of 0s and 1s, implement an algorithm to determine the size of the largest connected cluster of 1s.
Additional Requirement:
Explain whether you would use a separate structure to mark visited cells and justify your choice.


# My thinking
## Brute force?
Such as:
for i in rows:
    for j in cols:
        ...

This option allows us to traversal in 1 dimension at a time.
However, we need to traversal both in x and y axis together.
-> Not easy to do it with 2 for-loops.
-> Skip it a bit.

## Graphs 
I'm thinking if this matrix is a representation of a graph?
Then we can traverse this graph.
Let's check it.
A graph can be represented with a matrix by 2 methods:
- Adjacency Matrix: this MUST be a square, (n, n) matrix. But we do not have a square matrix here -> drop it.
- Incidence Matrix: (vertices, edges): we have a (m, n) matrix. If m + n, it means we have loops and directed edges, which is hard to traversal. 
(At least I am not familiar with traversing this type.) -> skip it. 
 
## Trees?
Sound promising.
We consider a cell (in the array) as a root of an unknown tree, then we explore that "tree" with BFS or DFS.
Regardless of BFS or DFS, they both work, as we only need to count the number of edges of the tree.


Sketch algorithm:
Firstly,
    Modeling the input array of numbers to an array of cells

Secondly,
    Start at a any cell, run the below pseudocode for all cells.
    If cell.value = 1:
        if cell.visited == False:
            Traverse the cell.
            While traversing, measure the cluster size and return it.
            After traversing, compare with the maximum

    Return the maximum cluster size.
     
