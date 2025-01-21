## Minimum Difference Between Largest and Smallest Value in Three Moves
**Problem Link:** https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5` and `1 <= nums[i] <= 10^9`.
- Expected Output: The minimum possible difference between the maximum and minimum values of `nums` after performing at most three moves.
- Key Requirements: A move consists of either adding or subtracting `1` from a number in the array.
- Edge Cases: Handling arrays with fewer than four elements, and ensuring the difference between the maximum and minimum values is minimized.

**Example Test Cases:**
- For `nums = [5,3,2,4]`, the output should be `0` because we can make all numbers equal to `3` by performing three moves.
- For `nums = [7,8,8,5]`, the output should be `1` because the minimum difference achievable is between `7` and `6` (or `8` and `7`) after at most three moves.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible combinations of adding or subtracting `1` from each number up to three times.
- This approach is straightforward but inefficient due to its exponential time complexity.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minDifference(vector<int>& nums) {
    int n = nums.size();
    int minDiff = INT_MAX;
    
    // Function to calculate difference after applying moves
    auto calculateDiff = [&](vector<int> nums, int movesLeft) {
        if (movesLeft == 0) {
            sort(nums.begin(), nums.end());
            return nums.back() - nums.front();
        }
        
        int minDiff = INT_MAX;
        for (int i = 0; i < n; ++i) {
            // Try adding 1
            nums[i] += 1;
            minDiff = min(minDiff, calculateDiff(nums, movesLeft - 1));
            nums[i] -= 1;
            
            // Try subtracting 1
            nums[i] -= 1;
            minDiff = min(minDiff, calculateDiff(nums, movesLeft - 1));
            nums[i] += 1;
        }
        return minDiff;
    };
    
    minDiff = calculateDiff(nums, 3);
    return minDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{3n})$ due to trying all possible combinations of moves on each number.
> - **Space Complexity:** $O(n)$ for the recursive call stack.
> - **Why these complexities occur:** The exponential time complexity arises from the brute force exploration of all possible move combinations, making this approach impractical for large inputs.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to realize that to minimize the difference between the maximum and minimum values, we should focus on the extreme values (the largest and smallest numbers) in the array.
- We will consider scenarios where we can reduce the largest number or increase the smallest number by applying the three moves.
- Sorting the array allows us to easily identify the largest and smallest values.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minDifference(vector<int>& nums) {
    int n = nums.size();
    if (n <= 4) {
        // For fewer than 4 elements, we can make all numbers equal
        return 0;
    }
    
    sort(nums.begin(), nums.end());
    
    // Calculate differences for all possible scenarios of applying moves
    vector<int> differences = {
        nums[n-1] - nums[0], // No moves
        nums[n-2] - nums[0], // One move on max
        nums[n-1] - nums[1], // One move on min
        nums[n-2] - nums[1], // One move on max and min
        nums[n-3] - nums[0], // Two moves on max
        nums[n-1] - nums[2], // Two moves on min
        nums[n-2] - nums[2], // One move on max, two on min
        nums[n-3] - nums[1]  // Two moves on max, one on min
    };
    
    // Find the minimum difference among all scenarios
    return *min_element(differences.begin(), differences.end());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the array.
> - **Space Complexity:** $O(1)$ if we consider the space used by the `differences` vector as constant, since its size does not depend on the input size `n`.
> - **Optimality proof:** This approach is optimal because it considers all relevant scenarios for minimizing the difference between the maximum and minimum values after at most three moves, without unnecessary exploration.

---

### Final Notes

**Learning Points:**
- **Sorting** can significantly simplify the problem by allowing easy access to the smallest and largest numbers.
- **Focusing on extreme values** is crucial for minimizing the difference between the maximum and minimum values.
- **Analyzing scenarios** helps in identifying the optimal strategy.

**Mistakes to Avoid:**
- Not considering the impact of the number of elements in the array on the possible moves.
- Overlooking the potential for making all numbers equal when the array has fewer than four elements.
- Failing to account for all possible scenarios when applying the moves to the extreme values.