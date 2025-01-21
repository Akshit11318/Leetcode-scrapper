## Pour Water Between Buckets to Make Water Levels Equal

**Problem Link:** https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/description

**Problem Statement:**
- Input: An integer array `buckets` where each element represents the height of a bucket, and an integer `capacity`.
- Constraints: The length of `buckets` is in the range `[2, 10^5]`, and `0 <= buckets[i], capacity <= 10^6`.
- Expected Output: The maximum height of the water level in the buckets after pouring water between them, assuming that we can pour water from one bucket to another if the height of the water in the source bucket is greater than or equal to the height of the water in the destination bucket.
- Key Requirements:
  - We can pour water from one bucket to another if the height of the water in the source bucket is greater than or equal to the height of the water in the destination bucket.
  - We want to maximize the minimum water level among all buckets.
- Edge Cases:
  - If the total capacity of all buckets is less than or equal to the given capacity, we can fill all buckets to their maximum capacity.
  - If the total capacity of all buckets is greater than the given capacity, we need to distribute the given capacity among the buckets to maximize the minimum water level.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of pouring water from one bucket to another.
- However, this approach is impractical due to the large number of possible combinations.
- A more feasible brute force approach is to use a binary search to find the maximum height of the water level.

```cpp
class Solution {
public:
    int maxHeight(vector<int>& buckets, int capacity) {
        int n = buckets.size();
        int totalCapacity = 0;
        for (int i = 0; i < n; i++) {
            totalCapacity += buckets[i];
        }
        if (totalCapacity <= capacity) {
            return min(capacity / n, *max_element(buckets.begin(), buckets.end()));
        }
        int low = 0, high = *max_element(buckets.begin(), buckets.end());
        while (low < high) {
            int mid = (low + high + 1) / 2;
            long long sum = 0;
            for (int i = 0; i < n; i++) {
                sum += min(buckets[i], mid);
            }
            if (sum <= capacity) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log m)$, where $n$ is the number of buckets and $m$ is the maximum height of the buckets. The reason for this complexity is that we are performing a binary search over the range of possible heights, and for each iteration of the binary search, we are iterating over the buckets to calculate the sum of their heights.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the variables.
> - **Why these complexities occur:** The time complexity occurs because we are using a binary search to find the maximum height, and the space complexity occurs because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a binary search to find the maximum height of the water level.
- The optimal solution is the same as the brute force approach, as it already uses a binary search to find the maximum height.

```cpp
class Solution {
public:
    int maxHeight(vector<int>& buckets, int capacity) {
        int n = buckets.size();
        int totalCapacity = 0;
        for (int i = 0; i < n; i++) {
            totalCapacity += buckets[i];
        }
        if (totalCapacity <= capacity) {
            return min(capacity / n, *max_element(buckets.begin(), buckets.end()));
        }
        int low = 0, high = *max_element(buckets.begin(), buckets.end());
        while (low < high) {
            int mid = (low + high + 1) / 2;
            long long sum = 0;
            for (int i = 0; i < n; i++) {
                sum += min(buckets[i], mid);
            }
            if (sum <= capacity) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log m)$, where $n$ is the number of buckets and $m$ is the maximum height of the buckets.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the variables.
> - **Optimality proof:** This is the optimal solution because we are using a binary search to find the maximum height, which has a time complexity of $O(\log m)$. We are also iterating over the buckets to calculate the sum of their heights, which has a time complexity of $O(n)$. Therefore, the overall time complexity is $O(n \log m)$.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the use of binary search to find the maximum height of the water level.
- The problem-solving pattern identified in this problem is to use a binary search to find the maximum or minimum value of a function.
- The optimization technique learned in this problem is to use a binary search to reduce the time complexity of the solution.

**Mistakes to Avoid:**
- A common implementation error is to use a linear search instead of a binary search, which can increase the time complexity of the solution.
- An edge case to watch for is when the total capacity of all buckets is less than or equal to the given capacity, in which case we can fill all buckets to their maximum capacity.
- A performance pitfall is to use a recursive solution instead of an iterative solution, which can increase the space complexity of the solution.