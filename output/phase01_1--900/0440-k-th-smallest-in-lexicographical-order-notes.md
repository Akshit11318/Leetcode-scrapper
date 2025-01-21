## K-th Smallest in Lexicographical Order
**Problem Link:** https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description

**Problem Statement:**
- Input format: `int n` and `int k` where `n` is the upper limit of the numbers and `k` is the k-th smallest number to find.
- Constraints: `1 <= k <= n <= 2 * 10^4`.
- Expected output format: The k-th smallest number in lexicographical order.
- Key requirements and edge cases to consider: Handling large inputs and ensuring lexicographical order.
- Example test cases with explanations:
  - For `n = 13` and `k = 2`, the output should be `10` because the lexicographical order is `[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]`.
  - For `n = 1` and `k = 1`, the output should be `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all numbers from `1` to `n`, sort them in lexicographical order, and then select the k-th number.
- Step-by-step breakdown of the solution:
  1. Create a vector to store all numbers from `1` to `n`.
  2. Convert each number to a string to facilitate lexicographical sorting.
  3. Sort the vector of strings.
  4. Select the k-th string and convert it back to an integer.
- Why this approach comes to mind first: It directly addresses the requirement for lexicographical order but is inefficient for large inputs.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

int findKthNumber(int n, int k) {
    std::vector<std::string> numbers;
    for (int i = 1; i <= n; i++) {
        numbers.push_back(std::to_string(i));
    }
    std::sort(numbers.begin(), numbers.end());
    return std::stoi(numbers[k - 1]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting `n` elements.
> - **Space Complexity:** $O(n)$ for storing all numbers as strings.
> - **Why these complexities occur:** The brute force approach involves generating all numbers, sorting them, which leads to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize the fact that the numbers are in lexicographical order and use a prefix-based approach to efficiently calculate the k-th smallest number.
- Detailed breakdown of the approach:
  1. Initialize a variable `cur` to `1`, representing the current number being considered.
  2. Calculate the number of nodes in the current prefix by considering the number of digits and the range of numbers that can be appended to the current prefix.
  3. If `k` is less than or equal to the number of nodes in the current prefix, move into the current prefix.
  4. Otherwise, subtract the number of nodes in the current prefix from `k` and move to the next prefix.
  5. Repeat steps 2-4 until `k` becomes `1`, indicating the k-th smallest number has been found.
- Proof of optimality: This approach avoids generating all numbers and instead calculates the k-th smallest number directly, reducing the time complexity significantly.

```cpp
int findKthNumber(int n, int k) {
    long long cur = 1;
    k--;
    while (k > 0) {
        long long step = 0, first = cur, last = cur + 1;
        while (first <= n) {
            step += std::min(n + 1, last) - first;
            first *= 10;
            last *= 10;
        }
        if (k < step) {
            k--;
            cur *= 10;
        } else {
            k -= step;
            cur++;
        }
    }
    return cur;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n + \log k)$ due to the while loop and the calculation of the number of nodes in each prefix.
> - **Space Complexity:** $O(1)$ as only a constant amount of space is used.
> - **Optimality proof:** This approach directly calculates the k-th smallest number without generating all numbers, achieving the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix-based approach, lexicographical sorting, and efficient calculation of the k-th smallest number.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (calculating the number of nodes in each prefix) and using a loop to iteratively refine the solution.
- Optimization techniques learned: Avoiding unnecessary computations by directly calculating the k-th smallest number.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect calculation of the number of nodes in each prefix or incorrect handling of edge cases.
- Edge cases to watch for: Handling large inputs and ensuring the correct calculation of the k-th smallest number.
- Performance pitfalls: Using the brute force approach for large inputs, which can lead to significant performance issues.