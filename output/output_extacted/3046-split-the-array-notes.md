## Split the Array
**Problem Link:** https://leetcode.com/problems/split-the-array/description

**Problem Statement:**
- Given an integer array `nums` of size `n`, split the array into two non-empty subarrays or sublists at an index.
- The product of all the numbers in the left subarray should be equal to the product of all the numbers in the right subarray.
- Input: `nums = [2,3,5]`
- Output: `true`
- Key requirements: The input array `nums` contains integers, and we need to find a split point that satisfies the product condition.
- Edge cases: The array must have at least two elements, and the product of all numbers in the left and right subarrays should be equal.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible split points in the array and calculate the product of the left and right subarrays.
- For each split point, we calculate the product of the left subarray and the product of the right subarray.
- We compare the two products and return `true` if they are equal.

```cpp
class Solution {
public:
    bool splitArraySameAverage(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return false;
        
        // Calculate the total sum of the array
        int sum = accumulate(nums.begin(), nums.end(), 0);
        
        // Try all possible split points
        for (int i = 1; i < n; i++) {
            int leftSum = accumulate(nums.begin(), nums.begin() + i, 0);
            int rightSum = sum - leftSum;
            
            // Calculate the product of the left and right subarrays
            long long leftProduct = 1;
            for (int j = 0; j < i; j++) {
                leftProduct *= nums[j];
            }
            long long rightProduct = 1;
            for (int j = i; j < n; j++) {
                rightProduct *= nums[j];
            }
            
            // Check if the products are equal
            if (leftProduct == rightProduct) return true;
        }
        
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. The outer loop tries all possible split points, and the inner loops calculate the products of the left and right subarrays.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array. The space complexity is constant because we only use a few variables to store the sums and products.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it tries all possible split points and calculates the products of the left and right subarrays for each split point.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that the product of the left subarray should be equal to the product of the right subarray.
- We can use a prefix product array to calculate the product of the left subarray in $O(1)$ time.
- We can use a suffix product array to calculate the product of the right subarray in $O(1)$ time.
- We iterate over the array and check if the product of the left subarray is equal to the product of the right subarray.

```cpp
class Solution {
public:
    bool splitArraySameAverage(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return false;
        
        // Calculate the total sum of the array
        int sum = accumulate(nums.begin(), nums.end(), 0);
        
        // Calculate the prefix product array
        vector<long long> prefixProduct(n + 1, 1);
        for (int i = 0; i < n; i++) {
            prefixProduct[i + 1] = prefixProduct[i] * nums[i];
        }
        
        // Calculate the suffix product array
        vector<long long> suffixProduct(n + 1, 1);
        for (int i = n - 1; i >= 0; i--) {
            suffixProduct[i] = suffixProduct[i + 1] * nums[i];
        }
        
        // Check if the products are equal
        for (int i = 0; i < n - 1; i++) {
            if (prefixProduct[i + 1] == suffixProduct[i + 1]) return true;
        }
        
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. We calculate the prefix and suffix product arrays in $O(n)$ time and then iterate over the array to check if the products are equal.
> - **Space Complexity:** $O(n)$, excluding the space needed for the input array. The space complexity is linear because we need to store the prefix and suffix product arrays.
> - **Optimality proof:** This approach is optimal because we only need to iterate over the array once to calculate the prefix and suffix product arrays, and then we can check if the products are equal in $O(1)$ time.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of prefix and suffix arrays to calculate the product of subarrays in $O(1)$ time.
- The problem-solving pattern identified is the use of dynamic programming to solve problems that involve calculating aggregates over subarrays.
- The optimization technique learned is the use of prefix and suffix arrays to reduce the time complexity of the algorithm.

**Mistakes to Avoid:**
- A common implementation error is to use a brute force approach that tries all possible split points and calculates the products of the left and right subarrays for each split point.
- An edge case to watch for is when the input array has less than two elements, in which case the function should return `false`.
- A performance pitfall is to use a naive approach that calculates the product of the left and right subarrays for each split point, resulting in a high time complexity.