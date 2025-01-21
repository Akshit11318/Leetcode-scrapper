## Find the K-th Lucky Number
**Problem Link:** https://leetcode.com/problems/find-the-k-th-lucky-number/description

**Problem Statement:**
- Input format: An integer `n` and an integer `k`.
- Constraints: `1 <= n <= 10^5`, `1 <= k <= n`.
- Expected output format: The k-th lucky number in the range `[1, n]`.
- Key requirements and edge cases to consider:
  - A lucky number is defined as a number that has at least one `7` in its digits.
  - We need to find the k-th lucky number in the range `[1, n]`.
- Example test cases with explanations:
  - For `n = 13` and `k = 2`, the output should be `7` because the first two lucky numbers in the range `[1, 13]` are `7` and `13`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the k-th lucky number, we can start by checking each number in the range `[1, n]` to see if it is lucky.
- Step-by-step breakdown of the solution:
  1. Iterate over the range `[1, n]`.
  2. For each number, check if it has at least one `7` in its digits.
  3. If a number is lucky, increment a counter.
  4. When the counter reaches `k`, return the current number as the k-th lucky number.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, but it may not be the most efficient.

```cpp
vector<int> luckyNumbers(int n) {
    vector<int> lucky;
    for (int i = 1; i <= n; i++) {
        string numStr = to_string(i);
        bool isLucky = false;
        for (char c : numStr) {
            if (c == '7') {
                isLucky = true;
                break;
            }
        }
        if (isLucky) {
            lucky.push_back(i);
        }
    }
    return lucky;
}

int findKthLucky(int n, int k) {
    vector<int> lucky = luckyNumbers(n);
    if (k > lucky.size()) {
        return -1; // or throw an exception
    }
    return lucky[k - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $m$ is the maximum number of digits in a number in the range `[1, n]`. This is because for each number, we are checking each digit.
> - **Space Complexity:** $O(n)$, as we are storing all lucky numbers in a vector.
> - **Why these complexities occur:** The time complexity is due to the iteration over all numbers and their digits, and the space complexity is due to storing all lucky numbers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing all lucky numbers and then finding the k-th one, we can stop as soon as we find the k-th lucky number.
- Detailed breakdown of the approach:
  1. Initialize a counter for lucky numbers.
  2. Iterate over the range `[1, n]`.
  3. For each number, check if it is lucky.
  4. If a number is lucky, increment the counter.
  5. When the counter reaches `k`, return the current number as the k-th lucky number.
- Why further optimization is impossible: This approach has the best possible time complexity because we must check each number at least once to determine if it is lucky.

```cpp
int findKthLucky(int n, int k) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        string numStr = to_string(i);
        bool isLucky = false;
        for (char c : numStr) {
            if (c == '7') {
                isLucky = true;
                break;
            }
        }
        if (isLucky) {
            count++;
            if (count == k) {
                return i;
            }
        }
    }
    return -1; // or throw an exception if k is larger than the number of lucky numbers
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $m$ is the maximum number of digits in a number in the range `[1, n]`. This is because for each number, we are checking each digit.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the counter and the current number.
> - **Optimality proof:** This approach is optimal because we must check each number at least once to determine if it is lucky, and we stop as soon as we find the k-th lucky number.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and optimization by stopping early.
- Problem-solving patterns identified: Checking each number in a range and stopping when a condition is met.
- Optimization techniques learned: Stopping the iteration as soon as the required number of lucky numbers is found.
- Similar problems to practice: Finding the k-th smallest/largest number in an array, finding the first/last occurrence of a number in a sorted array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases (e.g., `k` larger than the number of lucky numbers), not stopping the iteration early.
- Edge cases to watch for: `k` larger than the number of lucky numbers, `n` being very large.
- Performance pitfalls: Using unnecessary extra space, not stopping the iteration early.
- Testing considerations: Test with different values of `n` and `k`, including edge cases.