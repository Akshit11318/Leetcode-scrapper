## Longest Nice Subarray
**Problem Link:** https://leetcode.com/problems/longest-nice-subarray/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Output: The length of the longest `nice` subarray.
- A `nice` subarray is a subarray where for every element `x` in the subarray, there exists a `y` in the subarray such that `x ^ y = x + y`.
- This implies that for every element `x`, there must be a corresponding element `y` such that `x & y = 0`, because `x ^ y = x + y` only holds true if `x` and `y` have no bits in common.
- Key requirements: The subarray must be contiguous and must satisfy the `nice` condition.
- Edge cases: Empty array, single-element array, arrays with duplicate elements.

**Example Test Cases:**
- `[1, 3, 2, 4, 5]`: The longest nice subarray is `[1, 3, 2, 4]`.
- `[0, 1, 2]`: The longest nice subarray is `[0, 1]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible subarray to see if it's `nice`.
- This involves iterating over all possible start and end indices for subarrays, then for each subarray, checking if it's `nice` by ensuring that for every element `x`, there exists a `y` such that `x & y = 0`.

```cpp
class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int n = nums.size();
        int maxLength = 0;
        
        // Iterate over all possible subarrays
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                vector<int> subarray(nums.begin() + i, nums.begin() + j + 1);
                
                // Check if the subarray is nice
                if (isNice(subarray)) {
                    maxLength = max(maxLength, (int)subarray.size());
                }
            }
        }
        
        return maxLength;
    }
    
    bool isNice(vector<int>& subarray) {
        for (int x : subarray) {
            bool found = false;
            for (int y : subarray) {
                if ((x & y) == 0) {
                    found = true;
                    break;
                }
            }
            if (!found) return false;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we are generating all possible subarrays ($O(n^2)$) and then for each subarray, we are checking if it's `nice` ($O(n)$).
> - **Space Complexity:** $O(n)$, as in the worst case, we might need to store a subarray of the same length as the input array.
> - **Why these complexities occur:** The high time complexity occurs due to the nested loops used to generate all possible subarrays and then check each one. The space complexity is due to the storage needed for the subarray.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight here is to use a hashmap to store the elements we've seen so far and their corresponding complements.
- We can utilize the property of `nice` subarrays that for every element `x`, there must exist a `y` such that `x & y = 0`.
- This approach involves maintaining a sliding window where we expand the window to the right and shrink it from the left based on whether the current window is `nice`.

```cpp
class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int n = nums.size();
        int maxLength = 0;
        int left = 0;
        unordered_map<int, int> freq;
        
        for (int right = 0; right < n; right++) {
            freq[nums[right]]++;
            
            while (hasConflictingPair(freq)) {
                freq[nums[left]]--;
                if (freq[nums[left]] == 0) freq.erase(nums[left]);
                left++;
            }
            
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
    
    bool hasConflictingPair(unordered_map<int, int>& freq) {
        for (auto& [num, count] : freq) {
            for (int mask = 0; mask < 31; mask++) {
                int complement = (1 << mask);
                if (freq.find(complement) != freq.end()) {
                    if ((num & complement) != 0) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};
```

However, a better solution exists for this particular problem that doesn't require checking all pairs. Instead, we can utilize the fact that if `x` and `y` have no bits in common, they must be complements in the subarray's context.

```cpp
class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int maxLength = 0;
        int mask = 0;
        unordered_map<int, int> lastSeen;
        
        lastSeen[0] = -1;
        
        for (int i = 0; i < nums.size(); i++) {
            mask ^= nums[i];
            for (int j = 0; j < 31; j++) {
                int target = mask ^ (1 << j);
                if (lastSeen.find(target) != lastSeen.end()) {
                    maxLength = max(maxLength, i - lastSeen[target]);
                }
            }
            lastSeen[mask] = i;
        }
        
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot b)$, where $n$ is the number of elements and $b$ is the number of bits in the largest number. However, since $b$ is constant (32 for integers), this simplifies to $O(n)$.
> - **Space Complexity:** $O(n)$, for storing the last seen indices of masks.
> - **Optimality proof:** This solution is optimal because it checks every possible subarray exactly once and uses a hashmap to store and retrieve information in constant time, avoiding redundant calculations.

---

### Final Notes

**Learning Points:**
- Utilizing bit manipulation to solve problems related to binary representations.
- Applying sliding window techniques to efficiently scan through arrays.
- Employing hashmaps for efficient storage and retrieval of data.

**Mistakes to Avoid:**
- Failing to consider edge cases such as empty arrays or arrays with single elements.
- Not optimizing the solution by removing unnecessary computations.
- Incorrectly implementing the sliding window or hashmap, leading to incorrect results or inefficiencies.