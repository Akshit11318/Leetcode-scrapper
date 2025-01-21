## Patching Array
**Problem Link:** https://leetcode.com/problems/patching-array/description

**Problem Statement:**
- Given a sorted integer array `nums` and an integer `n`, return the minimum number of operations required to make every number in the range `[1, n]` (inclusive) a possible sum of elements from `nums`. You can perform two types of operations:
  - Add an element from the range `[1, n]` to `nums`.
  - Use an existing element in `nums` to form a sum.
- The input array `nums` is sorted in ascending order.
- The input integer `n` represents the upper limit of the range.
- The goal is to find the minimum number of operations required to make all numbers in the range `[1, n]` possible sums.

**Example Test Cases:**
- Input: `nums = [1, 3], n = 6`
  - Output: `1`
  - Explanation: Adding `2` to `nums` allows all numbers from `1` to `6` to be formed as sums: `1`, `2`, `3`, `1+3=4`, `2+3=5`, and `1+2+3=6`.
- Input: `nums = [1, 5, 10, 100], n = 20`
  - Output: `2`
  - Explanation: Adding `2` and `4` to `nums` allows all numbers from `1` to `20` to be formed as sums.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible sums that can be formed using the elements of `nums`.
- For each number in the range `[1, n]`, check if it can be formed as a sum of elements from `nums`.
- If a number cannot be formed, add it to `nums` and continue checking the remaining numbers.
- This approach is straightforward but inefficient due to its exponential time complexity.

```cpp
#include <vector>
using namespace std;

int minPatches(vector<int>& nums, int n) {
    int count = 0;
    int i = 0;
    int miss = 1;
    while (miss <= n) {
        if (i < nums.size() && nums[i] <= miss) {
            miss += nums[i];
            i++;
        } else {
            count++;
            miss *= 2;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the input integer and $m$ is the size of `nums`, because in the worst case, we might need to iterate through all numbers up to $n$ and all elements in `nums`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables.
> - **Why these complexities occur:** The time complexity is linear because we potentially iterate through all numbers in the range and all elements in `nums`, and the space complexity is constant because we use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to maintain a variable `miss` that represents the smallest number that cannot be formed as a sum of elements from `nums`.
- We start with `miss = 1` because `1` is the smallest possible number.
- We iterate through `nums`, and for each element, if it is less than or equal to `miss`, we add it to `miss` because we can now form all numbers up to `miss + nums[i]`.
- If we encounter an element greater than `miss`, it means we cannot form `miss`, so we increment the count of operations and update `miss` to `miss * 2`, effectively adding `miss` to `nums` to make all numbers up to `miss * 2` possible sums.
- This approach is optimal because it minimizes the number of operations required by always adding the smallest possible number to make the largest range of numbers possible sums.

```cpp
#include <vector>
using namespace std;

int minPatches(vector<int>& nums, int n) {
    int count = 0;
    int i = 0;
    long long miss = 1;
    while (miss <= n) {
        if (i < nums.size() && (long long)nums[i] <= miss) {
            miss += nums[i];
            i++;
        } else {
            count++;
            miss *= 2;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m + \log(n))$ where $m$ is the size of `nums` and $n$ is the input integer, because we iterate through `nums` and potentially update `miss` a number of times proportional to the logarithm of $n$.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because it always chooses the smallest possible number to add to `nums` to make the largest range of numbers possible sums, thereby minimizing the number of operations required.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the use of a greedy algorithm to find the minimum number of operations required to achieve a certain goal.
- It highlights the importance of maintaining a variable that tracks the smallest number that cannot be formed as a sum of elements from `nums`.
- The solution shows how to optimize the approach by always adding the smallest possible number to make the largest range of numbers possible sums.

**Mistakes to Avoid:**
- Not considering the use of a greedy algorithm to solve the problem.
- Failing to maintain a variable that tracks the smallest number that cannot be formed as a sum of elements from `nums`.
- Not optimizing the approach by always adding the smallest possible number to make the largest range of numbers possible sums.