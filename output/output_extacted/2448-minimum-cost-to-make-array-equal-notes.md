## Minimum Cost to Make Array Equal
**Problem Link:** https://leetcode.com/problems/minimum-cost-to-make-array-equal/description

**Problem Statement:**
- Given an array `nums` and an integer `k`, find the minimum cost to make all elements in the array equal. The cost of changing an element from `x` to `y` is `abs(x - y)`.
- Input format and constraints: `1 <= nums.length <= 100`, `1 <= nums[i] <= 100`, `1 <= k <= 100`.
- Expected output format: The minimum cost to make all elements in the array equal.
- Key requirements and edge cases to consider: Handling cases where `k` is larger than the maximum value in `nums`, and cases where `nums` contains only one unique element.
- Example test cases with explanations: 
    - For `nums = [1, 3, 5, 2]` and `k = 2`, the minimum cost is `2` because we can change all elements to `2`.
    - For `nums = [2, 2, 2, 2]` and `k = 2`, the minimum cost is `0` because all elements are already equal.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible values that can be the target value to make all elements in the array equal.
- Step-by-step breakdown of the solution: 
    1. Generate all possible target values.
    2. For each target value, calculate the total cost to make all elements in the array equal to the target value.
    3. Keep track of the minimum cost found.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, but it can be inefficient for large inputs.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int minCost(vector<int>& nums, int k) {
    int minCost = INT_MAX;
    for (int target = 1; target <= 100; target++) {
        int cost = 0;
        for (int num : nums) {
            cost += abs(num - target);
        }
        minCost = min(minCost, cost);
    }
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of elements in `nums` and $m$ is the range of possible target values.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum cost and the current target value.
> - **Why these complexities occur:** The brute force approach tries all possible target values, resulting in a time complexity that is linear in the number of elements and the range of possible target values.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal target value is the median of the array, because it minimizes the sum of absolute differences to all other values.
- Detailed breakdown of the approach: 
    1. Sort the array to find the median.
    2. Calculate the total cost to make all elements in the array equal to the median.
- Proof of optimality: The median is the value that minimizes the sum of absolute differences to all other values, because it is the value that is closest to the largest number of other values.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int minCost(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    int median = nums[nums.size() / 2];
    int cost = 0;
    for (int num : nums) {
        cost += abs(num - median);
    }
    return cost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in `nums`, due to the sorting step.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the median and the current cost.
> - **Optimality proof:** The median is the optimal target value because it minimizes the sum of absolute differences to all other values, resulting in the minimum cost to make all elements in the array equal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, median calculation, and minimization of sum of absolute differences.
- Problem-solving patterns identified: Using the median as the optimal target value to minimize the sum of absolute differences.
- Optimization techniques learned: Sorting the array to find the median, and calculating the total cost using the median.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the array correctly, or not calculating the median correctly.
- Edge cases to watch for: Handling cases where `k` is larger than the maximum value in `nums`, and cases where `nums` contains only one unique element.
- Performance pitfalls: Using an inefficient sorting algorithm, or not using the median as the optimal target value.
- Testing considerations: Testing the solution with different inputs, including edge cases and large inputs.