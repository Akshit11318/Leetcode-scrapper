## Maximum Difference by Remapping a Digit

**Problem Link:** https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description

**Problem Statement:**
- Input: A non-negative integer `num`.
- Expected output: The maximum difference between the original number and the number obtained after remapping a digit.
- Key requirements: We can remap at most one digit.
- Example test cases:
  - Input: `num = 1234`
  - Output: `1089`
  - Explanation: We can remap the digit `1` to `9` to get `9234`, and the difference is `9234 - 1234 = 8000`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible remappings of digits and calculate the maximum difference.
- Step-by-step breakdown of the solution:
  1. Convert the number to a string to easily access each digit.
  2. Iterate over each digit in the number.
  3. For each digit, try all possible remappings (0-9).
  4. Calculate the difference between the original number and the number obtained after remapping the digit.
  5. Keep track of the maximum difference found.

```cpp
int maxDiff(int num) {
    int max_diff = 0;
    string str = to_string(num);
    for (int i = 0; i < str.size(); i++) {
        for (int j = 0; j <= 9; j++) {
            string temp = str;
            temp[i] = '0' + j;
            int diff = abs(stoi(temp) - num);
            max_diff = max(max_diff, diff);
        }
    }
    return max_diff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 10)$, where $n$ is the number of digits in the input number. This is because we iterate over each digit and try all possible remappings (0-9) for each digit.
> - **Space Complexity:** $O(n)$, where $n$ is the number of digits in the input number. This is because we convert the number to a string to easily access each digit.
> - **Why these complexities occur:** The time complexity is high because we try all possible remappings for each digit, resulting in a lot of unnecessary calculations. The space complexity is moderate because we need to store the string representation of the number.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We only need to remap the first digit to the maximum possible digit (9) or the minimum possible digit (0) to get the maximum difference.
- Detailed breakdown of the approach:
  1. Convert the number to a string to easily access each digit.
  2. Check if the first digit is not 9. If it is not 9, we can remap it to 9 to get a larger number.
  3. Check if the first digit is not 0. If it is not 0, we can remap it to 0 to get a smaller number.
  4. Calculate the difference between the original number and the number obtained after remapping the digit.
  5. Keep track of the maximum difference found.

```cpp
int maxDiff(int num) {
    string str = to_string(num);
    int max_diff = 0;
    for (int i = 0; i < str.size(); i++) {
        if (str[i] != '9') {
            string temp = str;
            temp[i] = '9';
            int diff = abs(stoi(temp) - num);
            max_diff = max(max_diff, diff);
        }
        if (str[i] != '0') {
            string temp = str;
            temp[i] = '0';
            int diff = abs(stoi(temp) - num);
            max_diff = max(max_diff, diff);
        }
    }
    return max_diff;
}
```

However, the above solution is still not optimal as it has a time complexity of $O(n)$ and we can further optimize it by only checking the first digit.

```cpp
int maxDiff(int num) {
    string str = to_string(num);
    int max_diff = 0;
    if (str[0] != '9') {
        string temp = str;
        temp[0] = '9';
        int diff = abs(stoi(temp) - num);
        max_diff = max(max_diff, diff);
    }
    if (str[0] != '1' && str[0] != '0') {
        string temp = str;
        temp[0] = '1';
        int diff = abs(stoi(temp) - num);
        max_diff = max(max_diff, diff);
    }
    return max_diff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we only check the first digit and perform a constant number of operations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of digits in the input number. This is because we convert the number to a string to easily access each digit.
> - **Optimality proof:** This solution is optimal because we only need to check the first digit to get the maximum difference. Checking other digits would not result in a larger difference.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, optimization techniques.
- Problem-solving patterns identified: Checking the first digit to get the maximum difference.
- Optimization techniques learned: Reducing the number of operations by only checking the first digit.
- Similar problems to practice: Other optimization problems that involve finding the maximum or minimum difference.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the first digit correctly, not handling edge cases.
- Edge cases to watch for: When the first digit is 9 or 0, when the number is a single digit.
- Performance pitfalls: Checking all digits instead of just the first digit.
- Testing considerations: Test with different inputs, including edge cases and large numbers.