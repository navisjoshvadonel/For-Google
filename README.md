# 🚀 Google Interview Prep & Algorithmic Solutions

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LeetCode Profile](https://img.shields.io/badge/LeetCode-Solutions-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/)
[![Code Style](https://img.shields.io/badge/code%20style-pep8-green.svg?style=for-the-badge)](https://www.python.org/dev/peps/pep-0008/)

Welcome to my algorithm prep repository. This collection contains optimized, clean, and production-ready Python solutions to classic computational problems frequently encountered in Google technical assessments.

---

## 🛠️ Software Engineering Principles Applied
Google engineers value more than just code that "works." Here are the architectural standards followed in every solution:
*   **Time & Space Efficiency:** Algorithms are designed to meet optimal theoretical bounds. Space/Time analysis is documented explicitly.
*   **Self-Documenting Code:** Clean, descriptive variable names and minimal, high-impact comments explaining the *why*, not just the *what*.
*   **Built-in Verification:** Every solution includes runnable test blocks containing multiple test cases (including edge cases) to guarantee correctness and ease of verification.
*   **Edge-Case Resiliency:** Implementations proactively handle bounds (e.g., empty arrays, null trees, single-element structures, case-insensitivity, non-alphanumeric chars).

---

## 📂 Problem Index

The repository is categorized by algorithmic patterns to show a structured approach to problem-solving.

| # | Problem | Algorithmic Pattern | Time Complexity | Space Complexity | Solution Link |
|---|---------|---------------------|-----------------|------------------|---------------|
| 1 | **Two Sum** | Hash Map / Array lookup | $O(N)$ | $O(N)$ | [Two sums.py](./Two%20sums.py) |
| 2 | **Longest Substring Without Repeating Characters** | Sliding Window / Hash Set | $O(N)$ | $O(\min(M, N))$ | [Substring Slidingwindow.py](./Substring%20Slidingwindow.py) |
| 3 | **Valid Parentheses** | Stack / Mapping | $O(N)$ | $O(N)$ | [StackIsvalid.py](./StackIsvalid.py) |
| 4 | **Merge Two Sorted Lists** | Linked List / Dummy Head | $O(N + M)$ | $O(1)$ | [mergeLinkedSortlist.py](./mergeLinkedSortlist.py) |
| 5 | **Reverse Linked List** | Linked List / In-place Mutation | $O(N)$ | $O(1)$ | [linkedList.py](./linkedList.py) |
| 6 | **Maximum Depth of Binary Tree** | Binary Tree / DFS Recursion | $O(N)$ | $O(H)$ (Height) | [MaxDepth.py](./MaxDepth.py) |
| 7 | **Binary Search** | Divide & Conquer / Two Pointers | $O(\log N)$ | $O(1)$ | [binarSearch.py](./binarSearch.py) |
| 8 | **Best Time to Buy and Sell Stock** | Greedy / Dynamic Programming | $O(N)$ | $O(1)$ | [Stockprices.py](./Stockprices.py) |
| 9 | **Valid Palindrome** | Two Pointers / String Manipulation | $O(N)$ | $O(1)$ | [palindrome.py](./palindrome.py) |
| 10 | **Invert Binary Tree** | Binary Tree / DFS Recursion | $O(N)$ | $O(H)$ (Height) | [InvertTree.py](./InvertTree.py) |
| 11 | **Binary Tree Level Order Traversal** | Queue / BFS | $O(N)$ | $O(N)$ | [bfs.py](./bfs.py) |


---

## 💡 Algorithmic Highlights

### 1. Sliding Window & Two Pointers
*   **Problem:** [Substring Slidingwindow.py](./Substring%20Slidingwindow.py)
*   **Technique:** A dynamic window sliding over the string dynamically updates bounds by keeping track of elements in a `set`. By shrinking the left bound only when a duplicate is found, we process the array in a single linear pass ($O(N)$), avoiding nested $O(N^2)$ loops.

### 2. In-Place Linked List Manipulation
*   **Problem:** [linkedList.py](./linkedList.py) & [mergeLinkedSortlist.py](./mergeLinkedSortlist.py)
*   **Technique:** Reversing list links or merging them without allocating auxiliary memory lists. Utilizing temporary pointer swaps ensures $O(1)$ auxiliary space complexity—demonstrating clean memory management.

### 3. Tree Recursion (DFS)
*   **Problem:** [MaxDepth.py](./MaxDepth.py)
*   **Technique:** Utilizing the call stack to compute subproblem answers recursively ($1 + \max(\text{left}, \text{right})$). Space complexity scales with tree height $O(H)$ which defaults to $O(\log N)$ for balanced trees.

---

## 🚦 How to Run & Verify

Every script is designed as an executable standalone program containing test cases. You can run any file locally with Python 3:

```bash
# Example: Running the Sliding Window solution
python "Substring Slidingwindow.py"

# Example: Running the Tree Depth solution
python MaxDepth.py
```

Expected outputs will print directly to the console (e.g., test cases comparing output to targets).

---

## 📬 Let's Connect!

I am actively practicing advanced data structures and algorithms, system design, and software engineering best practices. 

*   **GitHub:** [@your-github-username](https://github.com/your-github-username)
*   **LinkedIn:** [Your LinkedIn Profile Name](https://www.linkedin.com/in/your-linkedin/)
*   **LeetCode Profile:** [Your LeetCode Handle](https://leetcode.com/your-leetcode-username/)

*Feel free to explore my solutions, review my commit history to see my incremental development style, or get in touch for software engineering opportunities!*
