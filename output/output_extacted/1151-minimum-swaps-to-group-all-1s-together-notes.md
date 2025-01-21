## Minimum Swaps to Group All 1s Together

**Problem Link:** https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/description

**Problem Statement:**
- Input: A binary array `nums` of size `n`.
- Constraints: $1 \leq n \leq 10^5$.
- Expected Output: The minimum number of swaps to group all 1s together.
- Key Requirements: The goal is to find the minimum number of swaps required to group all 1s together in the array.
- Edge Cases: If the array is empty or contains only 0s, the function should return 0.

**Example Test Cases:**
- Example 1: Input: `nums = [1,0,1,0,1]`, Output: `1`. Explanation: We can swap the second 0 and the third 1 to get `nums = [1,1,0,0,1]`.
- Example 2: Input: `nums = [0]`, Output: `0`. Explanation: The array already contains all 1s together (there are no 1s).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of swaps to group the 1s together.
- Step-by-step breakdown:
  1. Generate all possible permutations of the array.
  2. For each permutation, check if all 1s are grouped together.
  3. If they are, count the number of swaps required to reach this permutation from the original array.
  4. Keep track of the minimum number of swaps found so far.
- This approach comes to mind first because it guarantees finding the optimal solution, but it is inefficient due to its exponential time complexity.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minSwaps(vector<int>& nums) {
    int n = nums.size();
    int min_swaps = n;
    
    // Generate all permutations of the array
    do {
        bool grouped = true;
        int ones = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                ones++;
            } else if (ones > 0) {
                grouped = false;
                break;
            }
        }
        
        if (grouped) {
            // Count the number of swaps required to reach this permutation
            int swaps = 0;
            vector<int> original = nums;
            for (int i = 0; i < n; i++) {
                if (nums[i] != original[i]) {
                    swaps++;
                }
            }
            min_swaps = min(min_swaps, swaps);
        }
    } while (next_permutation(nums.begin(), nums.end()));
    
    return min_swaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the size of the array. This is because we generate all permutations of the array and for each permutation, we check if all 1s are grouped together.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum number of swaps and the current permutation.
> - **Why these complexities occur:** The time complexity is high because generating all permutations of the array takes $n!$ time, and for each permutation, we perform a linear scan to check if all 1s are grouped together.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a sliding window approach to find the minimum number of swaps required to group all 1s together.
- Step-by-step breakdown:
  1. Calculate the total number of 1s in the array.
  2. Initialize a sliding window of size equal to the total number of 1s.
  3. Slide the window over the array, and for each position, count the number of 0s inside the window.
  4. The minimum number of swaps required is the minimum number of 0s found in any window position.
- This approach is optimal because it only requires a single pass over the array, resulting in a linear time complexity.

```cpp
int minSwaps(vector<int>& nums) {
    int n = nums.size();
    int ones = 0;
    for (int num : nums) {
        if (num == 1) {
            ones++;
        }
    }
    
    if (ones == 0) {
        return 0;
    }
    
    int min_swaps = n;
    int window_ones = 0;
    for (int i = 0; i < ones; i++) {
        if (nums[i] == 1) {
            window_ones++;
        }
    }
    
    int zeros = ones - window_ones;
    min_swaps = zeros;
    
    for (int i = ones; i < n; i++) {
        if (nums[i] == 1) {
            window_ones++;
        }
        if (nums[i - ones] == 1) {
            window_ones--;
        }
        zeros = ones - window_ones;
        min_swaps = min(min_swaps, zeros);
    }
    
    return min_swaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the array. This is because we only need to make a single pass over the array to find the minimum number of swaps.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum number of swaps and the window boundaries.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the array, resulting in a linear time complexity. The sliding window approach allows us to efficiently find the minimum number of swaps required to group all 1s together.