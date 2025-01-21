## Maximum and Sum of Array
**Problem Link:** https://leetcode.com/problems/maximum-and-sum-of-array/description

**Problem Statement:**
- Input: An integer array `nums` with a length of `n`, where `n >= 3`.
- Constraints: All elements in `nums` are non-negative integers.
- Expected Output: The maximum value of the sum of the array after performing the following operation at most once: Choose two elements from the array and replace them with their bitwise AND and bitwise OR, respectively.
- Key Requirements: The replacement should be done in a way that maximizes the sum of the array.
- Edge Cases: Handle arrays with duplicate elements, arrays with elements that have the same bitwise AND and OR, and arrays with elements that are powers of 2.

**Example Test Cases:**
- For `nums = [1, 2, 3, 4, 5]`, the maximum sum is `15`.
- For `nums = [6, 2]`, the maximum sum is `8`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible pairs of elements to replace with their bitwise AND and OR.
- This approach comes to mind first because it guarantees finding the maximum sum by considering all possible replacements.
- Step-by-step breakdown:
  1. Iterate over all pairs of elements in the array.
  2. For each pair, calculate the bitwise AND and OR.
  3. Replace the pair with their bitwise AND and OR in the array.
  4. Calculate the sum of the modified array.
  5. Update the maximum sum if the current sum is larger.

```cpp
#include <vector>
#include <algorithm>

int maximumSum(std::vector<int>& nums) {
    int maxSum = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            std::vector<int> temp = nums;
            int andVal = temp[i] & temp[j];
            int orVal = temp[i] | temp[j];
            temp.erase(temp.begin() + j);
            temp.erase(temp.begin() + i);
            temp.push_back(andVal);
            temp.push_back(orVal);
            int sum = 0;
            for (int k = 0; k < temp.size(); k++) {
                sum += temp[k];
            }
            maxSum = std::max(maxSum, sum);
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we have three nested loops: two for iterating over pairs of elements and one for calculating the sum of the modified array.
> - **Space Complexity:** $O(n)$, as we create a temporary array of the same size as the input array for each pair of elements.
> - **Why these complexities occur:** The brute force approach is computationally expensive due to the nested loops, and it requires additional space to store the temporary arrays.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is that the maximum sum is achieved by replacing the two smallest elements with their bitwise AND and OR.
- This is because the bitwise AND of two numbers is always less than or equal to the smaller of the two numbers, and the bitwise OR is always greater than or equal to the larger of the two numbers.
- By replacing the smallest elements, we minimize the decrease in the sum caused by the bitwise AND and maximize the increase caused by the bitwise OR.
- Step-by-step breakdown:
  1. Sort the array in ascending order.
  2. Calculate the bitwise AND and OR of the two smallest elements.
  3. Replace the two smallest elements with their bitwise AND and OR.
  4. Calculate the sum of the modified array.

```cpp
#include <vector>
#include <algorithm>

int maximumSum(std::vector<int>& nums) {
    std::sort(nums.begin(), nums.end());
    int andVal = nums[0] & nums[1];
    int orVal = nums[0] | nums[1];
    nums[0] = andVal;
    nums[1] = orVal;
    int sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        sum += nums[i];
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. This is because we sort the array, which has a time complexity of $O(n \log n)$.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the bitwise AND and OR values.
> - **Optimality proof:** This approach is optimal because it minimizes the decrease in the sum caused by the bitwise AND and maximizes the increase caused by the bitwise OR, resulting in the maximum possible sum.

---

### Final Notes
**Learning Points:**
- The importance of understanding bitwise operations and their properties.
- The concept of minimizing the decrease and maximizing the increase in a sum by replacing elements.
- The use of sorting to simplify the problem and reduce the time complexity.

**Mistakes to Avoid:**
- Not considering the properties of bitwise operations and their impact on the sum.
- Not sorting the array to simplify the problem and reduce the time complexity.
- Not replacing the smallest elements to minimize the decrease and maximize the increase in the sum.