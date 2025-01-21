## Remove K Digits
**Problem Link:** https://leetcode.com/problems/remove-k-digits/description

**Problem Statement:**
- Input: A non-negative integer `num` represented as a string and an integer `k`.
- Constraints: `1 <= num.length <= 20000`, `0 <= k <= num.length`, `num` consists of only digits, and `k` is an integer.
- Expected Output: The string representation of the smallest possible integer after removing `k` digits from `num`.
- Key Requirements: 
    - Remove exactly `k` digits from `num`.
    - After removal, the resulting string should be the smallest possible integer.
    - Leading zeros are not allowed in the result.
- Edge Cases: 
    - If `k` is equal to the length of `num`, the result should be `"0"`.
    - If `num` consists of all identical digits and `k` is less than the length of `num`, the result should be the first `num.length - k` digits.

Example Test Cases:
- Input: `num = "1432219", k = 3`
  Output: `"1219"`
- Input: `num = "10200", k = 1`
  Output: `"2000"`
- Input: `num = "10", k = 2`
  Output: `"0"`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of removing `k` digits from `num` and then compare the results to find the smallest possible integer.
- However, this approach is impractical due to its high computational complexity.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

void removeKDigitsBruteForce(std::string num, int k) {
    int n = num.size();
    std::vector<std::string> results;
    
    // Function to generate all permutations
    void generatePermutations(std::string current, int depth) {
        if (depth == n - k) {
            results.push_back(current);
            return;
        }
        for (int i = 0; i < n; ++i) {
            if (current.find(num[i]) != std::string::npos) continue;
            current += num[i];
            generatePermutations(current, depth + 1);
            current.pop_back();
        }
    }
    
    generatePermutations("", 0);
    
    // Find the smallest integer
    std::string smallest = "9999999999999999999";
    for (const auto& result : results) {
        if (result < smallest) smallest = result;
    }
    
    std::cout << smallest << std::endl;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! / (n-k)!)$. This is due to generating all permutations of `n` items taken `n-k` at a time.
> - **Space Complexity:** $O(n! / (n-k)!)$. This is for storing all permutations.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of removing `k` digits, which leads to factorial complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a **stack** to keep track of the digits that will form the smallest possible integer.
- We iterate through `num` and push each digit onto the stack. If the stack is not empty and the top of the stack is greater than the current digit, and we have removals left (`k > 0`), we pop the stack until it's empty or the top of the stack is less than or equal to the current digit, or we've used up all our removals.
- After iterating through all digits, if we still have removals left, we remove the remaining top digits from the stack.
- Finally, we construct the result by popping all digits from the stack and appending them to the result string, skipping any leading zeros.

```cpp
#include <iostream>
#include <string>

std::string removeKDigits(std::string num, int k) {
    std::string stack;
    for (char c : num) {
        while (k > 0 && !stack.empty() && stack.back() > c) {
            stack.pop_back();
            k--;
        }
        stack += c;
    }
    
    // Remove remaining top digits if k > 0
    if (k > 0) {
        stack.resize(stack.size() - k);
    }
    
    // Remove leading zeros
    size_t start = 0;
    while (start < stack.size() && stack[start] == '0') start++;
    if (start == stack.size()) return "0";
    return stack.substr(start);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$. We iterate through `num` once.
> - **Space Complexity:** $O(n)$. In the worst case, we might need to store all digits in the stack.
> - **Optimality proof:** This approach ensures the smallest possible integer by always removing the largest possible digit when given the choice, thus minimizing the resulting number.

---

### Final Notes

**Learning Points:**
- **Stack operations:** Using a stack to efficiently manage the digits of the resulting number.
- **Greedy algorithm:** Applying a greedy strategy to always remove the largest possible digit when given the choice.
- **String manipulation:** Efficiently constructing and manipulating strings in C++.

**Mistakes to Avoid:**
- Not considering the case where `k` is equal to the length of `num`.
- Not properly handling leading zeros in the result.
- Not optimizing the removal process, leading to inefficient solutions.