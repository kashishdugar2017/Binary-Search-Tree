# Binary Search Tree

A binary search tree I built from scratch in Python.

## How it works
Each node has a value, a left and a right. The rule: smaller numbers go left, bigger numbers go right. The top node is called the root.

## Insert
Start at the root. If the new number is smaller, go left; if bigger, go right. Keep going down until you find an empty spot (None), then put the new node there.

## Inorder
Inorder visits left, then the node, then right. Everything on a node's left is smaller, so it prints first. That's why the numbers come out sorted.

## How to run
`python main.py`

Inserting 5, 3, 8, 1 prints: 1 3 5 8
