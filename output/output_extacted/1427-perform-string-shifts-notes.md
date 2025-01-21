## Perform String Shifts

**Problem Link:** https://leetcode.com/problems/perform-string-shifts/description

**Problem Statement:**
- Input format and constraints: The problem takes a string `s` and a list of shift operations `shifts` as input. Each shift operation is a list containing a direction (0 for left shift, 1 for right shift) and the number of positions to shift.
- Expected output format: The function should return the resulting string after applying all shift operations.
- Key requirements and edge cases to consider: The string `s` will have a length between 1 and 10^4, and the list `shifts` will have a length between 1 and 10^3.
- Example test cases with explanations:
  - Input: `s = "abc", shifts = [[0,1],[1,1]]`
    Output: `"bac"`
    Explanation: First, we shift the string to the left by 1 position, resulting in `"bac"`. Then, we shift the string to the right by 1 position, resulting in `"cab"`.
  - Input: `s = "abcdefg", shifts = [[1,1],[1,1],[0,2]]`
    Output: `"cefgab"`
    Explanation: First, we shift the string to the right by 1 position, resulting in `"gabcdef"`. Then, we shift the string to the right by 1 position again, resulting in `"fgabcde"`. Finally, we shift the string to the left by 2 positions, resulting in `"cefgab"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can apply each shift operation one by one to the string.
- Step-by-step breakdown of the solution:
  1. Initialize the result string as the input string `s`.
  2. Iterate through each shift operation in the list `shifts`.
  3. For each shift operation, apply the shift to the result string.
  4. If the direction is 0 (left shift), remove the first `shift` characters from the result string and append them to the end.
  5. If the direction is 1 (right shift), remove the last `shift` characters from the result string and prepend them to the beginning.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it directly applies each shift operation to the string.

```cpp
string stringShift(string s, vector<vector<int>>& shifts) {
    string result = s;
    for (auto& shift : shifts) {
        if (shift[0] == 0) { // left shift
            string temp = result.substr(shift[1]);
            temp += result.substr(0, shift[1]);
            result = temp;
        } else { // right shift
            string temp = result.substr(result.size() - shift[1]);
            temp += result.substr(0, result.size() - shift[1]);
            result = temp;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the string and $m$ is the number of shift operations. This is because we are applying each shift operation to the string, and each shift operation takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we are storing the result string, which has the same length as the input string.
> - **Why these complexities occur:** The time complexity is high because we are applying each shift operation to the string, and each shift operation takes linear time. The space complexity is linear because we are storing the result string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of applying each shift operation to the string, we can calculate the total number of positions to shift and apply it only once.
- Detailed breakdown of the approach:
  1. Initialize the total shift as 0.
  2. Iterate through each shift operation in the list `shifts`.
  3. For each shift operation, add the shift value to the total shift if the direction is 0 (left shift), and subtract the shift value from the total shift if the direction is 1 (right shift).
  4. Take the total shift modulo the length of the string to handle cases where the total shift is greater than the length of the string.
  5. Apply the total shift to the string by removing the first `total_shift` characters and appending them to the end.
- Proof of optimality: This approach is optimal because it reduces the number of shift operations from $m$ to 1, where $m$ is the number of shift operations.

```cpp
string stringShift(string s, vector<vector<int>>& shifts) {
    int total_shift = 0;
    for (auto& shift : shifts) {
        if (shift[0] == 0) { // left shift
            total_shift += shift[1];
        } else { // right shift
            total_shift -= shift[1];
        }
    }
    total_shift = (total_shift % s.size() + s.size()) % s.size(); // handle negative total shift
    string result = s.substr(total_shift) + s.substr(0, total_shift);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the string and $m$ is the number of shift operations. This is because we are iterating through each shift operation and applying the total shift to the string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we are storing the result string, which has the same length as the input string.
> - **Optimality proof:** This approach is optimal because it reduces the number of shift operations from $m$ to 1, where $m$ is the number of shift operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: This problem demonstrates the concept of reducing the number of operations by calculating the total effect of multiple operations.
- Problem-solving patterns identified: This problem requires identifying the key insight that leads to the optimal solution, which is calculating the total shift and applying it only once.
- Optimization techniques learned: This problem demonstrates the technique of reducing the number of operations by calculating the total effect of multiple operations.
- Similar problems to practice: Other problems that require reducing the number of operations by calculating the total effect of multiple operations, such as the "Rotate Array" problem.

**Mistakes to Avoid:**
- Common implementation errors: One common implementation error is not handling the case where the total shift is greater than the length of the string.
- Edge cases to watch for: One edge case to watch for is when the input string is empty.
- Performance pitfalls: One performance pitfall is applying each shift operation to the string, which can result in high time complexity.
- Testing considerations: When testing the solution, make sure to test cases where the total shift is greater than the length of the string, and cases where the input string is empty.