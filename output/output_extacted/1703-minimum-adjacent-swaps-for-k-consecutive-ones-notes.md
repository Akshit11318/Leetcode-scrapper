## Minimum Adjacent Swaps for K Consecutive Ones

**Problem Link:** https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/description

**Problem Statement:**
- Given an array `nums` of integers and an integer `k`, find the minimum number of adjacent swaps required to have `k` consecutive ones.
- Input format: `nums` array and integer `k`.
- Expected output: Minimum number of adjacent swaps.
- Key requirements: The input array may contain zeros and ones, and `k` is a positive integer.
- Edge cases: Handle cases where `k` is greater than the number of ones in the array or when the array is empty.

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible swaps and count the minimum number of swaps required to get `k` consecutive ones.
- Step-by-step breakdown:
  1. Generate all permutations of the input array.
  2. For each permutation, check if there are `k` consecutive ones.
  3. If `k` consecutive ones are found, count the number of swaps required to achieve this permutation from the original array.
  4. Keep track of the minimum number of swaps across all permutations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minSwaps(vector<int>& nums, int k) {
    int n = nums.size();
    int min_swaps = INT_MAX;

    // Generate all permutations
    do {
        int swaps = 0;
        vector<int> temp = nums;

        // Check if k consecutive ones
        bool found = false;
        for (int i = 0; i <= n - k; i++) {
            bool consecutive_ones = true;
            for (int j = i; j < i + k; j++) {
                if (temp[j] != 1) {
                    consecutive_ones = false;
                    break;
                }
            }
            if (consecutive_ones) {
                found = true;
                break;
            }
        }

        if (found) {
            // Count swaps required for this permutation
            for (int i = 0; i < n; i++) {
                if (nums[i] != temp[i]) {
                    swaps++;
                    // Swap elements to match the permutation
                    for (int j = i + 1; j < n; j++) {
                        if (nums[j] == temp[i]) {
                            swap(nums[i], nums[j]);
                            break;
                        }
                    }
                }
            }
            min_swaps = min(min_swaps, swaps);
        }
    } while (next_permutation(nums.begin(), nums.end()));

    return min_swaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the size of the input array, due to generating all permutations and checking for `k` consecutive ones in each permutation.
> - **Space Complexity:** $O(1)$, excluding the space required for the input and output, as we only use a constant amount of space to store the minimum number of swaps and the current permutation.
> - **Why these complexities occur:** The brute force approach involves generating all permutations of the input array, which results in a factorial time complexity. The space complexity is constant because we only use a fixed amount of space to store the minimum number of swaps and the current permutation.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach to find `k` consecutive ones and then calculate the minimum number of swaps required to achieve this.
- Detailed breakdown:
  1. Initialize two pointers, `left` and `right`, to represent the sliding window.
  2. Move the `right` pointer to the right until we have `k` ones in the window.
  3. Calculate the number of swaps required to move the ones to the left of the window to the right of the window.
  4. Move the `left` pointer to the right and repeat steps 2-3 until the `right` pointer reaches the end of the array.
  5. Keep track of the minimum number of swaps across all window positions.

```cpp
int minSwaps(vector<int>& nums, int k) {
    int n = nums.size();
    int min_swaps = INT_MAX;

    for (int i = 0; i <= n - k; i++) {
        int ones = 0;
        int swaps = 0;

        for (int j = i; j < i + k; j++) {
            if (nums[j] == 1) {
                ones++;
            } else {
                swaps++;
            }
        }

        if (ones == k) {
            min_swaps = min(min_swaps, swaps);
        }
    }

    return min_swaps == INT_MAX ? -1 : min_swaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of the input array, due to iterating over the array and checking for `k` consecutive ones in each window position.
> - **Space Complexity:** $O(1)$, excluding the space required for the input and output, as we only use a constant amount of space to store the minimum number of swaps and the current window position.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the input array and uses a constant amount of space. The time complexity is linear with respect to the size of the input array, making it efficient for large inputs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, permutation generation, and swap counting.
- Problem-solving patterns identified: Using a sliding window to find consecutive elements and calculating the minimum number of swaps required to achieve a desired arrangement.
- Optimization techniques learned: Avoiding unnecessary swaps and using a constant amount of space to store intermediate results.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly counting swaps or failing to handle edge cases.
- Edge cases to watch for: Empty input array, `k` greater than the number of ones in the array, or `k` equal to zero.
- Performance pitfalls: Using a brute force approach with a high time complexity or failing to optimize the swap counting process.
- Testing considerations: Thoroughly testing the implementation with various input scenarios, including edge cases and large inputs.