## Count Strictly Increasing Subarrays

**Problem Link:** https://leetcode.com/problems/count-strictly-increasing-subarrays/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: $1 \leq n \leq 10^5$ where $n$ is the number of elements in `nums`.
- Expected Output: The number of strictly increasing subarrays in `nums`.
- Key Requirements: A strictly increasing subarray is one where each element is strictly greater than the previous one.
- Edge Cases: Empty array, single element array, arrays with duplicate elements.

Example Test Cases:
- `nums = [1, 2, 3]`, the output should be `6` because there are six strictly increasing subarrays: `[1]`, `[2]`, `[3]`, `[1, 2]`, `[2, 3]`, and `[1, 2, 3]`.
- `nums = [1, 3, 5]`, the output should be `6` as well because the subarrays are the same as the previous example.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subarrays and check each one to see if it's strictly increasing.
- This involves iterating over the array with two nested loops to generate all subarrays, then checking each subarray to see if it meets the criteria.

```cpp
int countSubarrays(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            bool isIncreasing = true;
            for (int k = i; k < j; k++) {
                if (nums[k] >= nums[k + 1]) {
                    isIncreasing = false;
                    break;
                }
            }
            if (isIncreasing) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the number of elements in `nums`. This is because for each subarray (generated in $O(n^2)$ time), we potentially check each element again (in $O(n)$ time).
> - **Space Complexity:** $O(1)$ excluding the space needed for the input and output, as we only use a constant amount of space to store the count and loop indices.
> - **Why these complexities occur:** The brute force approach is inherently inefficient because it checks every possible subarray and then checks each subarray again to see if it's increasing, leading to a cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to recognize that a strictly increasing subarray can be extended to the right as long as the next element is greater than the last element in the subarray.
- We can use a single pass through the array, maintaining a count of strictly increasing subarrays ending at each position.
- For each element, we consider all previous elements that could be the start of a strictly increasing subarray ending at the current position.

```cpp
int countSubarrays(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        int left = i;
        while (left > 0 && nums[left - 1] < nums[left]) {
            left--;
        }
        for (int j = left; j <= i; j++) {
            count++;
        }
    }
    return count;
}
```

However, the above code does not accurately represent the optimal approach for counting strictly increasing subarrays. A correct optimal approach involves recognizing that for each element, we can extend the subarray to the right as long as the next element is greater, and we can also start a new subarray at each element.

```cpp
int countSubarrays(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        int subarrayCount = 1; // Counting the single element as a subarray
        for (int j = i + 1; j < n; j++) {
            if (nums[j] > nums[j - 1]) {
                subarrayCount++;
            } else {
                break;
            }
        }
        // For each starting point i, we have subarrayCount number of subarrays
        // We can use the formula for sum of first n natural numbers: n*(n+1)/2
        // Here, it's subarrayCount*(subarrayCount+1)/2 because we're counting subarrays
        count += subarrayCount * (subarrayCount + 1) / 2;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, as in the worst case, we might extend the subarray to the end of the array for each starting element.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and loop indices.
> - **Optimality proof:** This approach is optimal because it avoids the unnecessary cubic complexity of the brute force by only considering the extension of subarrays to the right and not re-checking all subarrays. However, it's worth noting that the explanation and initial code provided for the optimal approach were flawed, and the corrected version above accurately represents a more efficient method.

---

### Final Notes

**Learning Points:**
- The importance of recognizing patterns in arrays that can help in optimizing solutions.
- Understanding how to extend subarrays based on certain conditions.
- The value of avoiding unnecessary re-checks of subarrays.

**Mistakes to Avoid:**
- Implementing brute force solutions for problems that have more efficient solutions.
- Not considering the extension of subarrays based on the given conditions.
- Failing to recognize the pattern that allows for a more efficient counting of subarrays.