## Sequential Digits
**Problem Link:** https://leetcode.com/problems/sequential-digits/description

**Problem Statement:**
- Input format: Given an integer `low` and `high`, find all sequential digits in the range `[low, high]`.
- Constraints: `10^1 <= low <= high <= 10^9`.
- Expected output format: A list of integers representing sequential digits in the given range.
- Key requirements and edge cases to consider: 
  - Low and high are integers, and the range includes both low and high.
  - Sequential digits are those where each digit is one more than the previous digit (e.g., 123, 456, 789).
- Example test cases with explanations:
  - For `low = 100, high = 300`, one of the valid outputs is `[123, 234]` because these numbers are sequential digits within the given range.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all numbers in the range `[low, high]` and check if each number is a sequential digit.
- Step-by-step breakdown of the solution:
  1. Loop through all numbers from `low` to `high`.
  2. For each number, convert it to a string to easily access each digit.
  3. Check if the digits are sequential by comparing each digit with its previous one.
  4. If a number is a sequential digit, add it to the result list.

```cpp
vector<int> sequentialDigits(int low, int high) {
    vector<int> result;
    for (int num = low; num <= high; num++) {
        string strNum = to_string(num);
        bool isSequential = true;
        for (int i = 1; i < strNum.size(); i++) {
            if (strNum[i] - strNum[i-1] != 1) {
                isSequential = false;
                break;
            }
        }
        if (isSequential) {
            result.push_back(num);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of integers in the range `[low, high]` and $m$ is the average number of digits in these integers. This is because for each number, we potentially check each of its digits.
> - **Space Complexity:** $O(n)$, for storing the result list in the worst case where all numbers are sequential digits.
> - **Why these complexities occur:** The brute force approach checks every number and every digit within those numbers, leading to linear complexity in terms of the range and the average length of the numbers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all numbers, generate only the possible sequential digits by considering the length of the numbers and the starting digit.
- Detailed breakdown of the approach:
  1. Determine the possible lengths of sequential digits within the range `[low, high]`.
  2. For each possible length, generate sequential digits starting from each possible digit (1 through 9, but limited by the length and the upper bound `high`).
  3. Check if the generated sequential digit falls within the range `[low, high]`.
  4. If it does, add it to the result list.

```cpp
vector<int> sequentialDigits(int low, int high) {
    vector<int> result;
    string digits = "123456789";
    for (int length = to_string(low).size(); length <= to_string(high).size(); length++) {
        for (int start = 0; start <= 9 - length; start++) {
            int num = stoi(digits.substr(start, length));
            if (low <= num && num <= high) {
                result.push_back(num);
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(9 \cdot m)$, where $m$ is the maximum number of digits in the range `[low, high]`. This is because we consider each possible starting digit and each possible length up to $m$.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output, because we use a constant amount of space to store the string of digits and other variables.
> - **Optimality proof:** This approach is optimal because it only generates and checks numbers that could potentially be sequential digits within the given range, avoiding unnecessary checks.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Generation of sequential numbers, string manipulation for digit access, and optimization by limiting the search space.
- Problem-solving patterns identified: Looking for ways to reduce the search space and using string manipulation for digit-level operations.
- Optimization techniques learned: Focusing on generating only potential solutions rather than checking all possibilities.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect loop bounds, forgetting to check the range condition for generated numbers.
- Edge cases to watch for: Handling numbers with different lengths, ensuring the starting digit is within a valid range.
- Performance pitfalls: Using brute force approaches for large ranges, not optimizing the generation of potential solutions.
- Testing considerations: Thoroughly testing with different ranges, including edge cases like small ranges or ranges that start with a high digit.