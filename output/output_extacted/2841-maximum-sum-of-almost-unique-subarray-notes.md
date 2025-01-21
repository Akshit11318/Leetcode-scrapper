## Maximum Sum of Almost Unique Subarray
**Problem Link:** https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/description

**Problem Statement:**
- Input format: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`, and `1 <= k <= 10^5`.
- Expected output format: The maximum sum of a subarray that contains at most `k` unique elements.
- Key requirements: Find the maximum sum of a subarray with at most `k` unique elements.
- Example test cases:
  - Input: `nums = [1,2,3,2,1], k = 3`, Output: `9`
  - Input: `nums = [1,2,3,4,5], k = 1`, Output: `5`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subarrays and then check each one to see if it contains at most `k` unique elements.
- Step-by-step breakdown:
  1. Generate all possible subarrays of `nums`.
  2. For each subarray, count the number of unique elements.
  3. If the number of unique elements is less than or equal to `k`, calculate the sum of the subarray.
  4. Keep track of the maximum sum found.

```cpp
#include <vector>
#include <unordered_set>

int maximumSum(vector<int>& nums, int k) {
    int maxSum = 0;
    int n = nums.size();
    
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            vector<int> subarray(nums.begin() + i, nums.begin() + j + 1);
            unordered_set<int> uniqueElements(subarray.begin(), subarray.end());
            
            if (uniqueElements.size() <= k) {
                int sum = 0;
                for (int num : subarray) {
                    sum += num;
                }
                maxSum = max(maxSum, sum);
            }
        }
    }
    
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`. This is because we are generating all possible subarrays ($O(n^2)$) and then counting the unique elements in each subarray ($O(n)$).
> - **Space Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we are storing each subarray and the unique elements in each subarray.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all possible subarrays and then checks each one, resulting in a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach to efficiently find the maximum sum of a subarray with at most `k` unique elements.
- Step-by-step breakdown:
  1. Initialize a sliding window with two pointers, `left` and `right`, to the start of `nums`.
  2. Use an unordered map to count the frequency of each element in the current window.
  3. Expand the window to the right by incrementing `right` and updating the frequency count.
  4. If the number of unique elements in the window exceeds `k`, shrink the window from the left by incrementing `left` and updating the frequency count.
  5. Keep track of the maximum sum of the window.

```cpp
#include <vector>
#include <unordered_map>

int maximumSum(vector<int>& nums, int k) {
    int maxSum = 0;
    int n = nums.size();
    unordered_map<int, int> freqCount;
    int windowSum = 0;
    
    int left = 0;
    for (int right = 0; right < n; right++) {
        windowSum += nums[right];
        freqCount[nums[right]]++;
        
        while (freqCount.size() > k) {
            freqCount[nums[left]]--;
            if (freqCount[nums[left]] == 0) {
                freqCount.erase(nums[left]);
            }
            windowSum -= nums[left];
            left++;
        }
        
        maxSum = max(maxSum, windowSum);
    }
    
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we are scanning `nums` once with the sliding window.
> - **Space Complexity:** $O(n)$, where $n` is the length of `nums`. This is because we are storing the frequency count of each element in the window.
> - **Optimality proof:** The optimal approach is efficient because it uses a sliding window to find the maximum sum of a subarray with at most `k` unique elements, avoiding the need to generate all possible subarrays.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the sliding window technique.
- The problem-solving pattern identified is the use of frequency counting to track unique elements.
- The optimization technique learned is the use of a sliding window to efficiently find the maximum sum of a subarray with constraints.
- Similar problems to practice include finding the maximum sum of a subarray with at most `k` elements or finding the minimum window that contains all unique elements.

**Mistakes to Avoid:**
- Common implementation errors include incorrect handling of edge cases, such as an empty input array or `k` being 0.
- Edge cases to watch for include when `k` is greater than the number of unique elements in `nums`.
- Performance pitfalls include using inefficient data structures or algorithms, such as using a brute force approach.
- Testing considerations include testing with different input sizes, `k` values, and edge cases.