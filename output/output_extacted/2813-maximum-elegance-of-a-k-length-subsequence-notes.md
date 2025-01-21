## Maximum Elegance of a K-Length Subsequence

**Problem Link:** https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `items` and an integer `k`, find the maximum elegance of a `k`-length subsequence. The elegance of a subsequence is the sum of the products of each pair of elements in the subsequence.
- Expected output format: The maximum elegance of a `k`-length subsequence.
- Key requirements and edge cases to consider: 
    - The subsequence must have exactly `k` elements.
    - The elegance is calculated by summing the products of each pair of elements in the subsequence.
- Example test cases with explanations:
    - For `items = [1, 2, 3]` and `k = 2`, the maximum elegance is `2 * 3 = 6`.
    - For `items = [1, 2, 3, 4]` and `k = 3`, the maximum elegance is `1 * 2 + 1 * 3 + 1 * 4 + 2 * 3 + 2 * 4 + 3 * 4 = 35`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible `k`-length subsequences of the given array and calculate the elegance of each subsequence.
- Step-by-step breakdown of the solution:
    1. Generate all possible `k`-length subsequences of the given array.
    2. For each subsequence, calculate the elegance by summing the products of each pair of elements.
    3. Keep track of the maximum elegance found so far.
- Why this approach comes to mind first: It is a straightforward approach that involves generating all possible subsequences and calculating their elegance.

```cpp
#include <vector>
#include <algorithm>

int maximumElegance(std::vector<int>& items, int k) {
    int n = items.size();
    int maxElegance = 0;

    // Generate all possible k-length subsequences
    std::vector<bool> mask(n);
    std::fill(mask.begin(), mask.begin() + k, true);

    do {
        int elegance = 0;
        for (int i = 0; i < n; i++) {
            if (mask[i]) {
                for (int j = i + 1; j < n; j++) {
                    if (mask[j]) {
                        elegance += items[i] * items[j];
                    }
                }
            }
        }
        maxElegance = std::max(maxElegance, elegance);
    } while (std::prev_permutation(mask.begin(), mask.end()));

    return maxElegance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O\left({n \choose k} \cdot k^2\right)$, where $n$ is the length of the input array and $k$ is the length of the subsequence. This is because we generate all possible `k`-length subsequences and calculate the elegance of each subsequence in $O(k^2)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we use a boolean mask of size $n$ to generate all possible subsequences.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible subsequences and calculate their elegance. The space complexity occurs because we use a boolean mask to generate all possible subsequences.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a bitmask to generate all possible `k`-length subsequences and calculate their elegance.
- Detailed breakdown of the approach:
    1. Initialize a bitmask of size $n$, where $n$ is the length of the input array.
    2. Iterate over all possible bitmasks of length $n$ and count the number of bits set to 1.
    3. If the number of bits set to 1 is equal to $k$, calculate the elegance of the corresponding subsequence.
    4. Keep track of the maximum elegance found so far.
- Proof of optimality: This approach is optimal because it generates all possible `k`-length subsequences and calculates their elegance in $O(k^2)$ time.

```cpp
#include <vector>

int maximumElegance(std::vector<int>& items, int k) {
    int n = items.size();
    int maxElegance = 0;

    // Generate all possible k-length subsequences using bitmask
    for (int mask = 0; mask < (1 << n); mask++) {
        int elegance = 0;
        int count = 0;

        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                count++;
                for (int j = i + 1; j < n; j++) {
                    if ((mask & (1 << j)) != 0) {
                        elegance += items[i] * items[j];
                    }
                }
            }
        }

        if (count == k) {
            maxElegance = std::max(maxElegance, elegance);
        }
    }

    return maxElegance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O\left(2^n \cdot k^2\right)$, where $n$ is the length of the input array and $k$ is the length of the subsequence. This is because we generate all possible `k`-length subsequences using a bitmask and calculate their elegance in $O(k^2)$ time.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input array. This is because we use a constant amount of space to store the bitmask and the elegance of the subsequence.
> - **Optimality proof:** This approach is optimal because it generates all possible `k`-length subsequences and calculates their elegance in $O(k^2)$ time. The time complexity is dominated by the number of possible subsequences, which is $O(2^n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitmask, subsequence generation, elegance calculation.
- Problem-solving patterns identified: Generating all possible subsequences, calculating their elegance, and keeping track of the maximum elegance.
- Optimization techniques learned: Using a bitmask to generate all possible subsequences, calculating elegance in $O(k^2)$ time.
- Similar problems to practice: Generating all possible subsequences, calculating their sum or product, and keeping track of the maximum or minimum value.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the bitmask correctly, not counting the number of bits set to 1 correctly, not calculating the elegance correctly.
- Edge cases to watch for: When the input array is empty, when $k$ is 0, when $k$ is equal to the length of the input array.
- Performance pitfalls: Not using a bitmask to generate all possible subsequences, not calculating elegance in $O(k^2)$ time.
- Testing considerations: Testing the function with different input arrays and values of $k$, testing the function with edge cases.