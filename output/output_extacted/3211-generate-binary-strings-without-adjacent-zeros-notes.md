## Generate Binary Strings Without Adjacent Zeros

**Problem Link:** https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description

**Problem Statement:**
- Input format and constraints: The problem asks to generate all possible binary strings of length `n` without any adjacent zeros.
- Expected output format: The output should be a vector of strings, where each string is a binary string without adjacent zeros.
- Key requirements and edge cases to consider: The input `n` is a positive integer, and the output should include all possible binary strings that satisfy the condition.
- Example test cases with explanations: For `n = 1`, the output should be `["0", "1"]`. For `n = 2`, the output should be `["10", "11"]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible binary strings of length `n` and then filtering out the strings that have adjacent zeros.
- Step-by-step breakdown of the solution:
  1. Generate all possible binary strings of length `n`.
  2. For each generated string, check if it has any adjacent zeros.
  3. If a string does not have any adjacent zeros, add it to the result list.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is not efficient for large values of `n` because it generates all possible binary strings, which is a time-consuming operation.

```cpp
vector<string> generateBinaryStrings(int n) {
    vector<string> result;
    // Generate all possible binary strings of length n
    for (int i = 0; i < (1 << n); i++) {
        string binaryString = "";
        for (int j = 0; j < n; j++) {
            binaryString += ((i >> j) & 1) ? '1' : '0';
        }
        bool isValid = true;
        // Check if the string has any adjacent zeros
        for (int j = 0; j < n - 1; j++) {
            if (binaryString[j] == '0' && binaryString[j + 1] == '0') {
                isValid = false;
                break;
            }
        }
        if (isValid) {
            result.push_back(binaryString);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the binary string. The outer loop generates all possible binary strings, which takes $O(2^n)$ time. The inner loop checks if a string has any adjacent zeros, which takes $O(n)$ time.
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the binary string. The space complexity is dominated by the storage of the result list, which can contain up to $2^n$ strings, each of length $n$.
> - **Why these complexities occur:** The brute force approach generates all possible binary strings, which leads to an exponential time complexity. The space complexity is also exponential because the result list can contain a large number of strings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution uses dynamic programming to generate the binary strings without adjacent zeros. The idea is to build the strings iteratively, starting from the first character, and at each step, add a character that does not create adjacent zeros.
- Detailed breakdown of the approach:
  1. Initialize an empty result list.
  2. Start with an empty string and add it to the result list.
  3. For each string in the result list, add a '0' or '1' to the end of the string, but only if the resulting string does not have adjacent zeros.
  4. Repeat step 3 until the length of the strings in the result list reaches `n`.
- Proof of optimality: The optimal solution has a time complexity of $O(2^n)$, which is the minimum time complexity required to generate all possible binary strings without adjacent zeros.

```cpp
vector<string> generateBinaryStrings(int n) {
    vector<string> result = {""};
    for (int i = 0; i < n; i++) {
        vector<string> temp;
        for (const string& str : result) {
            if (str.empty() || str.back() == '1') {
                temp.push_back(str + "0");
            }
            temp.push_back(str + "1");
        }
        result = temp;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the binary string. The time complexity is dominated by the generation of the result list, which can contain up to $2^n$ strings.
> - **Space Complexity:** $O(2^n)$, where $n$ is the length of the binary string. The space complexity is dominated by the storage of the result list, which can contain up to $2^n$ strings.
> - **Optimality proof:** The optimal solution has a time complexity of $O(2^n)$, which is the minimum time complexity required to generate all possible binary strings without adjacent zeros. This is because the solution generates each string exactly once, and there are $2^n$ possible binary strings of length `n`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, iterative string generation.
- Problem-solving patterns identified: The problem can be solved using a bottom-up approach, starting from the base case and building up to the final solution.
- Optimization techniques learned: The optimal solution uses dynamic programming to avoid generating duplicate strings and to reduce the time complexity.
- Similar problems to practice: Generating all possible permutations of a set, generating all possible combinations of a set.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case correctly, not updating the result list correctly.
- Edge cases to watch for: The input `n` can be 0 or 1, which requires special handling.
- Performance pitfalls: Generating all possible binary strings without filtering out the strings with adjacent zeros can lead to an exponential time complexity.
- Testing considerations: The solution should be tested with different values of `n` to ensure that it generates all possible binary strings without adjacent zeros correctly.