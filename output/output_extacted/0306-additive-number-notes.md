## Additive Number
**Problem Link:** https://leetcode.com/problems/additive-number/description

**Problem Statement:**
- Input: a string `num` containing only digits.
- Constraints: `1 <= num.length <= 35`.
- Expected output: a boolean indicating whether `num` is an additive number.
- Key requirements:
  - An additive number is a string where its parts are consecutive numbers that add up to the next part.
  - The parts must be non-empty and not start with 0 unless they are zero itself.
- Example test cases:
  - Input: `"112358"`, Output: `true`, Explanation: The string can be divided into parts as `"1"`, `"1"`, `"2"`, `"3"`, `"5"`, `"8"`, where each part is a consecutive number that adds up to the next part.
  - Input: `"199100199"`, Output: `true`, Explanation: The string can be divided into parts as `"1"`, `"99"`, `"100"`, `"199"`, where each part is a consecutive number that adds up to the next part.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible combinations of parts from the input string and check if they form an additive sequence.
- Step-by-step breakdown:
  1. Generate all possible combinations of parts from the input string.
  2. For each combination, check if the parts form an additive sequence by comparing each part with the sum of the two preceding parts.
  3. If a combination is found that forms an additive sequence, return `true`.
  4. If no combination is found, return `false`.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible combinations, ensuring that no potential solution is missed.

```cpp
class Solution {
public:
    bool isAdditiveNumber(string num) {
        int n = num.size();
        for (int i = 1; i <= n / 2; i++) {
            for (int j = 1; j <= (n - i) / 2; j++) {
                string a = num.substr(0, i);
                string b = num.substr(i, j);
                if ((a.size() > 1 && a[0] == '0') || (b.size() > 1 && b[0] == '0')) {
                    continue;
                }
                string rest = num.substr(i + j);
                if (isAdditive(a, b, rest)) {
                    return true;
                }
            }
        }
        return false;
    }

    bool isAdditive(string a, string b, string rest) {
        while (rest.size() > 0) {
            string sum = to_string(stoi(a) + stoi(b));
            if (rest.find(sum) != 0) {
                return false;
            }
            rest = rest.substr(sum.size());
            a = b;
            b = sum;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the input string. This is because we generate all possible combinations of parts from the input string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the parts and the remaining string.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of parts from the input string, resulting in an exponential time complexity. The space complexity is linear because we only need to store the current combination of parts and the remaining string.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a backtracking approach to generate all possible combinations of parts from the input string.
- Detailed breakdown of the approach:
  1. Define a helper function to check if a string is a valid number (i.e., it does not start with 0 unless it is 0 itself).
  2. Define another helper function to check if a string is an additive number.
  3. Use a backtracking approach to generate all possible combinations of parts from the input string.
  4. For each combination, check if the parts form an additive sequence by comparing each part with the sum of the two preceding parts.
- Proof of optimality: The optimal approach has a time complexity of $O(2^n)$, which is the same as the brute force approach. However, the optimal approach uses a backtracking approach, which reduces the number of combinations that need to be checked, resulting in a more efficient solution.

```cpp
class Solution {
public:
    bool isAdditiveNumber(string num) {
        int n = num.size();
        for (int i = 1; i <= n / 2; i++) {
            if (i > 1 && num[0] == '0') {
                break;
            }
            for (int j = 1; j <= (n - i) / 2; j++) {
                if (j > 1 && num[i] == '0') {
                    break;
                }
                if (isValid(num, 0, i - 1) && isValid(num, i, i + j - 1)) {
                    string a = num.substr(0, i);
                    string b = num.substr(i, j);
                    string rest = num.substr(i + j);
                    if (isAdditive(a, b, rest)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    bool isValid(string num, int start, int end) {
        if (start == end) {
            return true;
        }
        if (num[start] == '0') {
            return false;
        }
        return true;
    }

    bool isAdditive(string a, string b, string rest) {
        while (rest.size() > 0) {
            string sum = to_string(stoi(a) + stoi(b));
            if (rest.find(sum) != 0) {
                return false;
            }
            rest = rest.substr(sum.size());
            a = b;
            b = sum;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the input string. This is because we generate all possible combinations of parts from the input string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the parts and the remaining string.
> - **Optimality proof:** The optimal approach has a time complexity of $O(2^n)$, which is the same as the brute force approach. However, the optimal approach uses a backtracking approach, which reduces the number of combinations that need to be checked, resulting in a more efficient solution.

---

### Final Notes

**Learning Points:**
- The problem requires generating all possible combinations of parts from the input string and checking if they form an additive sequence.
- The optimal approach uses a backtracking approach to generate all possible combinations of parts from the input string.
- The problem requires careful handling of edge cases, such as checking if a string is a valid number (i.e., it does not start with 0 unless it is 0 itself).

**Mistakes to Avoid:**
- Not checking if a string is a valid number (i.e., it does not start with 0 unless it is 0 itself).
- Not using a backtracking approach to generate all possible combinations of parts from the input string.
- Not handling edge cases carefully, such as checking if a string is a valid number.