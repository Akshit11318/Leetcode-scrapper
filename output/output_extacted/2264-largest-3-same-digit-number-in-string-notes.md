## Largest 3 Same Digit Number in String

**Problem Link:** https://leetcode.com/problems/largest-3-same-digit-number-in-string/description

**Problem Statement:**
- Input: A string `num` consisting of digits.
- Constraints: `3 <= num.length <= 1000`.
- Expected Output: The largest 3-digit number that can be formed by selecting digits from `num` such that all digits are the same.
- Key Requirements: 
    - All digits in the output must be the same.
    - The output must be the largest possible.
    - If no such number can be formed, return an empty string.
- Edge Cases:
    - If there are less than 3 occurrences of any digit, return an empty string.
    - If the string contains non-digit characters, the problem statement does not specify behavior, but we assume it will only contain digits.
- Example Test Cases:
    - Input: `num = "6777133339"`
      Output: `"777"`
    - Input: `num = "2300019"`
      Output: `"000"`
    - Input: `num = "42352338"`
      Output: `"888"` (Note: There are no three '8's in the input string, so this example would return an empty string if following the exact problem constraints)

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible combination of 3 digits from the string to find the largest number that consists of the same digits.
- However, since we are looking for the largest number and all digits must be the same, we can simplify this by counting the occurrences of each digit and then finding the largest digit that appears at least 3 times.

```cpp
string largestGoodInteger(string num) {
    unordered_map<char, int> count;
    for (char c : num) {
        if (count.find(c) != count.end()) {
            count[c]++;
        } else {
            count[c] = 1;
        }
    }
    
    char maxDigit = '0';
    for (auto& pair : count) {
        if (pair.second >= 3 && pair.first > maxDigit) {
            maxDigit = pair.first;
        }
    }
    
    if (maxDigit > '0') {
        string result(3, maxDigit);
        return result;
    } else {
        return "";
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string `num`, because we are iterating over the string once to count the occurrences of each digit, and then iterating over the map to find the maximum digit. The map operations (insertion and lookup) are $O(1)$ on average.
> - **Space Complexity:** $O(1)$ because the size of the map is at most 10 (for digits 0-9), which is constant.
> - **Why these complexities occur:** The iteration over the string and the map operations determine the time complexity. The space complexity is due to the use of the map to store the counts of each digit.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is essentially the same as the brute force approach since it already has a linear time complexity and constant space complexity. However, we can slightly optimize the code by directly returning the result as soon as we find a digit that appears at least 3 times, without needing to find the maximum digit separately.

```cpp
string largestGoodInteger(string num) {
    unordered_map<char, int> count;
    for (char c : num) {
        if (count.find(c) != count.end()) {
            count[c]++;
            if (count[c] >= 3) {
                string result(3, c);
                return result;
            }
        } else {
            count[c] = 1;
        }
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string `num$, because in the worst case, we still have to iterate over the entire string.
> - **Space Complexity:** $O(1)$ because the size of the map is at most 10 (for digits 0-9), which is constant.
> - **Optimality proof:** This is optimal because we must at least read the input string once to solve the problem, which already takes $O(n)$ time. The constant space complexity is also optimal since we only need to keep track of the counts of the digits.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, mapping, and basic string manipulation.
- Problem-solving patterns identified: Looking for the maximum or minimum value that satisfies certain conditions.
- Optimization techniques learned: Reducing the number of iterations or operations by directly returning the result when the condition is met.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases (like an empty string or a string with less than 3 occurrences of any digit).
- Edge cases to watch for: Non-digit characters in the input string, although the problem statement assumes the string will only contain digits.
- Performance pitfalls: Unnecessary iterations or operations that could increase the time complexity.
- Testing considerations: Ensure to test with various inputs, including edge cases like strings with repeating digits and strings without any repeating digits.