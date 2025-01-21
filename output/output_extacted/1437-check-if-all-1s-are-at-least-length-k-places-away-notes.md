## Check If All 1's Are At Least Length K Places Away

**Problem Link:** https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description

**Problem Statement:**
- Input format and constraints: The problem takes an array `nums` and an integer `k` as inputs. The array `nums` contains only 0s and 1s, and `k` is a non-negative integer.
- Expected output format: The function should return `true` if all 1s in the array are at least `k` places away from each other, and `false` otherwise.
- Key requirements and edge cases to consider: The function should handle edge cases such as an empty array, an array with no 1s, and an array with 1s that are not at least `k` places away from each other.
- Example test cases with explanations:
  - `nums = [1,0,0,1,0,1]`, `k = 2`: Returns `false` because the 1s at indices 0 and 3 are not at least 2 places away from each other.
  - `nums = [1,0,0,0,1,0,0,1]`, `k = 2`: Returns `true` because all 1s are at least 2 places away from each other.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all pairs of 1s in the array to see if they are at least `k` places away from each other.
- Step-by-step breakdown of the solution:
  1. Iterate through the array to find all indices of 1s.
  2. For each pair of 1s, calculate the distance between them.
  3. If any pair of 1s is not at least `k` places away from each other, return `false`.
- Why this approach comes to mind first: This approach is straightforward and involves checking all possible pairs of 1s, which makes it easy to understand and implement.

```cpp
bool kLengthApart(vector<int>& nums, int k) {
    vector<int> indices;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == 1) {
            indices.push_back(i);
        }
    }
    for (int i = 0; i < indices.size() - 1; i++) {
        if (indices[i + 1] - indices[i] <= k) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we iterate through the array once to find all indices of 1s, and then iterate through the indices once to check all pairs.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all indices of 1s in the array.
> - **Why these complexities occur:** The time complexity is linear because we perform two linear scans, and the space complexity is linear because we need to store all indices of 1s.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing all indices of 1s and then checking all pairs, we can keep track of the index of the last seen 1 and check if the current 1 is at least `k` places away from it.
- Detailed breakdown of the approach:
  1. Initialize a variable `lastSeen` to -1, which will store the index of the last seen 1.
  2. Iterate through the array. For each 1, check if it is at least `k` places away from the last seen 1.
  3. If a 1 is not at least `k` places away from the last seen 1, return `false`.
  4. If we finish iterating through the array without returning `false`, return `true`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array, and it uses constant space to store the index of the last seen 1.

```cpp
bool kLengthApart(vector<int>& nums, int k) {
    int lastSeen = -1;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == 1) {
            if (lastSeen != -1 && i - lastSeen <= k) {
                return false;
            }
            lastSeen = i;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we only need to iterate through the array once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the index of the last seen 1.
> - **Optimality proof:** This approach is optimal because it has the best possible time complexity ($O(n)$) and space complexity ($O(1)$) for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of iterating through an array and keeping track of relevant information (in this case, the index of the last seen 1).
- Problem-solving patterns identified: The problem illustrates the pattern of using a single pass through the data to solve the problem, which is often the most efficient approach.
- Optimization techniques learned: The problem shows how to optimize a brute force approach by reducing the amount of space used and the number of operations performed.
- Similar problems to practice: Other problems that involve iterating through an array and keeping track of relevant information, such as finding the maximum or minimum value in an array.

**Mistakes to Avoid:**
- Common implementation errors: One common error is to forget to initialize the `lastSeen` variable to -1, which can cause the function to return incorrect results.
- Edge cases to watch for: The function should handle edge cases such as an empty array, an array with no 1s, and an array with 1s that are not at least `k` places away from each other.
- Performance pitfalls: One performance pitfall is to use a brute force approach that has a high time or space complexity, which can cause the function to run slowly or use too much memory.
- Testing considerations: The function should be tested with a variety of inputs, including edge cases, to ensure that it works correctly in all situations.