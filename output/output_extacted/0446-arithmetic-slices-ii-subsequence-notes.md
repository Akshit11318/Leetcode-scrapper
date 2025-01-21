## Arithmetic Slices II - Subsequence
**Problem Link:** https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums`, return the number of all possible **arithmetic subsequences** of length at least `3`.
- Expected output format: The function should return an integer representing the total count of arithmetic subsequences.
- Key requirements and edge cases to consider: 
    - The input array `nums` has a length of at most `1000`.
    - The integers in `nums` are in the range `[1, 1000]`.
    - The sequence should be strictly increasing, i.e., each element is greater than the previous one.
- Example test cases with explanations:
    - For `nums = [2, 4, 6, 8, 10]`, the output is `7` because there are `7` arithmetic subsequences: `[2, 4, 6]`, `[2, 4, 8]`, `[2, 4, 10]`, `[2, 6, 10]`, `[4, 6, 8]`, `[4, 6, 10]`, and `[6, 8, 10]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking every possible subsequence of the input array `nums`.
- Step-by-step breakdown of the solution:
    1. Generate all possible subsequences of `nums`.
    2. For each subsequence, check if it is an arithmetic sequence by verifying that the difference between consecutive elements is constant.
    3. Count the number of arithmetic subsequences with a length of at least `3`.
- Why this approach comes to mind first: It is the most straightforward method, but it is inefficient due to the large number of subsequences.

```cpp
#include <vector>
using namespace std;

int numberOfArithmeticSlices(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int diff = nums[j] - nums[i];
            int k = j + 1;
            while (k < n) {
                if (nums[k] - nums[j] == diff) {
                    count++;
                    j = k;
                }
                k++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`. This is because for each pair of elements, we potentially iterate through the rest of the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and indices.
> - **Why these complexities occur:** The time complexity is high due to the nested loops, and the space complexity is low because we do not use any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hashmap to store the last seen index for each difference.
- Detailed breakdown of the approach:
    1. Initialize a hashmap `dp` where `dp[i][diff]` represents the number of arithmetic subsequences ending at index `i` with difference `diff`.
    2. Iterate through `nums`, and for each element, update `dp` based on the differences with previous elements.
    3. The total count of arithmetic subsequences is the sum of `dp[i][diff]` for all `i` and `diff`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input array and uses a hashmap to efficiently store and retrieve information about the subsequences.

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

int numberOfArithmeticSlices(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    unordered_map<int, unordered_map<int, int>> dp;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            int diff = nums[i] - nums[j];
            if (dp[j].find(diff) != dp[j].end()) {
                dp[i][diff] += dp[j][diff];
            }
            dp[i][diff]++;
            if (dp[i].find(diff) != dp[i].end() && dp[i][diff] >= 3) {
                count += dp[i][diff] - 2;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums`. This is because we iterate through the array and for each element, we potentially iterate through all previous elements.
> - **Space Complexity:** $O(n^2)$, as we use a hashmap to store the last seen index for each difference, which can grow up to the size of the input array squared in the worst case.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from $O(n^3)$ to $O(n^2)$ by using a hashmap to store and retrieve information about the subsequences efficiently.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using hashmaps to store and retrieve information efficiently, reducing time complexity by avoiding redundant calculations.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and using dynamic programming to solve them.
- Optimization techniques learned: Using hashmaps to reduce time complexity, avoiding redundant calculations by storing intermediate results.
- Similar problems to practice: Other problems involving subsequences, such as finding the longest increasing subsequence or the longest common subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the hashmap correctly, not updating the count correctly.
- Edge cases to watch for: Handling the case where the input array is empty or has only one element.
- Performance pitfalls: Using a brute force approach, not using a hashmap to store and retrieve information efficiently.
- Testing considerations: Testing the function with different input arrays, including edge cases, to ensure it works correctly.