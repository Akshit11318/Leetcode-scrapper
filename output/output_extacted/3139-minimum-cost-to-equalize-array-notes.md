## Minimum Cost to Equalize Array
**Problem Link:** https://leetcode.com/problems/minimum-cost-to-equalize-array/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: The length of `nums` is greater than 0.
- Expected output: The minimum cost to make all elements in `nums` equal, where the cost is the sum of absolute differences between each element and the target value.
- Key requirements: Find the optimal target value that minimizes the total cost.
- Edge cases: Handle arrays with duplicate elements, negative numbers, and zero.

**Example Test Cases:**
- `nums = [1, 3, 5]`: The optimal target is 3, with a total cost of 4 (|1-3| + |3-3| + |5-3|).
- `nums = [2, 2, 2]`: The optimal target is 2, with a total cost of 0 (since all elements are already equal).

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible target values and calculate the total cost for each one.
- Iterate through each unique element in `nums` as the potential target value.
- For each target value, calculate the total cost by summing the absolute differences between each element in `nums` and the target value.
- Keep track of the target value that results in the minimum total cost.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minCost(vector<int>& nums) {
    int minCost = INT_MAX;
    for (int target : nums) {
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
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums`, because we iterate through each element in `nums` for each unique target value.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the minimum cost and the current cost.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested iteration, but it has a low space complexity since we don't use any additional data structures.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is that the optimal target value is the median of the elements in `nums`.
- The median is the middle value in the sorted array, which minimizes the sum of absolute differences.
- We can find the median by sorting `nums` and selecting the middle element (or the average of the two middle elements if the length is even).
- Calculate the total cost by summing the absolute differences between each element in `nums` and the median.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minCost(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int median;
    int n = nums.size();
    if (n % 2 == 0) {
        median = (nums[n/2 - 1] + nums[n/2]) / 2;
    } else {
        median = nums[n/2];
    }
    int cost = 0;
    for (int num : nums) {
        cost += abs(num - median);
    }
    return cost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of `nums`, because we sort `nums` using a comparison-based sorting algorithm.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the median and the total cost.
> - **Optimality proof:** The optimal approach has a lower time complexity than the brute force approach because sorting `nums` allows us to find the median in linear time, and calculating the total cost takes linear time as well.

---

### Final Notes

**Learning Points:**
- The importance of understanding the properties of the median and its relationship to the sum of absolute differences.
- The use of sorting to find the median and calculate the total cost.
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Assuming that the optimal target value is the mean of the elements in `nums`, which would result in a higher total cost.
- Using a brute force approach for large inputs, which would lead to excessive computation time.
- Failing to consider edge cases, such as arrays with duplicate elements or negative numbers.