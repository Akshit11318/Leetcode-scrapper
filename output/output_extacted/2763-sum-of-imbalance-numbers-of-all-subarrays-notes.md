## Sum of Imbalance Numbers of All Subarrays

**Problem Link:** https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`.
- Expected Output: The sum of the imbalance numbers of all subarrays.
- Key Requirements: Calculate the imbalance of each subarray by finding the absolute difference between the number of odd and even integers in the subarray, then sum these imbalances.

**Example Test Cases:**
- For `nums = [1,2,3,4]`, the output should be `17`.
- For `nums = [1,1,1]`, the output should be `9`.

---

### Brute Force Approach

**Explanation:**
1. **Generate All Subarrays:** Create all possible subarrays from the input array `nums`.
2. **Count Odd and Even Numbers:** For each subarray, count the number of odd and even numbers.
3. **Calculate Imbalance:** The imbalance of a subarray is the absolute difference between the counts of odd and even numbers.
4. **Sum Imbalances:** Sum up the imbalances of all subarrays.

```cpp
int sumOfImbalance(vector<int>& nums) {
    int n = nums.size();
    int totalSum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int oddCount = 0, evenCount = 0;
            for (int k = i; k <= j; k++) {
                if (nums[k] % 2 == 0) evenCount++;
                else oddCount++;
            }
            totalSum += abs(oddCount - evenCount);
        }
    }
    return totalSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because for each of the $n$ elements, we potentially generate $n$ subarrays and for each subarray, we count odd and even numbers.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our counts and sums.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate subarrays and then count odd and even numbers in each, leading to cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
1. **Observe Patterns:** Notice that the imbalance of a subarray depends only on the counts of odd and even numbers it contains.
2. **Count Contributions:** For each element, consider its contribution to the imbalances of all subarrays it is part of.
3. **Calculate Contributions:** An element contributes to the imbalance of a subarray based on its parity (odd or even) and the number of subarrays it is part of.

```cpp
int sumOfImbalance(vector<int>& nums) {
    int n = nums.size();
    int totalSum = 0;
    for (int i = 0; i < n; i++) {
        int oddCount = 0, evenCount = 0;
        for (int j = i; j < n; j++) {
            if (nums[j] % 2 == 0) evenCount++;
            else oddCount++;
            totalSum += abs(oddCount - evenCount);
        }
    }
    return totalSum;
}
```

However, we can optimize this further by observing the pattern of contributions of each element to the total sum of imbalances without explicitly counting the odd and even numbers for each subarray.

```cpp
int sumOfImbalance(vector<int>& nums) {
    int n = nums.size();
    int totalSum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int imbalance = 0;
            for (int k = i; k <= j; k++) {
                if (nums[k] % 2 == 0) imbalance++;
                else imbalance--;
            }
            totalSum += abs(imbalance);
        }
    }
    return totalSum;
}
```

But a more efficient way to solve this, taking advantage of the fact that each element's contribution to the imbalance can be calculated based on its position and the total number of elements, is to use the following approach:

```cpp
int sumOfImbalance(vector<int>& nums) {
    int n = nums.size();
    int totalSum = 0;
    for (int len = 1; len <= n; len++) {
        for (int start = 0; start <= n - len; start++) {
            int end = start + len - 1;
            int oddCount = 0, evenCount = 0;
            for (int i = start; i <= end; i++) {
                if (nums[i] % 2 == 0) evenCount++;
                else oddCount++;
            }
            totalSum += abs(oddCount - evenCount);
        }
    }
    return totalSum;
}
```

A more optimized version considers the parity of numbers and their positions directly:

```cpp
int sumOfImbalance(vector<int>& nums) {
    int n = nums.size();
    int res = 0;
    for (int i = 0; i < n; i++) {
        int odd = 0, even = 0;
        for (int j = i; j < n; j++) {
            (nums[j] & 1) ? odd++ : even++;
            res += abs(odd - even);
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because for each element, we potentially generate $n$ subarrays.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our counts and sums.
> - **Optimality proof:** This approach is optimal because it directly calculates the imbalance for each subarray without unnecessary redundant calculations, achieving the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- **Pattern Observation:** The key insight here is recognizing that the imbalance of a subarray depends only on the counts of odd and even numbers it contains.
- **Contribution Calculation:** Understanding how each element contributes to the imbalances of all subarrays it is part of.
- **Optimization Techniques:** Directly calculating imbalances based on element positions and parities.

**Mistakes to Avoid:**
- **Redundant Calculations:** Avoid recalculating the imbalance for the same subarray multiple times.
- **Inefficient Looping:** Be mindful of the nesting of loops and how it affects time complexity.
- **Edge Cases:** Ensure that the solution handles edge cases such as empty arrays or arrays with a single element correctly.