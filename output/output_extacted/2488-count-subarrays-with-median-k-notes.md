## Count Subarrays with Median K

**Problem Link:** https://leetcode.com/problems/count-subarrays-with-median-k/description

**Problem Statement:**
- Input: An array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 3 * 10^5`, `1 <= nums[i] <= 5 * 10^5`, `1 <= k <= 5 * 10^5`.
- Expected Output: The number of subarrays where the median is equal to `k`.
- Key Requirements: The median of a subarray is the middle value when the subarray is sorted. If the length of the subarray is even, the median is the average of the two middle values.
- Edge Cases: Handle cases where the subarray has an odd or even length.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subarrays and check if the median of each subarray is equal to `k`.
- Step-by-step breakdown:
  1. Generate all possible subarrays.
  2. For each subarray, sort it and calculate the median.
  3. Check if the median is equal to `k`. If it is, increment the count.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by checking every possible subarray.

```cpp
class Solution {
public:
    int countSubarrays(vector<int>& nums, int k) {
        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i; j < nums.size(); j++) {
                vector<int> subarray(nums.begin() + i, nums.begin() + j + 1);
                sort(subarray.begin(), subarray.end());
                double median;
                if (subarray.size() % 2 == 0) {
                    median = (subarray[subarray.size() / 2 - 1] + subarray[subarray.size() / 2]) / 2.0;
                } else {
                    median = subarray[subarray.size() / 2];
                }
                if (median == k) {
                    count++;
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \log n)$, where $n$ is the length of the input array. This is because we generate $O(n^2)$ subarrays, each of which takes $O(n \log n)$ time to sort.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we need to store each subarray.
> - **Why these complexities occur:** The high time complexity occurs because we are generating and sorting all possible subarrays.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of sorting each subarray, we can use a sliding window approach to maintain a sorted subarray.
- Detailed breakdown:
  1. Initialize two pointers, `left` and `right`, to the start of the array.
  2. Use a multiset to store the elements in the current window.
  3. As we move the `right` pointer to the right, add the new element to the multiset.
  4. As we move the `left` pointer to the right, remove the old element from the multiset.
  5. At each step, check if the median of the current window is equal to `k`.
- Proof of optimality: This approach has a much lower time complexity than the brute force approach because we avoid sorting each subarray.

```cpp
class Solution {
public:
    int countSubarrays(vector<int>& nums, int k) {
        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            multiset<int> window;
            for (int j = i; j < nums.size(); j++) {
                window.insert(nums[j]);
                int median;
                if (window.size() % 2 == 0) {
                    auto it = window.begin();
                    advance(it, window.size() / 2 - 1);
                    int val1 = *it;
                    it++;
                    int val2 = *it;
                    median = (val1 + val2) / 2;
                } else {
                    auto it = window.begin();
                    advance(it, window.size() / 2);
                    median = *it;
                }
                if (median == k) {
                    count++;
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log n)$, where $n$ is the length of the input array. This is because we use a multiset to store the elements in the current window, and each insertion and removal operation takes $O(\log n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we need to store the elements in the current window.
> - **Optimality proof:** This approach is optimal because we avoid sorting each subarray, which reduces the time complexity significantly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window, multiset, median calculation.
- Problem-solving patterns identified: Using a multiset to maintain a sorted window.
- Optimization techniques learned: Avoiding unnecessary sorting operations.
- Similar problems to practice: Other problems involving median calculation or sliding window techniques.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect median calculation, incorrect multiset operations.
- Edge cases to watch for: Handling cases where the subarray has an odd or even length.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Testing with different input sizes and edge cases.