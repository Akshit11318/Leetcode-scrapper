## Remove Trailing Zeros from a String
**Problem Link:** https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description

**Problem Statement:**
- Input: A string `num` representing a non-negative integer.
- Constraints: `1 <= num.length <= 1000`.
- Expected Output: The input string with trailing zeros removed.
- Key Requirements: Handle strings with leading zeros, and return the empty string if the input string only contains zeros.
- Example Test Cases:
  - Input: "0010"
    - Output: "001"
  - Input: "10000"
    - Output: "1"

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves iterating through the string from right to left and removing zeros until a non-zero character is encountered.
- This approach comes to mind first because it directly addresses the problem statement by removing trailing zeros.

```cpp
string removeTrailingZeros(string num) {
    // Start from the end of the string
    int i = num.length() - 1;
    while (i >= 0 && num[i] == '0') {
        // Remove the trailing zero
        num.pop_back();
        i--;
    }
    return num;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because in the worst case, we might need to iterate through the entire string.
> - **Space Complexity:** $O(1)$, assuming the input string can be modified in-place. Otherwise, $O(n)$ if we need to create a new string.
> - **Why these complexities occur:** The time complexity is linear due to the potential need to iterate through the entire string, and the space complexity is constant if we can modify the input string, or linear if a new string is required.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is recognizing that we can achieve the same result as the brute force approach but with more efficiency by using `std::string` methods to find and remove the trailing zeros in one step.
- The optimal approach involves using `std::string::find_last_not_of` to find the last non-zero character and then using `std::string::substr` to get the substring up to and including that character.

```cpp
string removeTrailingZeros(string num) {
    int lastNonZero = num.find_last_not_of('0');
    if (lastNonZero == std::string::npos) {
        // If no non-zero character is found, return an empty string
        return "";
    }
    return num.substr(0, lastNonZero + 1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because `find_last_not_of` needs to potentially scan the entire string.
> - **Space Complexity:** $O(n)$, because we are creating a new substring.
> - **Optimality proof:** This approach is optimal because it reduces the number of operations needed to remove trailing zeros to a single step after finding the last non-zero character, making it as efficient as possible given the constraints of the problem.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated include string manipulation and the use of standard library functions to simplify tasks.
- Problem-solving patterns identified include the importance of understanding the problem constraints and leveraging built-in functions for efficiency.
- Optimization techniques learned include minimizing the number of operations and using in-place modification when possible.

**Mistakes to Avoid:**
- Common implementation errors include not handling edge cases properly, such as an input string of all zeros.
- Edge cases to watch for include empty strings, strings with only one character, and strings with all zeros.
- Performance pitfalls include unnecessary iterations or creations of temporary strings.
- Testing considerations should include a variety of inputs, including edge cases and large inputs to ensure efficiency and correctness.