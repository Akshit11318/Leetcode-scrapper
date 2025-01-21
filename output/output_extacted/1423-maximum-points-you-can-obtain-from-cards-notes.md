## Maximum Points You Can Obtain From Cards

**Problem Link:** https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description

**Problem Statement:**
- Input: An array of integers `cards` of size `2n`, and an integer `k`.
- Constraints: `1 <= n <= 10^4`, `1 <= k <= n`.
- Expected Output: The maximum points that can be obtained from `k` cards.
- Key Requirements: The goal is to find the maximum sum of `k` cards that can be obtained from the array, considering the constraint that the first `i` cards and the last `i` cards cannot be taken at the same time for any `i`.
- Example Test Cases:
  - Input: `cards = [1, 2, 3, 4, 5, 6, 1], k = 3`
  - Output: `12`
  - Explanation: Take the first three cards, which are `[1, 2, 3]`, and their sum is `6`. Alternatively, take the last three cards, which are `[5, 6, 1]`, and their sum is `12`. The maximum sum is `12`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible combinations of `k` cards from the array and calculating their sums.
- This approach considers all possible subsets of the array of size `k` and calculates the sum of each subset.
- The maximum sum found among all subsets is the answer.

```cpp
class Solution {
public:
    int maxScore(vector<int>& cards, int k) {
        int n = cards.size();
        int maxSum = 0;
        
        // Generate all possible subsets of size k
        for (int mask = 0; mask < (1 << n); mask++) {
            if (__builtin_popcount(mask) == k) {
                int sum = 0;
                for (int i = 0; i < n; i++) {
                    if ((mask & (1 << i)) != 0) {
                        sum += cards[i];
                    }
                }
                // Check if the subset does not contain both the first and last i cards for any i
                bool valid = true;
                for (int i = 1; i <= k; i++) {
                    if ((mask & (1 << (i - 1))) != 0 && (mask & (1 << (n - i))) != 0) {
                        valid = false;
                        break;
                    }
                }
                if (valid) {
                    maxSum = max(maxSum, sum);
                }
            }
        }
        return maxSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the `cards` array. This is because we generate all possible subsets of the array and check each subset.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, since we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is high because we generate all possible subsets of the array, and for each subset, we calculate its sum and check its validity.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal solution involves using a sliding window approach to find the maximum sum of `k` cards.
- We consider the array as a circular array and use two pointers to represent the start and end of the window.
- We calculate the sum of the cards in the window and update the maximum sum if the current sum is larger.

```cpp
class Solution {
public:
    int maxScore(vector<int>& cards, int k) {
        int n = cards.size();
        int maxSum = 0;
        
        // Calculate the total sum of the array
        int totalSum = 0;
        for (int i = 0; i < n; i++) {
            totalSum += cards[i];
        }
        
        // Calculate the minimum sum of (n - k) cards
        int minSum = INT_MAX;
        int windowSum = 0;
        for (int i = 0; i < n - k; i++) {
            windowSum += cards[i];
        }
        minSum = min(minSum, windowSum);
        
        // Slide the window to the right
        for (int i = n - k; i < n; i++) {
            windowSum = windowSum - cards[i - (n - k)] + cards[i];
            minSum = min(minSum, windowSum);
        }
        
        // Calculate the maximum sum of k cards
        maxSum = totalSum - minSum;
        
        return maxSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the `cards` array. This is because we make a single pass through the array to calculate the total sum and the minimum sum of `(n - k)` cards.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, since we only use a constant amount of space.
> - **Optimality proof:** This solution is optimal because it uses a single pass through the array to calculate the maximum sum of `k` cards, and it avoids the need to generate all possible subsets of the array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sliding window approach, dynamic programming.
- Problem-solving patterns identified: finding the maximum sum of a subarray, using a sliding window to reduce the search space.
- Optimization techniques learned: avoiding the generation of all possible subsets, using a single pass through the array to calculate the maximum sum.
- Similar problems to practice: finding the maximum sum of a subarray with a given size, finding the minimum sum of a subarray with a given size.

**Mistakes to Avoid:**
- Common implementation errors: not checking the validity of the subset, not updating the maximum sum correctly.
- Edge cases to watch for: handling the case where `k` is equal to `n`, handling the case where the array is empty.
- Performance pitfalls: generating all possible subsets of the array, using a brute force approach to find the maximum sum.
- Testing considerations: testing the solution with different input sizes, testing the solution with different values of `k`.