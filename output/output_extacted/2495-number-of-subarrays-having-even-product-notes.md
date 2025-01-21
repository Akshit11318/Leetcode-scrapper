## Number of Subarrays Having Even Product
**Problem Link:** https://leetcode.com/problems/number-of-subarrays-having-even-product/description

**Problem Statement:**
- Given an array `nums` of integers, return the number of subarrays with an even product.
- Input format: `nums` array of integers.
- Constraints: `1 <= nums.length <= 10^5` and `1 <= nums[i] <= 10^5`.
- Expected output format: The number of subarrays with an even product.
- Key requirements: Identify subarrays where the product of elements is even.
- Edge cases: Handle arrays with odd and even numbers, and arrays with zeros.

### Brute Force Approach
**Explanation:**
- The initial thought process is to calculate the product of all possible subarrays and check if the product is even.
- Step-by-step breakdown:
  1. Generate all possible subarrays.
  2. Calculate the product of each subarray.
  3. Check if the product is even by using the modulo operator (`%`).
  4. Count the number of subarrays with an even product.

```cpp
int numSubarraysWithEvenProduct(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        long long product = 1;
        for (int j = i; j < nums.size(); j++) {
            product *= nums[j];
            if (product % 2 == 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of elements in the array and $m$ is the maximum number of digits in the product. This is because we are generating all possible subarrays and calculating the product for each subarray.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the count and product variables.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops and product calculation, making it inefficient for large inputs.

### Optimal Approach (Required)
**Explanation:**
- The key insight is that a product is even if at least one of the factors is even.
- We can use a prefix sum-like approach to keep track of the number of even and odd numbers encountered so far.
- If the current number is even, we increment the count of subarrays with an even product by the total number of subarrays ending at the previous even number.
- If the current number is odd, we only consider the subarrays starting from the previous odd number.

```cpp
int numSubarraysWithEvenProduct(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        int evenCount = 0;
        for (int j = i; j < nums.size(); j++) {
            if (nums[j] % 2 == 0) {
                evenCount++;
            }
            if (evenCount > 0) {
                count++;
            }
        }
    }
    return count;
}
```

However, the above solution still has a time complexity of $O(n^2)$. We can further optimize it by observing that the presence of a single even number in a subarray makes the entire product even.

```cpp
int numSubarraysWithEvenProduct(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        bool hasEven = false;
        for (int j = i; j < nums.size(); j++) {
            if (nums[j] % 2 == 0) {
                hasEven = true;
            }
            if (hasEven) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the count and hasEven variables.
> - **Optimality proof:** This is the best possible time complexity for this problem, as we need to consider all possible subarrays to count the number of subarrays with an even product.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: prefix sum-like approach, counting subarrays with even product.
- Problem-solving patterns identified: using a flag to track the presence of an even number in a subarray.
- Optimization techniques learned: reducing the number of operations by using a flag instead of calculating the product.
- Similar problems to practice: counting subarrays with other properties (e.g., sum, maximum, minimum).

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases (e.g., arrays with only odd numbers).
- Edge cases to watch for: arrays with zeros, arrays with only even numbers.
- Performance pitfalls: using unnecessary calculations (e.g., calculating the product for each subarray).
- Testing considerations: testing with different input sizes, testing with different types of input (e.g., arrays with only odd numbers, arrays with only even numbers).