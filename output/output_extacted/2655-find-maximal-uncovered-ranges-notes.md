## Find Maximal Uncovered Ranges

**Problem Link:** https://leetcode.com/problems/find-maximal-uncovered-ranges/description

**Problem Statement:**
- Input format and constraints: Given a sorted array `n` of distinct integers and an integer `maxn`, find all maximal uncovered ranges.
- Expected output format: Return a list of arrays, where each array contains two integers representing the start and end of an uncovered range.
- Key requirements and edge cases to consider: 
  - The input array `n` is sorted and contains distinct integers.
  - The integer `maxn` represents the maximum value in the range.
  - A range is considered uncovered if it does not contain any element from the array `n`.
- Example test cases with explanations:
  - Example 1: Input: `n = [0,1,3,50,75]`, `maxn = 99`. Output: `[[2,2],[4,4],[5,49],[51,74],[76,99]]`.
  - Example 2: Input: `n = []`, `maxn = 3`. Output: `[[0,3]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all possible ranges from 0 to `maxn` and check if each range is uncovered.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the uncovered ranges.
  2. Iterate through all possible ranges from 0 to `maxn`.
  3. For each range, check if it is uncovered by iterating through the array `n`.
  4. If the range is uncovered, add it to the list of uncovered ranges.
- Why this approach comes to mind first: It is a straightforward and intuitive solution, but it is not efficient due to its high time complexity.

```cpp
vector<vector<int>> findMaximalUncoveredRanges(vector<int>& n, int maxn) {
    vector<vector<int>> uncoveredRanges;
    for (int i = 0; i <= maxn; i++) {
        for (int j = i; j <= maxn; j++) {
            bool isUncovered = true;
            for (int num : n) {
                if (num >= i && num <= j) {
                    isUncovered = false;
                    break;
                }
            }
            if (isUncovered) {
                uncoveredRanges.push_back({i, j});
            }
        }
    }
    return uncoveredRanges;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(maxn^3 + n \cdot maxn^2)$, where $n$ is the size of the array `n` and $maxn$ is the maximum value in the range. This is because we have three nested loops: two for iterating through all possible ranges and one for checking if a range is uncovered.
> - **Space Complexity:** $O(maxn^2)$, where $maxn$ is the maximum value in the range. This is because we need to store all uncovered ranges in the list.
> - **Why these complexities occur:** The high time complexity occurs because we are iterating through all possible ranges and checking if each range is uncovered. The high space complexity occurs because we need to store all uncovered ranges.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through the array `n` to find all uncovered ranges.
- Detailed breakdown of the approach:
  1. Initialize an empty list to store the uncovered ranges.
  2. If the array `n` is empty, add the range `[0, maxn]` to the list of uncovered ranges.
  3. Iterate through the array `n`. For each element, check if the previous element is not adjacent to it. If it is not adjacent, add the uncovered range to the list.
  4. After iterating through the array `n`, check if the last element is not equal to `maxn`. If it is not equal, add the uncovered range to the list.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array `n` and uses a constant amount of space to store the previous element.

```cpp
vector<vector<int>> findMaximalUncoveredRanges(vector<int>& n, int maxn) {
    vector<vector<int>> uncoveredRanges;
    if (n.empty()) {
        uncoveredRanges.push_back({0, maxn});
        return uncoveredRanges;
    }
    if (n[0] > 0) {
        uncoveredRanges.push_back({0, n[0] - 1});
    }
    for (int i = 1; i < n.size(); i++) {
        if (n[i] - n[i - 1] > 1) {
            uncoveredRanges.push_back({n[i - 1] + 1, n[i] - 1});
        }
    }
    if (n.back() < maxn) {
        uncoveredRanges.push_back({n.back() + 1, maxn});
    }
    return uncoveredRanges;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the array `n`. This is because we only need to iterate through the array `n` once.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the array `n`. This is because we need to store all uncovered ranges in the list.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the array `n` and uses a linear amount of space to store the uncovered ranges.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and array manipulation.
- Problem-solving patterns identified: Using a single pass through the array to find all uncovered ranges.
- Optimization techniques learned: Reducing the number of iterations and using a constant amount of space.
- Similar problems to practice: Finding all uncovered ranges in a given array, finding all maximal uncovered ranges in a given array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty array or a range that is not uncovered.
- Edge cases to watch for: An empty array, a range that is not uncovered, and a range that is not maximal.
- Performance pitfalls: Using a high time complexity algorithm, such as the brute force approach.
- Testing considerations: Testing the algorithm with different input sizes, including edge cases and large inputs.