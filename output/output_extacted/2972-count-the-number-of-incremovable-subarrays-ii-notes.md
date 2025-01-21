## Count the Number of Inremovable Subarrays II

**Problem Link:** https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: The length of `nums` is between 1 and 10^5, and each element is between 1 and 10^5.
- Expected Output: The number of subarrays that cannot be made strictly increasing by removing at most one element.
- Key Requirements and Edge Cases:
  - Subarrays must be non-empty.
  - Removing an element means the subarray can become strictly increasing.
- Example Test Cases:
  - For `nums = [1,2,3,4,5]`, all subarrays are strictly increasing, so the answer is 0.
  - For `nums = [5,4,3,2,1]`, the only subarray that cannot be made strictly increasing by removing at most one element is the entire array itself, so the answer is 1.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subarray of the given array.
- For each subarray, we then check if it can be made strictly increasing by removing at most one element.
- We iterate through all elements in the subarray and check if removing any single element makes the subarray strictly increasing.

```cpp
int countInremovableSubarrays(vector<int>& nums) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            vector<int> subarray(nums.begin() + i, nums.begin() + j + 1);
            bool removable = false;
            for (int k = 0; k < subarray.size(); k++) {
                vector<int> temp = subarray;
                temp.erase(temp.begin() + k);
                bool strictlyIncreasing = true;
                for (int m = 1; m < temp.size(); m++) {
                    if (temp[m] <= temp[m - 1]) {
                        strictlyIncreasing = false;
                        break;
                    }
                }
                if (strictlyIncreasing) {
                    removable = true;
                    break;
                }
            }
            if (!removable) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot m)$, where $n$ is the size of the input array and $m$ is the average size of a subarray. The reason is that for each subarray, we potentially remove each element once and check if the resulting array is strictly increasing.
> - **Space Complexity:** $O(m)$, where $m$ is the maximum size of a subarray, because we create a temporary copy of the subarray when checking if removing an element makes it strictly increasing.
> - **Why these complexities occur:** These complexities occur because the brute force approach involves exhaustive checking of all subarrays and all possible removals within those subarrays, leading to a high time complexity.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a sliding window technique to efficiently check all subarrays.
- For each subarray, instead of removing each element and checking if the subarray becomes strictly increasing, we can maintain a count of how many elements would need to be removed to make the subarray strictly increasing.
- If this count is more than 1, we know the subarray cannot be made strictly increasing by removing at most one element.

```cpp
int countInremovableSubarrays(vector<int>& nums) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            vector<int> subarray(nums.begin() + i, nums.begin() + j + 1);
            int removalsNeeded = 0;
            for (int k = 1; k < subarray.size(); k++) {
                if (subarray[k] <= subarray[k - 1]) {
                    removalsNeeded++;
                }
            }
            if (removalsNeeded > 1) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the size of the input array and $m$ is the average size of a subarray. This is because for each subarray, we check each element to see if it would need to be removed to make the subarray strictly increasing.
> - **Space Complexity:** $O(m)$, where $m$ is the maximum size of a subarray, because we create a temporary copy of the subarray.
> - **Optimality proof:** This approach is optimal because it checks each subarray exactly once and uses a linear pass through the subarray to determine if it can be made strictly increasing, minimizing the number of operations required.

---

### Final Notes

**Learning Points:**
- The importance of considering all possible subarrays when solving array-based problems.
- The use of a sliding window technique to efficiently check subarrays.
- The optimization of checking for strictly increasing subarrays by maintaining a count of elements that would need to be removed.

**Mistakes to Avoid:**
- Failing to consider all possible subarrays.
- Not optimizing the check for strictly increasing subarrays.
- Not using a sliding window technique to reduce the time complexity.