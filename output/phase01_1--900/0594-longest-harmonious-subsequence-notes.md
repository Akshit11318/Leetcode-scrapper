## Longest Harmonious Subsequence

**Problem Link:** https://leetcode.com/problems/longest-harmonious-subsequence/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: `1 <= nums.length <= 2 * 10^4`, `-10^9 <= nums[i] <= 10^9`.
- Expected Output: The length of the longest harmonious subsequence.
- Key Requirements: A harmonious subsequence is a subsequence where the difference between the maximum and minimum elements is exactly 1.
- Example Test Cases:
  - Input: `nums = [1,3,2,2,5,2,3,7]`
  - Output: `5`
  - Explanation: The longest harmonious subsequence is `[3,2,2,2,3]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subsequences of the input array and check if each subsequence is harmonious.
- We can use a recursive function to generate all subsequences and then calculate the difference between the maximum and minimum elements in each subsequence.
- This approach comes to mind first because it directly addresses the problem statement without requiring any additional insights.

```cpp
class Solution {
public:
    int findLHS(vector<int>& nums) {
        int n = nums.size();
        int maxLen = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            vector<int> subsequence;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i))) {
                    subsequence.push_back(nums[i]);
                }
            }
            if (subsequence.empty()) continue;
            int minVal = *min_element(subsequence.begin(), subsequence.end());
            int maxVal = *max_element(subsequence.begin(), subsequence.end());
            if (maxVal - minVal == 1) {
                maxLen = max(maxLen, (int)subsequence.size());
            }
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we generate all possible subsequences (which takes $O(2^n)$ time) and for each subsequence, we find the minimum and maximum elements (which takes $O(n)$ time).
> - **Space Complexity:** $O(n)$, because in the worst case, we might store all elements of the input array in a subsequence.
> - **Why these complexities occur:** The brute force approach has exponential time complexity because it generates all possible subsequences, and linear space complexity because we store each subsequence.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a hash map to store the frequency of each number in the input array.
- We then iterate through the hash map and for each number, we check if the number plus one is also in the hash map. If it is, we update the maximum length of the harmonious subsequence.
- This approach is optimal because it only requires a single pass through the input array and the hash map, resulting in a significant reduction in time complexity.

```cpp
class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        int maxLen = 0;
        for (auto& pair : freq) {
            if (freq.find(pair.first + 1) != freq.end()) {
                maxLen = max(maxLen, pair.second + freq[pair.first + 1]);
            }
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we make a single pass through the input array to populate the hash map, and then another pass through the hash map to find the maximum length of the harmonious subsequence.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store all elements of the input array in the hash map.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity, which is the best possible time complexity for this problem. We must at least read the input array once, which takes $O(n)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: hash maps, frequency counting, and iteration through a data structure.
- Problem-solving patterns identified: using a hash map to store frequency information and then iterating through the hash map to find the desired result.
- Optimization techniques learned: reducing time complexity by using a hash map to store frequency information and avoiding unnecessary iterations.
- Similar problems to practice: other problems that involve frequency counting and iteration through a data structure, such as finding the most frequent element in an array.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to initialize variables, using incorrect data structures, and not handling edge cases.
- Edge cases to watch for: empty input arrays, arrays with a single element, and arrays with duplicate elements.
- Performance pitfalls: using inefficient data structures or algorithms, such as using a linear search instead of a hash map.
- Testing considerations: testing the solution with different input arrays, including edge cases, to ensure that it produces the correct result.