## Restore the Array
**Problem Link:** https://leetcode.com/problems/shuffle-string/description

**Problem Statement:**
- Input format and constraints: The problem takes a string `s` and an integer array `indices` as input, where `s` has a length of `n` and `indices` has a length of `n`. The task is to restore the original array from the shuffled array.
- Expected output format: The output should be a string representing the restored array.
- Key requirements and edge cases to consider: The problem requires restoring the original array based on the given shuffled array and indices. Edge cases include handling empty strings and arrays, as well as arrays with duplicate elements.
- Example test cases with explanations: 
    - Example 1: Input: `s = "codeleet"`, `indices = [4,5,6,7,0,2,1,3]`, Output: `"leetcode"`
    - Example 2: Input: `s = "abc"`, `indices = [0,1,2]`, Output: `"abc"`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves creating a new array and filling it with characters from the shuffled array based on the given indices.
- Step-by-step breakdown of the solution: 
    1. Create a new array of characters with the same length as the shuffled array.
    2. Iterate over the shuffled array and the indices array simultaneously.
    3. For each index, place the corresponding character from the shuffled array at the correct position in the new array.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, making it a natural first attempt at solving the problem.

```cpp
class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string result(s.size(), ' ');
        for (int i = 0; i < s.size(); i++) {
            result[indices[i]] = s[i];
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we are iterating over the string and the indices array once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we are creating a new array of characters to store the restored string.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each character in the string. The space complexity is also linear because we are creating a new array that is the same size as the input string.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, as it already has a time complexity of $O(n)$ and a space complexity of $O(n)$.
- Detailed breakdown of the approach: 
    1. Create a new array of characters with the same length as the shuffled array.
    2. Iterate over the shuffled array and the indices array simultaneously.
    3. For each index, place the corresponding character from the shuffled array at the correct position in the new array.
- Proof of optimality: This approach is optimal because it only requires a single pass over the input data and uses a minimal amount of extra space.
- Why further optimization is impossible: Further optimization is impossible because we must at least read the input data once and write the output data once, which already takes $O(n)$ time.

```cpp
class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string result(s.size(), ' ');
        for (int i = 0; i < s.size(); i++) {
            result[indices[i]] = s[i];
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we are iterating over the string and the indices array once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we are creating a new array of characters to store the restored string.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the input data and uses a minimal amount of extra space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of iteration and array manipulation to solve a string restoration problem.
- Problem-solving patterns identified: The problem requires identifying the correct position of each character in the restored string based on the given indices.
- Optimization techniques learned: The problem does not require any optimization techniques beyond the optimal approach.
- Similar problems to practice: Similar problems include string manipulation and array restoration problems.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to forget to initialize the result array with the correct size.
- Edge cases to watch for: Edge cases to watch for include empty strings and arrays, as well as arrays with duplicate elements.
- Performance pitfalls: A performance pitfall is to use an inefficient algorithm that has a higher time complexity than the optimal approach.
- Testing considerations: Testing considerations include testing the function with different input sizes and edge cases.