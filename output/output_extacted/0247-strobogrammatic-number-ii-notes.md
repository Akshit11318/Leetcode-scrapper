## Strobogrammatic Number II
**Problem Link:** https://leetcode.com/problems/strobogrammatic-number-ii/description

**Problem Statement:**
- Input format: An integer `n` representing the number of digits in the strobogrammatic number.
- Constraints: `1 <= n <= 2`.
- Expected output format: A list of all possible `n`-digit strobogrammatic numbers.
- Key requirements and edge cases to consider: Understanding the mapping of strobogrammatic digits and generating all combinations based on this mapping.
- Example test cases with explanations:
  - For `n = 1`, the output should be `["0", "1", "8"]` because these are the only single-digit strobogrammatic numbers.
  - For `n = 2`, the output should include `["11", "69", "88", "96"]` among others, as these are strobogrammatic when viewed upside down.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible numbers of length `n` and then filter out those that are not strobogrammatic.
- Step-by-step breakdown of the solution:
  1. Define a mapping of strobogrammatic digits.
  2. Generate all possible numbers of length `n`.
  3. For each number, check if it's strobogrammatic by comparing it with its rotated version.
- Why this approach comes to mind first: It's straightforward but inefficient due to the large number of possible combinations to check.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

std::unordered_map<char, char> strobogrammaticMap = {
    {'0', '0'},
    {'1', '1'},
    {'6', '9'},
    {'8', '8'},
    {'9', '6'}
};

std::vector<std::string> generateStrobogrammatic(int n) {
    std::vector<std::string> result;
    for (int i = 0; i < pow(10, n); i++) {
        std::string num = std::to_string(i);
        // Pad with leading zeros if necessary
        while (num.length() < n) num = "0" + num;
        
        bool isStrobogrammatic = true;
        for (int j = 0; j < num.length(); j++) {
            if (strobogrammaticMap.find(num[j]) == strobogrammaticMap.end() ||
                strobogrammaticMap[num[j]] != num[num.length() - 1 - j]) {
                isStrobogrammatic = false;
                break;
            }
        }
        
        if (isStrobogrammatic) result.push_back(num);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^n \cdot n)$ because for each of the $10^n$ numbers, we perform a check that takes $O(n)$ time.
> - **Space Complexity:** $O(10^n \cdot n)$ for storing the result, assuming in the worst case, all numbers are strobogrammatic.
> - **Why these complexities occur:** The brute force approach checks every possible number, leading to exponential time complexity, and stores all strobogrammatic numbers, resulting in exponential space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all numbers, generate strobogrammatic numbers directly using the mapping of strobogrammatic digits. This can be achieved through a recursive or iterative approach, building numbers from the center outwards.
- Detailed breakdown of the approach:
  1. Start with the base case for `n = 1`.
  2. For `n > 1`, consider the first and last digits, and then recursively generate the middle part.
- Proof of optimality: This approach generates all strobogrammatic numbers without checking unnecessary candidates, thus it's more efficient than the brute force approach.

```cpp
std::vector<std::string> generateStrobogrammatic(int n) {
    std::vector<std::string> result;
    std::vector<std::pair<char, char>> pairs = {{'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};
    
    std::function<void(int, int, std::string&)> dfs = [&](int left, int right, std::string& s) {
        if (left > right) {
            result.push_back(s);
            return;
        }
        
        for (auto& pair : pairs) {
            if (left == right && (pair.first == '6' || pair.first == '9')) continue;
            if (left == n - 1 && right == n - 1 && (pair.first == '0')) continue;
            
            s[left] = pair.first;
            s[right] = pair.second;
            dfs(left + 1, right - 1, s);
        }
    };
    
    if (n % 2 == 0) {
        std::string s(n, ' ');
        dfs(0, n - 1, s);
    } else {
        std::string s(n, ' ');
        dfs(0, n - 1, s);
        std::string s2(n, ' ');
        s2[n / 2] = '0';
        dfs(0, n - 1, s2);
        s2[n / 2] = '1';
        dfs(0, n - 1, s2);
        s2[n / 2] = '8';
        dfs(0, n - 1, s2);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(5^{n/2})$ for even `n` and $O(3 \cdot 5^{(n-1)/2})$ for odd `n`, because we have 5 choices for each pair of digits in the first half of the number, and for odd `n`, we have 3 choices for the middle digit.
> - **Space Complexity:** $O(5^{n/2})$ for storing the result, as in the worst case, we might generate up to $5^{n/2}$ strobogrammatic numbers for even `n`.
> - **Optimality proof:** This approach is optimal because it directly generates all strobogrammatic numbers without unnecessary checks, thus minimizing both time and space complexities.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive generation, backtracking, and direct construction of solutions based on specific rules (strobogrammatic mapping).
- Problem-solving patterns identified: Breaking down problems into smaller sub-problems (recursion) and using pre-defined mappings or rules to generate solutions directly.
- Optimization techniques learned: Avoiding brute force by directly generating solutions, using recursion or iteration to build up solutions from smaller parts.
- Similar problems to practice: Other problems involving generation of numbers or strings based on specific rules or mappings.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases (e.g., `n = 1`), forgetting to include all possible strobogrammatic digits in the mapping.
- Edge cases to watch for: Handling of `0` as a first digit, ensuring that the middle digit for odd `n` is correctly handled.
- Performance pitfalls: Using brute force approaches for large `n`, not optimizing the generation process by directly constructing strobogrammatic numbers.
- Testing considerations: Thoroughly testing with different values of `n`, including edge cases like `n = 1` and ensuring the output matches the expected list of strobogrammatic numbers.