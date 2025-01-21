## Check If Number Has Equal Digit Count and Digit Value

**Problem Link:** https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description

**Problem Statement:**
- Input: An integer `num` containing digits from 1 to 9.
- Constraints: The input number will not be empty and will only contain digits from 1 to 9.
- Expected output: Return `true` if the number has equal digit count and digit value, otherwise return `false`.
- Key requirements: The function should iterate through each digit in the number, count the occurrences of each digit, and compare this count with the digit's value.
- Edge cases: Numbers with repeated digits, numbers with digits that are not present in the number (e.g., 0), and numbers with a single digit.

**Example Test Cases:**
- Input: `num = 121` - Output: `true`
- Input: `num = 2` - Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each digit in the number, count the occurrences of each digit, and compare this count with the digit's value.
- Step-by-step breakdown:
  1. Convert the integer into a string to easily access each digit.
  2. Create a frequency map to store the count of each digit.
  3. Iterate through the string representation of the number, updating the frequency map.
  4. After counting all digits, iterate through the frequency map and compare each digit's count with its value.
  5. If any digit's count does not match its value, return `false`. If all counts match, return `true`.

```cpp
bool digitCount(string num) {
    unordered_map<char, int> freqMap;
    for (char c : num) {
        freqMap[c]++;
    }
    for (int i = 0; i < num.size(); i++) {
        if (freqMap[num[i]] != num[i] - '0') {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits in the input number, because we iterate through the string twice: once to count the frequencies and once to compare these frequencies with the digit values.
> - **Space Complexity:** $O(n)$, as in the worst case, every digit in the number could be unique, requiring $n$ entries in the frequency map.
> - **Why these complexities occur:** The iteration through the string to count frequencies and the subsequent iteration to compare counts both contribute to the linear time complexity. The space complexity is due to the storage required for the frequency map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of creating a frequency map and then comparing counts, we can directly compare the count of each digit with its value as we iterate through the number. This eliminates the need for a second pass through the string.
- Detailed breakdown:
  1. Convert the integer into a string.
  2. Iterate through the string representation of the number.
  3. For each digit, count its occurrences in the string and compare this count with the digit's value.
  4. If any digit's count does not match its value, return `false`. If all counts match, return `true`.

```cpp
bool digitCount(string num) {
    for (int i = 0; i < num.size(); i++) {
        int count = 0;
        for (int j = 0; j < num.size(); j++) {
            if (num[j] == num[i]) count++;
        }
        if (count != num[i] - '0') return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of digits in the input number. This is because for each digit, we potentially iterate through the entire string to count its occurrences.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and indices.
> - **Optimality proof:** While this approach is not more efficient than the brute force in terms of time complexity, it demonstrates a different perspective on solving the problem by directly comparing counts with values without an explicit frequency map. However, the brute force approach is more efficient.

---

### Alternative Approach

**Explanation:**
- Different perspective: Using a single pass through the string to both count frequencies and compare them with digit values, without the need for a frequency map. This approach utilizes the fact that the problem only deals with single-digit numbers (1-9) and can thus use the digit itself as an index into an array to count occurrences.
- Unique trade-offs: This approach has a better space complexity than the brute force but may be less intuitive due to its use of an array to count frequencies.

```cpp
bool digitCount(string num) {
    int count[10] = {0}; // Assuming digits are from 0 to 9, but we know they're 1-9
    for (char c : num) {
        count[c - '0']++;
    }
    for (int i = 0; i < num.size(); i++) {
        if (count[i] != num[i] - '0') return false;
    }
    return true;
}
```

However, this is essentially the same as the brute force approach in terms of logic, just with an array instead of a map for counting. The optimal approach as defined earlier isn't truly optimal in terms of time complexity but demonstrates a point. The actual optimal approach in terms of time complexity remains the first brute force approach due to its clarity and efficiency.

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits in the input number.
> - **Space Complexity:** $O(1)$, because the array size is constant (10 elements for digits 0-9), regardless of the input size.
> - **Trade-off analysis:** This approach offers better space complexity than the original brute force but may be slightly less readable due to its use of an array. However, it's essentially the same logic as the brute force, just with an array for counting.

---

### Final Notes

**Learning Points:**
- The importance of understanding the constraints of the problem (e.g., digits are from 1 to 9).
- How to iterate through a string in C++ and manipulate characters.
- The use of frequency maps or arrays to count occurrences of digits.
- The trade-offs between different approaches, including time and space complexity.

**Mistakes to Avoid:**
- Not validating the input (though the problem statement guarantees certain constraints).
- Incorrectly comparing character values with integer values without proper conversion.
- Not considering edge cases, such as numbers with repeated digits or single-digit numbers.
- Failing to optimize the solution for better time or space complexity when possible.