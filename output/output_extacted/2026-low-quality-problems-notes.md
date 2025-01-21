## Low Quality Problems

**Problem Link:** https://leetcode.com/problems/low-quality-problems/description

**Problem Statement:**
- Input format and constraints: Given a list of problems and their corresponding likes and dislikes.
- Expected output format: Return the problems with more likes than dislikes.
- Key requirements and edge cases to consider: 
    * Empty list
    * List with single element
    * Problems with equal likes and dislikes
- Example test cases with explanations:
    * problems = [[1,2],[2,3],[3,4]] 
    * likes = [3,3,2]
    * dislikes = [2,1,1]

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each problem and compare its likes and dislikes.
- Step-by-step breakdown of the solution:
    1. Create a result list to store problems with more likes than dislikes.
    2. Iterate through each problem.
    3. Compare likes and dislikes for each problem.
    4. If likes are more than dislikes, add the problem to the result list.
- Why this approach comes to mind first: It's a straightforward and intuitive approach.

```cpp
class Solution {
public:
    vector<int> findLowQualityProblems(vector<vector<int>>& problems, vector<int>& likes, vector<int>& dislikes) {
        vector<int> result;
        for (int i = 0; i < problems.size(); i++) {
            if (likes[i] > dislikes[i]) {
                result.push_back(problems[i][0]);
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of problems. This is because we are iterating through each problem once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of problems. This is because in the worst case, we might have to store all problems in the result list.
> - **Why these complexities occur:** These complexities occur because we are using a single loop to iterate through the problems and a vector to store the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can't do better than a single pass through the problems.
- Detailed breakdown of the approach:
    1. Create a result list to store problems with more likes than dislikes.
    2. Iterate through each problem.
    3. Compare likes and dislikes for each problem.
    4. If likes are more than dislikes, add the problem to the result list.
- Proof of optimality: This is optimal because we must examine each problem at least once to determine if it has more likes than dislikes.
- Why further optimization is impossible: We can't avoid examining each problem, so the time complexity is optimal.

```cpp
class Solution {
public:
    vector<int> findLowQualityProblems(vector<vector<int>>& problems, vector<int>& likes, vector<int>& dislikes) {
        vector<int> result;
        for (int i = 0; i < problems.size(); i++) {
            if (likes[i] > dislikes[i]) {
                result.push_back(problems[i][0]);
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of problems. This is because we are iterating through each problem once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of problems. This is because in the worst case, we might have to store all problems in the result list.
> - **Optimality proof:** This is optimal because we must examine each problem at least once to determine if it has more likes than dislikes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Single pass iteration, conditional checks.
- Problem-solving patterns identified: Iterate through data, compare values, store results.
- Optimization techniques learned: None, this is already optimal.
- Similar problems to practice: Other problems that involve iterating through data and comparing values.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors, incorrect conditional checks.
- Edge cases to watch for: Empty input lists, lists with single elements.
- Performance pitfalls: Unnecessary iterations or comparisons.
- Testing considerations: Test with empty lists, lists with single elements, and lists with multiple elements.