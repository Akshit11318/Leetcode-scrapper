## Create Sorted Array Through Instructions

**Problem Link:** https://leetcode.com/problems/create-sorted-array-through-instructions/description

**Problem Statement:**
- Input: `instructions`, an array of integers representing the instructions to follow.
- Constraints: `1 <= instructions.length <= 100`, `1 <= instructions[i] <= 100`.
- Expected Output: The minimum cost to create a sorted array by following the instructions.
- Key Requirements:
  - Create a sorted array through instructions.
  - Calculate the minimum cost to create the sorted array.

**Example Test Cases:**
- `instructions = [1, 3, 3, 4, 2]`, the output should be `4`.
- `instructions = [1, 2, 3]`, the output should be `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of instructions to find the minimum cost.
- Step-by-step breakdown of the solution:
  1. Generate all possible permutations of the instructions.
  2. For each permutation, calculate the cost to create a sorted array by following the instructions.
  3. Return the minimum cost among all permutations.
- Why this approach comes to mind first: It's a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int createSortedArray(int* instructions, int instructionsSize) {
        // Initialize the minimum cost to a large value
        int minCost = INT_MAX;
        
        // Generate all possible permutations of the instructions
        vector<int> perm(instructions, instructions + instructionsSize);
        do {
            // Calculate the cost to create a sorted array by following the instructions
            int cost = 0;
            vector<int> sortedArray;
            for (int i = 0; i < instructionsSize; i++) {
                // Find the position to insert the current instruction
                int pos = lower_bound(sortedArray.begin(), sortedArray.end(), perm[i]) - sortedArray.begin();
                // Insert the current instruction into the sorted array
                sortedArray.insert(sortedArray.begin() + pos, perm[i]);
                // Update the cost
                cost += pos;
            }
            // Update the minimum cost
            minCost = min(minCost, cost);
        } while (next_permutation(perm.begin(), perm.end()));
        
        return minCost;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n \cdot log(n))$, where $n$ is the number of instructions. This is because we generate all possible permutations of the instructions, and for each permutation, we calculate the cost to create a sorted array by following the instructions.
> - **Space Complexity:** $O(n)$, where $n$ is the number of instructions. This is because we need to store the current permutation and the sorted array.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of instructions, which leads to a high time complexity. The space complexity is relatively low because we only need to store the current permutation and the sorted array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a `multiset` to store the sorted array, which allows us to insert elements and calculate the cost in $O(log(n))$ time.
- Detailed breakdown of the approach:
  1. Create a `multiset` to store the sorted array.
  2. Iterate over the instructions and insert each instruction into the `multiset`.
  3. For each instruction, calculate the cost to create a sorted array by following the instructions.
  4. Return the minimum cost.
- Proof of optimality: The optimal approach has a time complexity of $O(n \cdot log(n))$, which is the best possible time complexity for this problem.

```cpp
class Solution {
public:
    int createSortedArray(int* instructions, int instructionsSize) {
        // Create a multiset to store the sorted array
        multiset<int> sortedArray;
        
        // Initialize the minimum cost to 0
        int minCost = 0;
        
        // Iterate over the instructions
        for (int i = 0; i < instructionsSize; i++) {
            // Calculate the cost to create a sorted array by following the instructions
            int cost = distance(sortedArray.begin(), sortedArray.lower_bound(instructions[i]));
            // Update the minimum cost
            minCost += cost;
            // Insert the current instruction into the sorted array
            sortedArray.insert(instructions[i]);
        }
        
        return minCost;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(n))$, where $n$ is the number of instructions. This is because we use a `multiset` to store the sorted array, which allows us to insert elements and calculate the cost in $O(log(n))$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of instructions. This is because we need to store the sorted array.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n \cdot log(n))$, which is the best possible time complexity for this problem. This is because we need to iterate over the instructions and calculate the cost to create a sorted array by following the instructions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `multiset` to store a sorted array, calculating the cost to create a sorted array by following instructions.
- Problem-solving patterns identified: Using a data structure to store a sorted array, iterating over the instructions and calculating the cost.
- Optimization techniques learned: Using a `multiset` to reduce the time complexity, calculating the cost in $O(log(n))$ time.
- Similar problems to practice: Creating a sorted array through instructions with different constraints, calculating the cost to create a sorted array by following instructions with different data structures.

**Mistakes to Avoid:**
- Common implementation errors: Not using a `multiset` to store the sorted array, not calculating the cost in $O(log(n))$ time.
- Edge cases to watch for: Empty instructions, instructions with duplicate elements.
- Performance pitfalls: Not using a `multiset` to store the sorted array, not calculating the cost in $O(log(n))$ time.
- Testing considerations: Test the solution with different inputs, including empty instructions, instructions with duplicate elements, and large inputs.