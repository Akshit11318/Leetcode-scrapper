## Semi-Ordered Permutation

**Problem Link:** https://leetcode.com/problems/semi-ordered-permutation/description

**Problem Statement:**
- Given an integer `n`, return the number of semi-ordered permutations of length `n`. 
- A permutation of length `n` is an array of `n` distinct integers from `1` to `n` in a specific order.
- A permutation is considered semi-ordered if for every pair of elements `a` and `b` in the permutation where `a` is not equal to `b`, if `a` is odd, then `a` must come before `b` in the permutation.
- The function should return the total number of such permutations.

**Expected Output Format:**
- The function should return a single integer representing the total number of semi-ordered permutations.

**Key Requirements and Edge Cases:**
- The input `n` will be a positive integer.
- The function should handle large inputs efficiently.

**Example Test Cases with Explanations:**
- For `n = 2`, there are 2 semi-ordered permutations: `[1, 2]` and `[2, 1]`.
- For `n = 3`, there are 4 semi-ordered permutations: `[1, 2, 3]`, `[1, 3, 2]`, `[3, 1, 2]`, and `[3, 2, 1]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible permutations of length `n` and then check each permutation to see if it satisfies the semi-ordered condition.
- This approach involves using a recursive function to generate all permutations and then iterating over each permutation to check the condition.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int countSemiOrdered(int n) {
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        nums[i] = i + 1;
    }
    
    int count = 0;
    do {
        bool isSemiOrdered = true;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] % 2 == 1 && nums[i] > nums[j]) {
                    isSemiOrdered = false;
                    break;
                }
            }
            if (!isSemiOrdered) break;
        }
        if (isSemiOrdered) count++;
    } while (next_permutation(nums.begin(), nums.end()));
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n^2)$, where $n!$ is the number of permutations and $n^2$ is the time to check each permutation.
> - **Space Complexity:** $O(n)$, where $n$ is the space needed to store the current permutation.
> - **Why these complexities occur:** The brute force approach generates all permutations and checks each one, resulting in a high time complexity. The space complexity is low because we only need to store the current permutation.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to recognize that the semi-ordered condition only depends on the parity of the numbers, not their actual values.
- We can use the concept of `factorial` to calculate the number of semi-ordered permutations directly.
- For each odd number, we can place it in any of the `n` positions, and for each even number, we can place it in any of the remaining positions.
- This results in a much more efficient calculation.

```cpp
int countSemiOrdered(int n) {
    long long count = 1;
    for (int i = 1; i <= n / 2; i++) {
        count *= (2 * i);
    }
    for (int i = 1; i <= n - n / 2; i++) {
        count *= i;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of iterations to calculate the factorials.
> - **Space Complexity:** $O(1)$, where the space is constant and does not depend on the input size.
> - **Optimality proof:** This approach is optimal because it directly calculates the number of semi-ordered permutations using the properties of factorials, avoiding the need to generate and check all permutations.

---

### Final Notes

**Learning Points:**
- The importance of recognizing patterns and properties of the problem to avoid brute force approaches.
- The use of factorials to calculate permutations.
- The concept of semi-ordered permutations and how to calculate them efficiently.

**Mistakes to Avoid:**
- Using brute force approaches for large inputs.
- Not recognizing the properties of the problem that can lead to more efficient solutions.
- Not considering the use of factorials to calculate permutations.

---