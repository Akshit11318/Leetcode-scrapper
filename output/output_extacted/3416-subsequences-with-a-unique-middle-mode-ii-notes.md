## Subsequences with a Unique Middle Mode II
**Problem Link:** https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Output: The number of subsequences with a unique middle mode, where a subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.
- Key requirements and edge cases: The array `nums` can contain duplicate elements, and a subsequence with a unique middle mode is a subsequence where all elements in the middle (if the length of the subsequence is odd) or the two middle elements (if the length of the subsequence is even) have the same value and this value is unique among all middle elements of all subsequences.
- Example test cases:
  - `nums = [1, 2, 1, 3]`, the subsequences with a unique middle mode are `[1]`, `[1, 1]`, `[1, 1, 3]`, `[1, 2, 1]`, `[2, 1]`, and `[2, 1, 3]`.
  - `nums = [1, 1, 2]`, the subsequences with a unique middle mode are `[1]`, `[1, 1]`, and `[1, 1, 2]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subsequences of the given array `nums` and then check each subsequence to see if it has a unique middle mode.
- This approach involves using a recursive function or bit manipulation to generate all subsequences.
- For each subsequence, we determine the middle element(s) and check if this element is unique among all middle elements found so far.

```cpp
int numUniqueSubseqs(vector<int>& nums) {
    set<int> uniqueSubseqs;
    int n = nums.size();
    
    // Generate all possible subsequences
    for (int mask = 0; mask < (1 << n); ++mask) {
        vector<int> subseq;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                subseq.push_back(nums[i]);
            }
        }
        
        // Check if the subsequence has a unique middle mode
        if (subseq.size() > 0) {
            int middleMode = subseq[subseq.size() / 2];
            if (subseq.size() % 2 == 0) {
                middleMode = min(middleMode, subseq[subseq.size() / 2 - 1]);
            }
            bool isUnique = true;
            for (int i = 0; i < subseq.size(); ++i) {
                if (subseq[i] != middleMode && i >= subseq.size() / 2 - (subseq.size() % 2) && i <= subseq.size() / 2) {
                    isUnique = false;
                    break;
                }
            }
            if (isUnique) {
                sort(subseq.begin(), subseq.end());
                uniqueSubseqs.insert(subseq[0]);
            }
        }
    }
    
    return uniqueSubseqs.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot log(n))$ due to generating all subsequences and sorting each subsequence to check for uniqueness.
> - **Space Complexity:** $O(2^n \cdot n)$ for storing all subsequences.
> - **Why these complexities occur:** The brute force approach generates all possible subsequences, which leads to an exponential time complexity. The space complexity is also exponential due to storing these subsequences.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using dynamic programming to count the number of subsequences with a unique middle mode.
- We maintain a map to store the count of each number as we process the array.
- For each number, we calculate the number of subsequences that can be formed with this number as the middle mode.

```cpp
int numUniqueSubseqs(vector<int>& nums) {
    unordered_map<int, long long> count;
    long long result = 0;
    
    for (int num : nums) {
        if (count.find(num) == count.end()) {
            count[num] = 1;
        } else {
            count[num] *= 2;
        }
    }
    
    for (auto& pair : count) {
        result += pair.second;
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array.
> - **Space Complexity:** $O(n)$ for storing the count of each number.
> - **Optimality proof:** This approach is optimal because it directly counts the number of subsequences with a unique middle mode without generating all possible subsequences, thus avoiding exponential complexity.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems that involve counting and combinatorics.
- How to optimize the solution by avoiding unnecessary computations and using data structures like maps to store and retrieve information efficiently.

**Mistakes to Avoid:**
- Generating all possible subsequences, which can lead to exponential time complexity.
- Not using dynamic programming to count the number of subsequences with a unique middle mode, which can simplify the solution and improve efficiency.