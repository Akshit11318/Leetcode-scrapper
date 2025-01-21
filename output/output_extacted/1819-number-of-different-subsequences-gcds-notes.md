## Number of Different Subsequences GCDs
**Problem Link:** https://leetcode.com/problems/number-of-different-subsequences-gcds/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Output: The number of different possible GCDs for subsequences of `nums`.
- Key requirements: Consider all possible subsequences, calculate their GCD, and count the distinct GCDs.
- Example test cases:
  - Input: `nums = [6,10,3]`
  - Output: `5`
  - Explanation: The GCDs of subsequences are 6, 10, 3, 2, and 1.

---

### Brute Force Approach
**Explanation:**
- Generate all possible subsequences of `nums`.
- For each subsequence, calculate its GCD.
- Store unique GCDs in a set.
- Return the size of the set.

```cpp
#include <vector>
#include <set>
#include <numeric>

int countDifferentSubsequenceGCDs(vector<int>& nums) {
    int n = nums.size();
    set<int> gcds;
    for (int mask = 1; mask < (1 << n); ++mask) {
        vector<int> subsequence;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i))) {
                subsequence.push_back(nums[i]);
            }
        }
        if (!subsequence.empty()) {
            int gcd = subsequence[0];
            for (int i = 1; i < subsequence.size(); ++i) {
                gcd = std::__gcd(gcd, subsequence[i]);
            }
            gcds.insert(gcd);
        }
    }
    return gcds.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot \log(max(nums)))$, where $n$ is the size of `nums` and $max(nums)$ is the maximum value in `nums`. This is because we generate $2^n$ subsequences, and for each, we calculate the GCD in $O(n \cdot \log(max(nums)))$ time using the Euclidean algorithm.
> - **Space Complexity:** $O(2^n)$ for storing all subsequences and $O(n)$ for the recursion stack, totaling $O(2^n + n)$.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsequences, and the logarithmic factor is due to the GCD calculation.

---

### Optimal Approach (Required)
**Explanation:**
- Find the maximum value in `nums` to determine the upper limit for potential GCDs.
- Iterate over all numbers from 1 to the maximum value in `nums`.
- For each number, check if it can be a GCD of a subsequence by verifying if there exist two elements in `nums` that are multiples of this number and have a GCD equal to this number.
- Alternatively, check if there exists at least one element in `nums` that is a multiple of this number, indicating it could be a GCD.

```cpp
#include <vector>
#include <set>
#include <numeric>

int countDifferentSubsequenceGCDs(vector<int>& nums) {
    int maxVal = *max_element(nums.begin(), nums.end());
    set<int> gcds;
    for (int i = 1; i <= maxVal; ++i) {
        bool found = false;
        for (int num : nums) {
            if (num % i == 0) {
                found = true;
                break;
            }
        }
        if (found) {
            gcds.insert(i);
        }
    }
    return gcds.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + max(nums))$, where $n$ is the size of `nums` and $max(nums)$ is the maximum value in `nums`. This is because we iterate over `nums` to find the maximum value and then iterate up to this maximum value.
> - **Space Complexity:** $O(n + max(nums))$ for storing the set of GCDs.
> - **Optimality proof:** This approach is optimal because it directly checks for the existence of each potential GCD without generating all subsequences, significantly reducing the time complexity.

---

### Final Notes

**Learning Points:**
- The importance of understanding the properties of GCD and how it applies to subsequences.
- The concept of using a set to store unique values.
- How to optimize a brute force approach by directly addressing the problem's requirements.

**Mistakes to Avoid:**
- Generating all subsequences when not necessary.
- Failing to consider the properties of GCD that allow for a more efficient solution.
- Not optimizing the algorithm based on the problem's constraints and requirements.