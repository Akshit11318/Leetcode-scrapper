## K-Divisible Elements Subarrays

**Problem Link:** https://leetcode.com/problems/k-divisible-elements-subarrays/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`, and `1 <= k <= 10^5`.
- Expected Output: The number of subarrays in `nums` where all elements are divisible by `k`.
- Key Requirements: 
  - Identify all possible subarrays within the given array `nums`.
  - Determine which of these subarrays contain only elements that are divisible by `k`.
- Edge Cases: 
  - An empty array.
  - An array with a single element.
  - An array with no elements divisible by `k`.
- Example Test Cases:
  - `nums = [4, 5, 9, 7, 2, 10], k = 3`. Expected output: `3` because the subarrays `[9], [9, 7, 2], [9, 7, 2, 10]` have all elements divisible by `3`.
  - `nums = [1, 2, 3], k = 4`. Expected output: `0` because no subarray has all elements divisible by `4`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subarray within the given array `nums`.
- For each subarray, we verify if all its elements are divisible by `k`.
- This approach is straightforward but inefficient for large arrays due to its exhaustive nature.

```cpp
int countSubarrays(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); ++i) {
        for (int j = i; j < nums.size(); ++j) {
            bool allDivisible = true;
            for (int index = i; index <= j; ++index) {
                if (nums[index] % k != 0) {
                    allDivisible = false;
                    break;
                }
            }
            if (allDivisible) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the size of the `nums` array, because for each of the $n$ elements, we potentially iterate over the rest of the array, and for each subarray, we check divisibility.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our variables, regardless of the input size.
> - **Why these complexities occur:** The cubic time complexity arises from the nested loops that generate all possible subarrays and then check each element within these subarrays for divisibility by `k`.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to recognize that checking every subarray is unnecessary. Instead, we can use a sliding window approach to efficiently scan the array and identify subarrays where all elements are divisible by `k`.
- We maintain a window `[left, right]` and expand it to the right as long as all elements within the window are divisible by `k`. When we encounter an element not divisible by `k`, we slide the window to the right, starting from the next element.
- This approach significantly reduces the number of subarrays we need to check.

```cpp
int countSubarrays(vector<int>& nums, int k) {
    int count = 0;
    for (int left = 0; left < nums.size(); ++left) {
        for (int right = left; right < nums.size(); ++right) {
            bool allDivisible = true;
            for (int index = left; index <= right; ++index) {
                if (nums[index] % k != 0) {
                    allDivisible = false;
                    break;
                }
            }
            if (allDivisible) {
                count++;
            }
        }
    }
    return count;
}
```
However the previous code still has a time complexity of $O(n^3)$. We can use a prefix sum array to calculate the number of subarrays in $O(n^2)$ time complexity.

```cpp
int countSubarrays(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); ++i) {
        bool allDivisible = true;
        for (int j = i; j < nums.size(); ++j) {
            if (nums[j] % k != 0) {
                allDivisible = false;
                break;
            }
            if (allDivisible) {
                count++;
            }
        }
    }
    return count;
}
```
However the previous code still has a time complexity of $O(n^2)$ and it's possible to do better than that by using a mathematical formula to calculate the total number of subarrays.

Let's calculate the total number of subarrays first.
The total number of subarrays is given by the formula $\frac{n(n+1)}{2}$ where $n$ is the number of elements in the array.

```cpp
int countSubarrays(vector<int>& nums, int k) {
    int n = nums.size();
    int totalSubarrays = n * (n + 1) / 2;
    int count = 0;
    for (int i = 0; i < n; ++i) {
        if (nums[i] % k == 0) {
            count++;
        }
    }
    // calculate the number of subarrays where all elements are divisible by k
    // this can be done by using a sliding window approach
    int windowStart = 0;
    int divisibleCount = 0;
    for (int windowEnd = 0; windowEnd < n; windowEnd++) {
        if (nums[windowEnd] % k == 0) {
            divisibleCount++;
        }
        while (divisibleCount == windowEnd - windowStart + 1) {
            count++;
            if (nums[windowStart] % k == 0) {
                divisibleCount--;
            }
            windowStart++;
        }
    }
    return count;
}
```
However this code still has a time complexity of $O(n^2)$.

To achieve a time complexity of $O(n)$ we need to use a different approach.

We can use a hash map to store the cumulative sum of the array elements modulo `k`. The cumulative sum at each index `i` is the sum of all elements from index `0` to `i` modulo `k`. We then use this cumulative sum to calculate the number of subarrays where all elements are divisible by `k`.

```cpp
int countSubarrays(vector<int>& nums, int k) {
    int count = 0;
    unordered_map<int, int> prefixSumCount;
    prefixSumCount[0] = 1; // base case
    int cumulativeSum = 0;
    for (int num : nums) {
        cumulativeSum = (cumulativeSum + num % k) % k;
        if (prefixSumCount.find(cumulativeSum) != prefixSumCount.end()) {
            count += prefixSumCount[cumulativeSum];
        }
        prefixSumCount[cumulativeSum]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the `nums` array, because we make a single pass through the array.
> - **Space Complexity:** $O(k)$, as in the worst case, we might store every possible remainder modulo `k` in our hash map.
> - **Optimality proof:** This solution is optimal because it only requires a single pass through the input array, and it uses a hash map to efficiently keep track of the cumulative sums modulo `k`, allowing it to count the subarrays in linear time.

---

### Final Notes

**Learning Points:**
- The importance of recognizing the need for an efficient algorithm when dealing with large inputs.
- The use of a hash map to store cumulative sums modulo `k` for efficient subarray counting.
- The concept of a sliding window approach and how it can be adapted for different problems.

**Mistakes to Avoid:**
- Assuming that brute force is the only approach, especially for large inputs.
- Not considering the use of data structures like hash maps for efficient counting and tracking.
- Failing to recognize the pattern or property that allows for an optimal solution, such as the cumulative sum modulo `k` in this case.