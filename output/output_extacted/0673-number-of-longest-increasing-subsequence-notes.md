## Number of Longest Increasing Subsequence

**Problem Link:** https://leetcode.com/problems/number-of-longest-increasing-subsequence/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The length of `nums` is in the range `[1, 2000]`.
- Expected output format: The number of longest increasing subsequences in `nums`.
- Key requirements and edge cases to consider:
  - Handling arrays with a single element.
  - Arrays with no increasing subsequences.
  - Arrays with multiple longest increasing subsequences.
- Example test cases with explanations:
  - Input: `nums = [1,3,5,4,7]`
    - Output: `2`
    - Explanation: The two longest increasing subsequences are `[1, 3, 4, 7]` and `[1, 3, 5, 7]`.
  - Input: `nums = [2,2,2,2,2]`
    - Output: `5`
    - Explanation: The longest increasing subsequence is of length 1, and there are 5 such subsequences.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of `nums` and check each one to see if it is increasing.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of `nums`.
  2. For each subsequence, check if it is increasing.
  3. Keep track of the longest increasing subsequences found so far.
  4. Count the number of longest increasing subsequences.
- Why this approach comes to mind first: It is a straightforward, brute-force solution that checks all possible subsequences.

```cpp
int findNumberOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<vector<int>> subsequences;
    generateSubsequences(nums, 0, {}, subsequences);
    int maxLength = 0;
    int count = 0;
    for (auto& subsequence : subsequences) {
        if (isIncreasing(subsequence)) {
            int length = subsequence.size();
            if (length > maxLength) {
                maxLength = length;
                count = 1;
            } else if (length == maxLength) {
                count++;
            }
        }
    }
    return count;
}

void generateSubsequences(vector<int>& nums, int start, vector<int> current, vector<vector<int>>& subsequences) {
    subsequences.push_back(current);
    for (int i = start; i < nums.size(); i++) {
        current.push_back(nums[i]);
        generateSubsequences(nums, i + 1, current, subsequences);
        current.pop_back();
    }
}

bool isIncreasing(vector<int>& subsequence) {
    for (int i = 1; i < subsequence.size(); i++) {
        if (subsequence[i] <= subsequence[i - 1]) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of `nums`. This is because there are $2^n$ possible subsequences, and checking if each one is increasing takes $O(n)$ time.
> - **Space Complexity:** $O(2^n \cdot n)$, as we need to store all possible subsequences.
> - **Why these complexities occur:** The brute-force approach generates all possible subsequences, which results in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to keep track of the length of the longest increasing subsequence ending at each position, as well as the number of such subsequences.
- Detailed breakdown of the approach:
  1. Initialize two arrays, `lengths` and `counts`, to keep track of the length of the longest increasing subsequence ending at each position and the number of such subsequences, respectively.
  2. Iterate over `nums`, updating `lengths` and `counts` as we go.
  3. Keep track of the maximum length seen so far and the number of subsequences of that length.
- Proof of optimality: This approach has a time complexity of $O(n^2)$, which is optimal because we must at least look at each element in `nums` once.

```cpp
int findNumberOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> lengths(n, 1);
    vector<int> counts(n, 1);
    int maxLength = 1;
    int count = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                if (lengths[j] + 1 > lengths[i]) {
                    lengths[i] = lengths[j] + 1;
                    counts[i] = counts[j];
                } else if (lengths[j] + 1 == lengths[i]) {
                    counts[i] += counts[j];
                }
            }
        }
        if (lengths[i] > maxLength) {
            maxLength = lengths[i];
            count = counts[i];
        } else if (lengths[i] == maxLength) {
            count += counts[i];
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums`. This is because we have a nested loop over `nums`.
> - **Space Complexity:** $O(n)$, as we need to store the `lengths` and `counts` arrays.
> - **Optimality proof:** This approach is optimal because we must at least look at each element in `nums` once, and we do so in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, iteration over arrays.
- Problem-solving patterns identified: Using dynamic programming to keep track of the length of the longest increasing subsequence ending at each position.
- Optimization techniques learned: Avoiding brute-force approaches, using dynamic programming to reduce time complexity.
- Similar problems to practice: Longest Increasing Subsequence, Shortest Path.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing arrays correctly, not updating variables correctly.
- Edge cases to watch for: Empty input array, array with a single element.
- Performance pitfalls: Using brute-force approaches, not using dynamic programming.
- Testing considerations: Test with different input sizes, test with different types of input (e.g. increasing, decreasing, random).