## Find K-th Smallest Pair Distance
**Problem Link:** https://leetcode.com/problems/find-k-th-smallest-pair-distance/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 60,000`, `0 <= nums[i] <= 10^6`, `1 <= k <= nums.length * (nums.length - 1) / 2`.
- Expected Output: The `k`-th smallest distance among all pairs `(nums[i], nums[j])` where `0 <= i < nums.length` and `0 <= j < nums.length` and `i < j`.
- Key Requirements:
  - Handle large inputs efficiently.
  - Consider all pairs of elements in the array.
- Edge Cases:
  - Duplicate elements in the array.
  - `k` is larger than the number of unique pair distances.
- Example Test Cases:
  - `nums = [1, 3, 1]`, `k = 1`: Output should be `0` because the smallest pair distance is `0` (between two `1`s).
  - `nums = [1, 6, 1]`, `k = 3`: Output should be `5` because the third smallest pair distance is `5` (between `1` and `6`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate all possible pair distances and sort them to find the `k`-th smallest.
- Step-by-step breakdown:
  1. Generate all pairs of elements from the input array.
  2. Calculate the distance for each pair (as the absolute difference between the two elements).
  3. Store all distances in a list.
  4. Sort the list of distances.
  5. Return the `k`-th element of the sorted list as the `k`-th smallest pair distance.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int smallestDistancePair(vector<int>& nums, int k) {
    vector<int> distances;
    for (int i = 0; i < nums.size(); ++i) {
        for (int j = i + 1; j < nums.size(); ++j) {
            distances.push_back(abs(nums[i] - nums[j]));
        }
    }
    sort(distances.begin(), distances.end());
    return distances[k - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log(n^2))$ where $n$ is the size of the input array `nums`. This comes from generating $O(n^2)$ pairs and sorting them, which takes $O(n^2 \log(n^2))$ time.
> - **Space Complexity:** $O(n^2)$ for storing all pair distances.
> - **Why these complexities occur:** The brute force approach involves generating all possible pairs of elements and sorting their distances, leading to quadratic time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach uses a binary search strategy to find the `k`-th smallest pair distance efficiently.
- Key insight: Instead of directly calculating and sorting all distances, we can use binary search to narrow down the range of possible distances until we find the `k`-th smallest.
- Step-by-step breakdown:
  1. Determine the range of possible distances (from `0` to the maximum possible distance in the array).
  2. Perform a binary search within this range.
  3. For each mid-distance in the binary search, count how many pair distances are less than or equal to this mid-distance.
  4. If the count is greater than or equal to `k`, update the upper bound of the search range to the mid-distance.
  5. If the count is less than `k`, update the lower bound of the search range to just above the mid-distance.
  6. Continue the binary search until the lower and upper bounds converge to a single distance value, which is the `k`-th smallest pair distance.

```cpp
#include <vector>
using namespace std;

int smallestDistancePair(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    int low = 0, high = nums.back() - nums[0];
    while (low < high) {
        int mid = low + (high - low) / 2;
        int count = 0;
        for (int i = 0, j = 0; i < nums.size(); ++i) {
            while (j < nums.size() && nums[j] - nums[i] <= mid) {
                j++;
            }
            count += j - i - 1;
        }
        if (count < k) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return low;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log(max - min))$ where $n$ is the size of the input array `nums`, and $max$ and $min$ are the maximum and minimum values in `nums`. This comes from the binary search and the inner loop that counts pair distances less than or equal to the mid-distance.
> - **Space Complexity:** $O(1)$ excluding the space needed for sorting the input array, as we only use a constant amount of space to store variables.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity significantly compared to the brute force approach by using binary search to find the `k`-th smallest distance without explicitly calculating and sorting all distances.

---

### Final Notes

**Learning Points:**
- The importance of binary search in solving problems involving finding a specific element or threshold within a range.
- How to apply the concept of counting pair distances less than or equal to a given distance to solve the problem efficiently.
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Failing to consider the range of possible distances and how to efficiently search within this range.
- Not optimizing the counting process for pair distances, potentially leading to inefficient solutions.
- Overlooking the possibility of using binary search to reduce the time complexity of the problem.