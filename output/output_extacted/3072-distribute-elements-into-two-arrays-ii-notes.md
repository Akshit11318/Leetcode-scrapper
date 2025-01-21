## Distribute Elements into Two Arrays II
**Problem Link:** https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/description

**Problem Statement:**
- Input: A list of integers `nums` and an integer `k`.
- Expected output: The minimum difference between the maximum sum of `k` elements in the first array and the sum of all elements in the second array.
- Key requirements: Distribute the elements of `nums` into two arrays such that the difference between the maximum sum of `k` elements in the first array and the sum of all elements in the second array is minimized.
- Example test cases:
  - `nums = [1, 2, 3, 4], k = 2`, the output should be `0`.
  - `nums = [1, 1, 1, 1], k = 2`, the output should be `0`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of distributing the elements of `nums` into two arrays.
- For each combination, calculate the maximum sum of `k` elements in the first array and the sum of all elements in the second array.
- Keep track of the minimum difference found.

```cpp
class Solution {
public:
    int minDifference(vector<int>& nums, int k) {
        int n = nums.size();
        int res = INT_MAX;
        for (int mask = 0; mask < (1 << n); mask++) {
            vector<int> first, second;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    first.push_back(nums[i]);
                } else {
                    second.push_back(nums[i]);
                }
            }
            if (first.size() < k) continue;
            sort(first.rbegin(), first.rend());
            int sumFirst = 0;
            for (int i = 0; i < k; i++) {
                sumFirst += first[i];
            }
            int sumSecond = 0;
            for (int num : second) {
                sumSecond += num;
            }
            res = min(res, sumFirst - sumSecond);
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \log n)$, where $n$ is the number of elements in `nums`. The reason is that we try all possible combinations of distributing the elements, and for each combination, we sort the first array.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. The reason is that we need to store the elements of the two arrays.
> - **Why these complexities occur:** The brute force approach has high time complexity because it tries all possible combinations, which is exponential in the number of elements. The space complexity is linear because we need to store the elements of the two arrays.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to realize that we can use a greedy approach to distribute the elements.
- We sort the elements of `nums` in descending order.
- We then distribute the largest `k` elements into the first array, and the remaining elements into the second array.
- This approach minimizes the difference between the maximum sum of `k` elements in the first array and the sum of all elements in the second array.

```cpp
class Solution {
public:
    int minDifference(vector<int>& nums, int k) {
        sort(nums.rbegin(), nums.rend());
        int sumFirst = 0;
        for (int i = 0; i < k; i++) {
            sumFirst += nums[i];
        }
        int sumSecond = 0;
        for (int i = k; i < nums.size(); i++) {
            sumSecond += nums[i];
        }
        return sumFirst - sumSecond;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in `nums`. The reason is that we sort the elements of `nums`.
> - **Space Complexity:** $O(1)$, where $n$ is the number of elements in `nums`. The reason is that we only need to use a constant amount of space to store the sums of the two arrays.
> - **Optimality proof:** This approach is optimal because it minimizes the difference between the maximum sum of `k` elements in the first array and the sum of all elements in the second array. By distributing the largest `k` elements into the first array, we maximize the sum of the first array, and by distributing the remaining elements into the second array, we minimize the sum of the second array.

---

### Final Notes

**Learning Points:**
- The importance of sorting in algorithmic problems.
- The use of greedy approaches to solve optimization problems.
- The need to consider the distribution of elements in arrays.

**Mistakes to Avoid:**
- Not considering the distribution of elements in arrays.
- Not using a greedy approach to solve the problem.
- Not sorting the elements of `nums` in descending order.

---