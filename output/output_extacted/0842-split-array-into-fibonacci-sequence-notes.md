## Split Array into Fibonacci Sequence

**Problem Link:** https://leetcode.com/problems/split-array-into-fibonacci-sequence/description

**Problem Statement:**
- Input: A string `S` consisting of digits.
- Constraints: `1 <= S.length <= 10^5`, `S` consists only of digits.
- Expected Output: Return all possible split results of `S` into a list of non-negative integers that represent a valid Fibonacci sequence.
- Key Requirements: 
  - A valid Fibonacci sequence must start with a sequence of two non-negative integers.
  - Each subsequent number must be the sum of the previous two.
  - The sequence should not include any leading zeros, unless the number is 0.
- Edge Cases:
  - If no such sequence exists, return an empty list.
- Example Test Cases:
  - Input: `S = "123456579"`, Output: `[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]`
  - Input: `S = "11235813"`, Output: `[1, 1, 2, 3, 5, 8, 13]`
  - Input: `S = "0123"`, Output: `[]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible splits of the string `S` and checking if each split forms a valid Fibonacci sequence.
- Step-by-step breakdown:
  1. Generate all possible splits of the string `S`.
  2. For each split, check if it forms a valid Fibonacci sequence.
  3. If a valid sequence is found, add it to the result list.
- Why this approach comes to mind first: It's a straightforward approach that involves checking all possibilities, which is often the first line of thinking when dealing with combinatorial problems.

```cpp
#include <iostream>
#include <vector>
#include <string>

void backtrack(const std::string& s, int start, std::vector<long long> path, std::vector<std::vector<long long>>& result) {
    if (start == s.size()) {
        if (path.size() >= 3) {
            result.push_back(path);
        }
        return;
    }

    for (int i = start; i < s.size(); ++i) {
        std::string substr = s.substr(start, i - start + 1);
        if (substr[0] == '0' && substr.size() > 1) {
            break;
        }
        long long num = std::stoll(substr);
        if (path.size() < 2 || num == path[path.size() - 1] + path[path.size() - 2]) {
            path.push_back(num);
            backtrack(s, i + 1, path, result);
            path.pop_back();
        }
    }
}

std::vector<std::vector<long long>> splitIntoFibonacci(const std::string& S) {
    std::vector<std::vector<long long>> result;
    std::vector<long long> path;
    backtrack(S, 0, path, result);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the string `S`. This is because in the worst case, we generate all possible splits of the string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `S`. This is because we need to store the current path and the result.
> - **Why these complexities occur:** The high time complexity occurs because we are generating all possible splits and checking each one, which leads to exponential time complexity. The space complexity is linear because we only need to store the current path and the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all possible splits and checking each one, we can use a more targeted approach by iterating through the string and trying to form a Fibonacci sequence.
- Detailed breakdown:
  1. Start with the first two numbers in the sequence.
  2. Try to extend the sequence by finding the next number that is the sum of the previous two.
  3. If we can extend the sequence, continue until we reach the end of the string.
  4. If we cannot extend the sequence, backtrack and try a different split.
- Proof of optimality: This approach is optimal because it avoids generating unnecessary splits and only explores paths that could potentially lead to a valid Fibonacci sequence.

```cpp
#include <iostream>
#include <vector>
#include <string>

void backtrack(const std::string& s, int start, std::vector<long long> path, std::vector<std::vector<long long>>& result) {
    if (start == s.size() && path.size() >= 3) {
        result.push_back(path);
        return;
    }

    for (int i = start; i < s.size(); ++i) {
        std::string substr = s.substr(start, i - start + 1);
        if (substr[0] == '0' && substr.size() > 1) {
            break;
        }
        long long num = std::stoll(substr);
        if (path.size() < 2 || num == path[path.size() - 1] + path[path.size() - 2]) {
            if (num > INT_MAX) {
                break;
            }
            path.push_back(num);
            backtrack(s, i + 1, path, result);
            path.pop_back();
        }
    }
}

std::vector<std::vector<long long>> splitIntoFibonacci(const std::string& S) {
    std::vector<std::vector<long long>> result;
    std::vector<long long> path;
    backtrack(S, 0, path, result);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the string `S`. Although the time complexity appears the same as the brute force approach, the optimal approach is more efficient in practice because it prunes branches that cannot lead to a valid Fibonacci sequence.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `S`.
> - **Optimality proof:** This approach is optimal because it uses a targeted search strategy that avoids exploring unnecessary branches, making it more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, Fibonacci sequence generation.
- Problem-solving patterns identified: Using a targeted search strategy to prune branches that cannot lead to a solution.
- Optimization techniques learned: Avoiding unnecessary computations by pruning branches.
- Similar problems to practice: Other problems involving backtracking and sequence generation.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as leading zeros or overflow.
- Edge cases to watch for: Handling cases where the input string is empty or contains only one digit.
- Performance pitfalls: Not pruning branches that cannot lead to a solution, leading to exponential time complexity.
- Testing considerations: Testing the implementation with a variety of input strings, including edge cases.