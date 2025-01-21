## Numbers With Same Consecutive Differences

**Problem Link:** https://leetcode.com/problems/numbers-with-same-consecutive-differences/description

**Problem Statement:**
- Input format: Given two integers `n` and `k`, where `1 <= n <= 9` and `0 <= k <= 9`.
- Constraints: The task is to find all `n`-digit numbers with the property that the difference between any two consecutive digits is `k`.
- Expected output format: Return an array of integers in ascending order.
- Key requirements and edge cases to consider: Ensure the solution handles cases where `n` is 1 and `k` is 0, as well as when `n` is greater than 1 and `k` can vary from 0 to 9.
- Example test cases with explanations:
  - Example 1: For `n = 3` and `k = 7`, the output should be `[181,292,383,484,585,686,787,888,979]`.
  - Example 2: For `n = 2` and `k = 1`, the output should be `[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible `n`-digit numbers and check each one to see if the difference between any two consecutive digits is `k`.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the numbers that meet the condition.
  2. Generate all possible `n`-digit numbers.
  3. For each number, convert it into a list of digits.
  4. Check if the difference between any two consecutive digits is `k`.
  5. If the condition is met, add the number to the list.
- Why this approach comes to mind first: It's a straightforward method to solve the problem by checking all possibilities.

```cpp
#include <iostream>
#include <vector>

std::vector<int> numsSameConsecDiff(int n, int k) {
    std::vector<int> result;
    for (int i = 1; i <= 9; i++) {
        std::vector<int> path = {i};
        dfs(n - 1, k, path, result);
    }
    return result;
}

void dfs(int n, int k, std::vector<int>& path, std::vector<int>& result) {
    if (n == 0) {
        int num = 0;
        for (int digit : path) {
            num = num * 10 + digit;
        }
        result.push_back(num);
        return;
    }
    int last = path.back();
    if (last + k <= 9) {
        path.push_back(last + k);
        dfs(n - 1, k, path, result);
        path.pop_back();
    }
    if (k != 0 && last - k >= 0) {
        path.push_back(last - k);
        dfs(n - 1, k, path, result);
        path.pop_back();
    }
}

int main() {
    int n = 3;
    int k = 7;
    std::vector<int> result = numsSameConsecDiff(n, k);
    for (int num : result) {
        std::cout << num << " ";
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^n)$, where `n` is the number of digits. This is because in the worst case, we generate all possible `n`-digit numbers.
> - **Space Complexity:** $O(10^n)$, for storing the generated numbers.
> - **Why these complexities occur:** The brute force approach checks all possible numbers, leading to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible numbers and checking them, we can use a depth-first search (DFS) approach to construct the numbers that meet the condition.
- Detailed breakdown of the approach:
  1. Start with each digit from 1 to 9.
  2. Use DFS to construct `n`-digit numbers by appending the next digit that is `k` more or less than the current digit.
  3. If the next digit is out of range (less than 0 or greater than 9), skip it.
- Proof of optimality: This approach is optimal because it only generates the numbers that meet the condition, avoiding unnecessary checks.

```cpp
#include <iostream>
#include <vector>

std::vector<int> numsSameConsecDiff(int n, int k) {
    std::vector<int> result;
    for (int i = 1; i <= 9; i++) {
        std::vector<int> path = {i};
        dfs(n - 1, k, path, result);
    }
    return result;
}

void dfs(int n, int k, std::vector<int>& path, std::vector<int>& result) {
    if (n == 0) {
        int num = 0;
        for (int digit : path) {
            num = num * 10 + digit;
        }
        result.push_back(num);
        return;
    }
    int last = path.back();
    if (last + k <= 9) {
        path.push_back(last + k);
        dfs(n - 1, k, path, result);
        path.pop_back();
    }
    if (k != 0 && last - k >= 0) {
        path.push_back(last - k);
        dfs(n - 1, k, path, result);
        path.pop_back();
    }
}

int main() {
    int n = 3;
    int k = 7;
    std::vector<int> result = numsSameConsecDiff(n, k);
    for (int num : result) {
        std::cout << num << " ";
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where `n` is the number of digits. This is because in the worst case, we have two branches for each digit (either `k` more or `k` less).
> - **Space Complexity:** $O(n)$, for the recursion stack.
> - **Optimality proof:** This approach is optimal because it only generates the numbers that meet the condition, avoiding unnecessary checks.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) and recursion.
- Problem-solving patterns identified: Constructing numbers that meet a specific condition using DFS.
- Optimization techniques learned: Avoiding unnecessary checks by constructing numbers that meet the condition directly.
- Similar problems to practice: Other problems that involve constructing numbers or sequences with specific properties.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly (e.g., when `n` is 1 or `k` is 0).
- Edge cases to watch for: When `n` is greater than 1 and `k` can vary from 0 to 9.
- Performance pitfalls: Using a brute force approach that checks all possible numbers, leading to exponential time complexity.
- Testing considerations: Ensure that the solution handles all possible inputs and edge cases correctly.