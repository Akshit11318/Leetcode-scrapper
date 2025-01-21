## Distribute Candies Among Children II
**Problem Link:** https://leetcode.com/problems/distribute-candies-among-children-ii/description

**Problem Statement:**
- Given an integer `numChildren`, a list of integers `candies`, and an integer `extraCandies`, return the number of children who can have the greatest number of candies among them.
- Each child initially gets one candy.
- The goal is to find the number of children who can have the greatest number of candies after distributing the `extraCandies`.
- The `extraCandies` can be distributed among the children in any way.

**Expected Output Format:**
- The function should return a list of booleans, where each boolean represents whether the child can have the greatest number of candies.

**Key Requirements and Edge Cases to Consider:**
- The number of children is represented by `numChildren`.
- The initial candies each child has is represented by the list `candies`.
- The number of extra candies is represented by `extraCandies`.
- Edge cases include when `extraCandies` is 0, or when all children have the same number of candies.

**Example Test Cases with Explanations:**
- Example 1: `numChildren = 4`, `candies = [1,2,3]`, `extraCandies = 3`. The output should be `[true,true,true,false]`.
- Example 2: `numChildren = 4`, `candies = [1,2,3]`, `extraCandies = 1`. The output should be `[false,false,true,false]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate over each child and check if they can have the greatest number of candies after distributing the `extraCandies`.
- The brute force approach involves calculating the maximum number of candies each child can have and comparing it with the maximum number of candies any child can have.

```cpp
vector<bool> kidsWithCandies(int numChildren, vector<int>& candies, int extraCandies) {
    vector<bool> result;
    for (int i = 0; i < numChildren; i++) {
        if (i < candies.size()) {
            if (candies[i] + extraCandies >= *max_element(candies.begin(), candies.end())) {
                result.push_back(true);
            } else {
                result.push_back(false);
            }
        } else {
            if (1 + extraCandies >= *max_element(candies.begin(), candies.end())) {
                result.push_back(true);
            } else {
                result.push_back(false);
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of children and $m$ is the number of candies. This is because we are iterating over each child and finding the maximum number of candies.
> - **Space Complexity:** $O(n)$, where $n$ is the number of children. This is because we are storing the result for each child.
> - **Why these complexities occur:** The time complexity occurs because we are using a nested loop to iterate over each child and find the maximum number of candies. The space complexity occurs because we are storing the result for each child.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to first find the maximum number of candies any child can have.
- Then, iterate over each child and check if they can have the greatest number of candies after distributing the `extraCandies`.
- This approach is optimal because it only requires a single pass over the children and candies.

```cpp
vector<bool> kidsWithCandies(int numChildren, vector<int>& candies, int extraCandies) {
    int maxCandies = *max_element(candies.begin(), candies.end());
    vector<bool> result;
    for (int i = 0; i < numChildren; i++) {
        if (i < candies.size()) {
            result.push_back(candies[i] + extraCandies >= maxCandies);
        } else {
            result.push_back(1 + extraCandies >= maxCandies);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of children and $m$ is the number of candies. This is because we are finding the maximum number of candies and then iterating over each child.
> - **Space Complexity:** $O(n)$, where $n$ is the number of children. This is because we are storing the result for each child.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the children and candies, and it uses a constant amount of extra space to store the result.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a single pass over the data to find the maximum value and then iterate over each child to check if they can have the greatest number of candies.
- The problem-solving pattern identified is to first find the maximum value and then use that value to make comparisons.
- The optimization technique learned is to avoid using nested loops and instead use a single pass over the data.

**Mistakes to Avoid:**
- A common implementation error is to use a nested loop to iterate over each child and find the maximum number of candies.
- An edge case to watch for is when `extraCandies` is 0, or when all children have the same number of candies.
- A performance pitfall is to use a brute force approach that has a high time complexity.