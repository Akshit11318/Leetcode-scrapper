## Find the Count of Monotonic Pairs I

**Problem Link:** https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/description

**Problem Statement:**
- Given a `0-indexed` integer array `nums` of length `n`.
- A pair of indices `(i, j)` is `monotonic` if `i < j` and either `nums[i] <= nums[j]` or `nums[i] >= nums[j]`.
- The task is to find the count of `monotonic` pairs in the array.

### Brute Force Approach

**Explanation:**
- The initial thought process is to compare each element with every other element that comes after it.
- For each pair, check if the condition for being `monotonic` is satisfied.
- This approach comes to mind first because it directly implements the definition of `monotonic` pairs without considering any optimizations.

```cpp
class Solution {
public:
    int countMonotonicPairs(vector<int>& nums) {
        int count = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] <= nums[j] || nums[i] >= nums[j]) {
                    count++;
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because for each element, we are potentially comparing it with every other element that comes after it.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array. This is because we are only using a constant amount of space to store the count of `monotonic` pairs.
> - **Why these complexities occur:** The time complexity is high because of the nested loop structure, which results in quadratic time complexity. The space complexity is low because we are not using any additional data structures that scale with the input size.

### Optimal Approach (Required)

**Explanation:**
- The key insight here is to realize that every pair of elements will be considered `monotonic` because the condition allows for either `nums[i] <= nums[j]` or `nums[i] >= nums[j]`, which covers all possible pairs since for any two numbers, one will be less than or equal to the other or greater than or equal to the other.
- Thus, the problem simplifies to counting the total number of pairs in the array, which can be done using the formula for combinations: $C(n, 2) = \frac{n(n-1)}{2}$, where $n$ is the number of elements in the array.
- This approach is optimal because it avoids the need for explicit comparisons between elements, reducing the time complexity significantly.

```cpp
class Solution {
public:
    int countMonotonicPairs(vector<int>& nums) {
        int n = nums.size();
        return n * (n - 1) / 2;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are performing a constant number of operations regardless of the size of the input array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, because we are not using any additional data structures that scale with the input size.
> - **Optimality proof:** This is the optimal solution because we are directly calculating the result without any unnecessary comparisons or iterations, achieving the lowest possible time complexity.

### Final Notes

**Learning Points:**
- The importance of carefully reading the problem statement to identify simplifications or patterns that can lead to more efficient solutions.
- Understanding that not all problems require complex algorithms or data structures; sometimes, a straightforward mathematical approach can be the most efficient.
- Recognizing the difference between brute force and optimal approaches and striving for the latter in real-world applications.

**Mistakes to Avoid:**
- Assuming that every problem requires a complex solution without first considering simpler, more mathematical approaches.
- Not recognizing the patterns or properties of the input data that could simplify the solution.
- Failing to consider the scalability of the solution, especially for large input sizes.