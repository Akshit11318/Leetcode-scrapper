## Find the Most Competitive Subsequence
**Problem Link:** https://leetcode.com/problems/find-the-most-competitive-subsequence/description

**Problem Statement:**
- Input format: Given an integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 100`, `1 <= nums[i] <= 1000`, `1 <= k <= nums.length`.
- Expected output format: Find the most competitive subsequence of length `k` from the given array `nums`.
- Key requirements: A subsequence is considered more competitive if it is smaller lexicographically.
- Edge cases to consider: When `k` equals the length of `nums`, the most competitive subsequence is the array itself.
- Example test cases:
  - Input: `nums = [3,5,2,6], k = 2`
    - Output: `[2,6]`
    - Explanation: Among the possible subsequences of length 2, `[2,6]` is the most competitive.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of length `k` from `nums` and compare them to find the smallest one lexicographically.
- Step-by-step breakdown:
  1. Generate all subsequences of length `k`.
  2. Compare each subsequence lexicographically.
  3. Return the smallest subsequence found.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> mostCompetitive(std::vector<int>& nums, int k) {
    int n = nums.size();
    std::vector<int> result(k);
    std::vector<int> temp;
    
    // Function to generate all subsequences
    std::function<void(int, int)> generateSubsequences = 
        [&](int start, int count) {
            if (count == k) {
                // Compare the generated subsequence with the current result
                if (temp.size() > 0 && (result.size() == 0 || temp < result)) {
                    result = temp;
                }
                return;
            }
            
            for (int i = start; i <= n - (k - count); ++i) {
                temp.push_back(nums[i]);
                generateSubsequences(i + 1, count + 1);
                temp.pop_back();
            }
        };
    
    generateSubsequences(0, 0);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot k \cdot log(k))$, where $n$ is the length of `nums`. This is because we generate all possible subsequences, and for each, we compare it with the current result which involves sorting or lexicographical comparison.
> - **Space Complexity:** $O(k)$, for storing the subsequence and temporary storage.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsequences, and the space complexity is due to storing these subsequences.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a stack to keep track of the most competitive subsequence seen so far. We iterate through `nums` and at each step, we decide whether to push the current number onto the stack or not, based on whether it's smaller than the top of the stack and if we have enough room left in the subsequence.
- Detailed breakdown:
  1. Initialize an empty stack.
  2. Iterate through `nums`. For each number, while the stack is not empty, the top of the stack is greater than the current number, and we have more than `k` numbers left to fill the subsequence, pop the top of the stack.
  3. Push the current number onto the stack if the stack's size is less than `k`.
  4. After iterating through all numbers, the stack contains the most competitive subsequence of length `k`.

```cpp
std::vector<int> mostCompetitive(std::vector<int>& nums, int k) {
    std::vector<int> stack;
    for (int i = 0; i < nums.size(); ++i) {
        while (!stack.empty() && stack.back() > nums[i] && stack.size() + nums.size() - i > k) {
            stack.pop_back();
        }
        if (stack.size() < k) {
            stack.push_back(nums[i]);
        }
    }
    return stack;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because each number in `nums` is pushed and popped from the stack at most once.
> - **Space Complexity:** $O(k)$, for storing the stack.
> - **Optimality proof:** This approach is optimal because it ensures that at each step, we have the most competitive subsequence seen so far, and it does so in linear time, which is the best we can achieve given that we must at least read the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Using a stack to keep track of the most competitive subsequence, and the insight that we can decide to include or exclude a number from the subsequence based on its comparison with the top of the stack and the remaining length of the subsequence.
- Problem-solving patterns: The use of a stack to solve problems involving subsequences or sequences, and the importance of considering the remaining length of the subsequence when making decisions.
- Optimization techniques: Avoiding unnecessary comparisons and operations by using a stack and considering the constraints of the problem.

**Mistakes to Avoid:**
- Not considering the remaining length of the subsequence when deciding to include or exclude a number.
- Not using a stack to efficiently keep track of the most competitive subsequence.
- Not optimizing the comparison process to avoid unnecessary operations.