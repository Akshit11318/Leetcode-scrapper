## Minimum Equal Sum of Two Arrays After Replacing Zeros

**Problem Link:** https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description

**Problem Statement:**
- Given two arrays `nums1` and `nums2`, both of length `n`, find the minimum sum that can be achieved by replacing zeros in either array with a value that makes the sum of both arrays equal.
- Input format and constraints: Two integer arrays `nums1` and `nums2` with the same length `n`.
- Expected output format: The minimum sum of the two arrays after replacing zeros.
- Key requirements and edge cases to consider: Handling cases where one or both arrays contain zeros, and ensuring the sum of the two arrays is equal after replacement.
- Example test cases with explanations: 
    - For `nums1 = [0,1,2,3]` and `nums2 = [0,3,2,1]`, the output should be `10` because we can replace the zeros in both arrays with `4` to achieve equal sums.
    - For `nums1 = [0,0,0,0]` and `nums2 = [1,2,3,4]`, the output should be `10` because we can replace the zeros in `nums1` with values that make the sums equal.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through all possible combinations of replacing zeros in both arrays and calculate the sum for each combination.
- For each combination, check if the sums of the two arrays are equal.
- If they are equal, calculate the total sum of both arrays.
- Keep track of the minimum total sum found across all combinations.

```cpp
#include <vector>
#include <algorithm>

int minimumSum(std::vector<int>& nums1, std::vector<int>& nums2) {
    int sum1 = 0, sum2 = 0;
    for (int num : nums1) sum1 += num;
    for (int num : nums2) sum2 += num;
    
    // Brute force approach: Try all possible values for replacing zeros
    int minSum = INT_MAX;
    for (int i = 0; i <= 100; ++i) {
        for (int j = 0; j <= 100; ++j) {
            int newSum1 = sum1, newSum2 = sum2;
            for (int k = 0; k < nums1.size(); ++k) {
                if (nums1[k] == 0) newSum1 += i;
                if (nums2[k] == 0) newSum2 += j;
            }
            if (newSum1 == newSum2) {
                minSum = std::min(minSum, newSum1);
            }
        }
    }
    return minSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times 100^2)$ where $n$ is the length of the input arrays. This is because we are trying all possible values for replacing zeros in both arrays.
> - **Space Complexity:** $O(1)$ since we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The brute force approach involves nested loops to try all possible combinations of replacing zeros, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we only need to consider the difference between the sums of the two arrays.
- We can calculate the initial difference between the sums of the two arrays.
- Then, we can try to make the sums equal by replacing zeros in the array with the smaller sum.
- We keep track of the minimum number of replacements needed to make the sums equal.

```cpp
#include <vector>
#include <algorithm>

int minimumSum(std::vector<int>& nums1, std::vector<int>& nums2) {
    int sum1 = 0, sum2 = 0;
    for (int num : nums1) sum1 += num;
    for (int num : nums2) sum2 += num;
    
    int diff = std::abs(sum1 - sum2);
    int zeros1 = 0, zeros2 = 0;
    for (int num : nums1) if (num == 0) zeros1++;
    for (int num : nums2) if (num == 0) zeros2++;
    
    int replacements = std::min(zeros1, zeros2);
    int minSum = std::min(sum1, sum2) + replacements * (diff / replacements + (diff % replacements != 0));
    
    return minSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the input arrays. This is because we are making a single pass through the input arrays.
> - **Space Complexity:** $O(1)$ since we are not using any additional space that scales with the input size.
> - **Optimality proof:** This approach is optimal because we are directly calculating the minimum number of replacements needed to make the sums equal, without trying all possible combinations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Calculating the difference between sums, using the minimum number of replacements to make sums equal.
- Problem-solving patterns identified: Direct calculation, avoiding brute force approaches.
- Optimization techniques learned: Using the minimum number of replacements, avoiding unnecessary iterations.
- Similar problems to practice: Problems involving making two values equal by replacing or modifying elements.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the difference between sums, not considering the minimum number of replacements.
- Edge cases to watch for: Handling cases where one or both arrays contain zeros, ensuring the sum of the two arrays is equal after replacement.
- Performance pitfalls: Using brute force approaches, not optimizing the solution for large input sizes.
- Testing considerations: Testing the solution with different input sizes, including edge cases and large inputs.