## Split the Array to Make Coprime Products

**Problem Link:** https://leetcode.com/problems/split-the-array-to-make-coprime-products/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`.
- Expected Output: The minimum number of subarrays to split `nums` into such that the product of elements in each subarray is coprime.
- Key Requirements: Two numbers are coprime if their greatest common divisor (GCD) is 1.
- Edge Cases: The product of all elements in `nums` could be very large, requiring careful handling of integer overflow.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible split of the array and calculating the product of each subarray.
- For each subarray, check if the product is coprime by verifying if the GCD of the product and any other number in the subarray is 1.
- This approach is straightforward but inefficient due to its exponential time complexity.

```cpp
#include <vector>
#include <numeric>

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int splitArray(vector<int>& nums) {
    int n = nums.size();
    int minSubarrays = n; // Initialize with the maximum possible subarrays
    
    for (int mask = 1; mask < (1 << n); ++mask) {
        vector<int> subarrayProducts;
        int currProduct = 1;
        
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                currProduct *= nums[i];
            } else {
                subarrayProducts.push_back(currProduct);
                currProduct = 1;
            }
        }
        subarrayProducts.push_back(currProduct);
        
        bool allCoprime = true;
        for (int product : subarrayProducts) {
            for (int num : nums) {
                if (gcd(product, num) != 1) {
                    allCoprime = false;
                    break;
                }
            }
            if (!allCoprime) break;
        }
        
        if (allCoprime) {
            minSubarrays = min(minSubarrays, (int)subarrayProducts.size());
        }
    }
    
    return minSubarrays;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the size of `nums` and $m$ is the maximum value in `nums`. This is because we generate all possible subsets of `nums` and for each subset, we calculate the product and check for coprime.
> - **Space Complexity:** $O(n)$, for storing the current subarray products.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsets of the input array, and the linear space complexity is due to storing the subarray products.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using the concept of coprime numbers and the properties of GCD to minimize the number of subarrays.
- We can observe that if two numbers are coprime, their GCD is 1, meaning they have no common prime factors.
- To minimize the number of subarrays, we should group numbers that are coprime together.
- We can use a greedy approach, always trying to add the next number to the current subarray if it's coprime with the product of the current subarray.

```cpp
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int splitArray(vector<int>& nums) {
    int n = nums.size();
    int subarrays = 1;
    long long currProduct = nums[0];
    
    for (int i = 1; i < n; ++i) {
        if (gcd(currProduct, nums[i]) != 1) {
            subarrays++;
            currProduct = nums[i];
        } else {
            currProduct *= nums[i];
        }
    }
    
    return subarrays;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of `nums` and $m$ is the maximum value in `nums`. This is because we iterate through `nums` once and for each number, we calculate the GCD with the current product.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it minimizes the number of subarrays by always trying to add the next number to the current subarray if it's coprime, thus ensuring that the product of each subarray is coprime.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: GCD, coprime numbers, greedy approach.
- Problem-solving patterns identified: minimizing the number of subarrays by grouping coprime numbers together.
- Optimization techniques learned: using GCD to check for coprime numbers, greedy approach to minimize subarrays.
- Similar problems to practice: problems involving GCD, coprime numbers, and greedy approaches.

**Mistakes to Avoid:**
- Common implementation errors: not handling integer overflow, not checking for coprime correctly.
- Edge cases to watch for: large input arrays, large numbers in the array.
- Performance pitfalls: using an inefficient algorithm with high time complexity.
- Testing considerations: testing with different input sizes, testing with edge cases.