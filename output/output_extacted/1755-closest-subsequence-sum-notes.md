## Closest Subsequence Sum
**Problem Link:** https://leetcode.com/problems/closest-subsequence-sum/description

**Problem Statement:**
- Given an array of integers `nums` and an integer `target`, return the closest subsequence sum to `target`.
- Input format: `nums` is a list of integers, and `target` is an integer.
- Expected output format: The closest subsequence sum to `target`.
- Key requirements and edge cases to consider: The subsequence sum should be as close as possible to `target`. If there are multiple subsequences with the same closest sum, any of them can be returned.
- Example test cases with explanations:
  - `nums = [1, 2, 3, 4], target = 7`, the closest subsequence sum is `7` itself.
  - `nums = [1, 2, 3, 4], target = 10`, the closest subsequence sum is `10` itself.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of `nums`, calculate their sums, and find the one closest to `target`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of `nums`.
  2. Calculate the sum of each subsequence.
  3. Compare the sums with `target` and find the closest one.
- Why this approach comes to mind first: It's a straightforward way to ensure all possibilities are considered.

```cpp
#include <vector>
#include <cmath>
using namespace std;

int minAbsDifference(vector<int>& nums, int target) {
    int closest = INT_MAX;
    int minDiff = INT_MAX;

    for (int mask = 0; mask < (1 << nums.size()); mask++) {
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            if ((mask & (1 << i)) != 0) {
                sum += nums[i];
            }
        }
        int diff = abs(sum - target);
        if (diff < minDiff) {
            minDiff = diff;
            closest = sum;
        }
    }
    return closest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of elements in `nums`. This is because we generate all possible subsequences ($2^n$) and for each, we calculate the sum which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, as we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is high because generating all subsequences and calculating their sums is computationally expensive. The space complexity is low because we only use a fixed amount of space to store the closest sum and the minimum difference.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a bitmask to generate all possible subsequences and keep track of the sums we've seen so far to avoid recalculating them. However, since we need to find the closest sum to the target, we can sort the sums and use a binary search approach to find the closest sum.
- Detailed breakdown of the approach:
  1. Generate all possible subsequences of `nums` using a bitmask.
  2. Calculate the sum of each subsequence and store them in a vector.
  3. Sort the vector of sums.
  4. Use binary search to find the closest sum to `target`.
- Proof of optimality: This approach ensures we consider all possible subsequences and find the closest sum to the target in an efficient manner.

```cpp
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int minAbsDifference(vector<int>& nums, int target) {
    vector<int> sums;
    for (int mask = 0; mask < (1 << nums.size()); mask++) {
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            if ((mask & (1 << i)) != 0) {
                sum += nums[i];
            }
        }
        sums.push_back(sum);
    }
    sort(sums.begin(), sums.end());

    int closest = sums[0];
    for (int sum : sums) {
        if (abs(sum - target) < abs(closest - target)) {
            closest = sum;
        }
    }
    return closest;
}
```

However, the optimal solution should utilize a more efficient method to find the closest sum, such as using a `set` to store unique sums and then iterating through the set to find the closest sum.

```cpp
#include <vector>
#include <set>
#include <cmath>
using namespace std;

int minAbsDifference(vector<int>& nums, int target) {
    set<int> sums;
    sums.insert(0);
    for (int num : nums) {
        set<int> temp = sums;
        for (int sum : temp) {
            sums.insert(sum + num);
        }
    }

    int closest = *sums.begin();
    for (int sum : sums) {
        if (abs(sum - target) < abs(closest - target)) {
            closest = sum;
        }
    }
    return closest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot \log n)$, where $n$ is the number of elements in `nums`. This is because we generate all possible subsequences ($2^n$) and for each, we insert into a set which takes $O(\log n)$ time.
> - **Space Complexity:** $O(2^n)$, as we store all unique sums in a set.
> - **Optimality proof:** This approach ensures we consider all possible subsequences and find the closest sum to the target in an efficient manner.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: bitmasking, set operations, and efficient search algorithms.
- Problem-solving patterns identified: generating all possible subsequences, calculating sums, and finding the closest sum to a target.
- Optimization techniques learned: using a set to store unique sums and iterating through the set to find the closest sum.
- Similar problems to practice: problems involving generating all possible subsequences, calculating sums, and finding the closest sum to a target.

**Mistakes to Avoid:**
- Common implementation errors: not considering all possible subsequences, not handling edge cases correctly.
- Edge cases to watch for: empty input array, target sum not found.
- Performance pitfalls: using inefficient algorithms, not optimizing the solution for large inputs.
- Testing considerations: test the solution with different input sizes, edge cases, and target sums.