## Sum of Absolute Differences in a Sorted Array

**Problem Link:** https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description

**Problem Statement:**
- Input format: A sorted array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `-10^5 <= nums[i] <= 10^5`, and `1 <= k <= nums.length`.
- Expected output format: The sum of absolute differences between `k` and each element in `nums`.
- Key requirements and edge cases to consider: The array is sorted, and `k` is within the bounds of the array length.
- Example test cases with explanations:
  - Example 1: `nums = [2, 3, 5], k = 2`, expected output is `3` because `|2-2| + |3-2| + |5-2| = 0 + 1 + 3 = 4` is incorrect, we need to calculate the sum for each possible `k` in the array and return the minimum sum.
  - Example 2: `nums = [1, 3, 5, 7], k = 4`, expected output is `4` because we can insert `4` into the array to get `[1, 3, 4, 5, 7]`, and then calculate the sum of absolute differences.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over each element in the array and calculate the absolute difference between `k` and each element.
- Step-by-step breakdown of the solution:
  1. Iterate over each element in the array.
  2. For each element, calculate the absolute difference between `k` and the element.
  3. Sum up all the absolute differences.
- Why this approach comes to mind first: It is a straightforward approach that directly calculates the sum of absolute differences.

```cpp
int sumAbsoluteDifferences(vector<int>& nums, int k) {
    int sum = 0;
    for (int num : nums) {
        sum += abs(num - k);
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array, because we iterate over each element in the array once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the sum.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each element in the array, and the space complexity is constant because we only use a fixed amount of space to store the sum.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the array is sorted, we can use the fact that the absolute difference between two numbers is minimized when the two numbers are closest to each other.
- Detailed breakdown of the approach:
  1. Find the index of the element in the array that is closest to `k`.
  2. Calculate the sum of absolute differences for the elements before and after the closest element.
- Proof of optimality: This approach is optimal because it takes advantage of the fact that the array is sorted, allowing us to find the closest element to `k` in linear time.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem because we must at least read the input array once.

```cpp
int sumAbsoluteDifferences(vector<int>& nums, int k) {
    int n = nums.size();
    int sum = 0;
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == k) {
            break;
        } else if (nums[mid] < k) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    int idx = left;
    for (int i = 0; i < n; i++) {
        sum += abs(nums[i] - k);
    }
    int minSum = sum;
    for (int i = 0; i < n; i++) {
        sum -= abs(nums[i] - k);
        sum += abs(nums[i] - nums[i]);
        minSum = min(minSum, sum);
    }
    return minSum;
}
```

However, the above code is still not optimal as we are iterating over the array multiple times. 

Let's consider a better approach:

We can use the fact that the sum of absolute differences is minimized when `k` is the median of the array. 

```cpp
int sumAbsoluteDifferences(vector<int>& nums, int k) {
    int n = nums.size();
    int sum = 0;
    for (int num : nums) {
        sum += abs(num - k);
    }
    int minSum = sum;
    for (int i = 0; i < n; i++) {
        sum -= abs(nums[i] - k);
        sum += abs(nums[i] - nums[i]);
        minSum = min(minSum, sum);
    }
    return minSum;
}
```

But still this is not optimal as we are iterating over the array multiple times.

Let's consider an optimal approach:

We can calculate the sum of absolute differences in a single pass by maintaining two variables: `leftSum` and `rightSum`. 

```cpp
int sumAbsoluteDifferences(vector<int>& nums, int k) {
    int n = nums.size();
    int minSum = INT_MAX;
    for (int i = 0; i < n; i++) {
        int leftSum = 0, rightSum = 0;
        for (int j = 0; j < i; j++) {
            leftSum += abs(nums[j] - nums[i]);
        }
        for (int j = i + 1; j < n; j++) {
            rightSum += abs(nums[j] - nums[i]);
        }
        minSum = min(minSum, leftSum + rightSum);
    }
    return minSum;
}
```

This approach still has a time complexity of $O(n^2)$.

To achieve a time complexity of $O(n)$, we can use the following approach:

We can calculate the sum of absolute differences in a single pass by maintaining two variables: `leftSum` and `rightSum`. 

```cpp
int sumAbsoluteDifferences(vector<int>& nums, int k) {
    int n = nums.size();
    int minSum = INT_MAX;
    for (int i = 0; i < n; i++) {
        int leftSum = 0, rightSum = 0;
        for (int j = 0; j < i; j++) {
            leftSum += nums[i] - nums[j];
        }
        for (int j = i + 1; j < n; j++) {
            rightSum += nums[j] - nums[i];
        }
        minSum = min(minSum, leftSum + rightSum);
    }
    return minSum;
}
```

However, the above code is still not optimal.

Let's consider an optimal approach:

We can calculate the sum of absolute differences in a single pass by maintaining two variables: `leftSum` and `rightSum`. 

```cpp
int sumAbsoluteDifferences(vector<int>& nums, int k) {
    int n = nums.size();
    int minSum = INT_MAX;
    for (int i = 0; i < n; i++) {
        int leftSum = i * nums[i] - (i > 0 ? accumulate(nums.begin(), nums.begin() + i, 0LL) : 0);
        int rightSum = (accumulate(nums.begin() + i + 1, nums.end(), 0LL)) - (n - i - 1) * nums[i];
        minSum = min(minSum, leftSum + rightSum);
    }
    return minSum;
}
```

This approach still has a time complexity of $O(n^2)$ due to the `accumulate` function.

To achieve a time complexity of $O(n)$, we can use the following approach:

We can calculate the sum of absolute differences in a single pass by maintaining two variables: `leftSum` and `rightSum`. 

```cpp
int sumAbsoluteDifferences(vector<int>& nums, int k) {
    int n = nums.size();
    int minSum = INT_MAX;
    long long prefixSum = 0;
    for (int i = 0; i < n; i++) {
        int leftSum = i * nums[i] - prefixSum;
        int rightSum = (long long)accumulate(nums.begin() + i + 1, nums.end(), 0LL) - (n - i - 1) * nums[i];
        minSum = min(minSum, leftSum + rightSum);
        prefixSum += nums[i];
    }
    return minSum;
}
```

However, the above code is still not optimal as we are using the `accumulate` function.

Let's consider an optimal approach:

We can calculate the sum of absolute differences in a single pass by maintaining two variables: `leftSum` and `rightSum`. 

```cpp
int sumAbsoluteDifferences(vector<int>& nums, int k) {
    int n = nums.size();
    int minSum = INT_MAX;
    long long prefixSum = 0;
    long long suffixSum = 0;
    for (int num : nums) {
        suffixSum += num;
    }
    for (int i = 0; i < n; i++) {
        int leftSum = i * nums[i] - prefixSum;
        int rightSum = suffixSum - prefixSum - nums[i] - (n - i - 1) * nums[i];
        minSum = min(minSum, leftSum + rightSum);
        prefixSum += nums[i];
        suffixSum -= nums[i];
    }
    return minSum;
}
```

This approach has a time complexity of $O(n)$ and a space complexity of $O(1)$.

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array, because we iterate over each element in the array once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the sum.
> - **Optimality proof:** This approach is optimal because it takes advantage of the fact that the array is sorted, allowing us to find the sum of absolute differences in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of using prefix and suffix sums to calculate the sum of absolute differences in a single pass.
- Problem-solving patterns identified: Using a single pass to calculate the sum of absolute differences.
- Optimization techniques learned: Using prefix and suffix sums to reduce the time complexity.
- Similar problems to practice: Other problems that involve calculating sums of absolute differences.

**Mistakes to Avoid:**
- Common implementation errors: Using the `accumulate` function, which has a time complexity of $O(n)$.
- Edge cases to watch for: The case where the array is empty.
- Performance pitfalls: Using a time complexity of $O(n^2)$ or higher.
- Testing considerations: Testing the code with large inputs to ensure that it has a time complexity of $O(n)$.