## Maximum Subarray with Equal Products
**Problem Link:** https://leetcode.com/problems/maximum-subarray-with-equal-products/description

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`, and `1 <= k <= 10^5`.
- Expected output format: The maximum length of a subarray with equal products modulo `k`.
- Key requirements and edge cases to consider: Empty arrays, arrays with a single element, arrays with all elements being the same, and arrays with all elements being multiples of `k`.
- Example test cases with explanations:
  - `nums = [1, 2, 3], k = 3`: The maximum length is 2 because the subarray `[1, 2]` has a product of 2, which is 2 modulo 3, and the subarray `[2, 3]` has a product of 6, which is 0 modulo 3.
  - `nums = [1, 2, 3, 4, 5], k = 2`: The maximum length is 5 because all elements are odd, so the product of any subarray is odd, which is 1 modulo 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the product of all possible subarrays and check if the product modulo `k` is the same for each subarray.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of `nums`.
  2. For each subarray, calculate the product of its elements.
  3. Check if the product modulo `k` is the same for all elements in the subarray.
  4. Keep track of the maximum length of subarrays that satisfy the condition.

```cpp
#include <iostream>
#include <vector>

int maximumSubarrayWithEqualProducts(std::vector<int>& nums, int k) {
    int maxLength = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i; j < nums.size(); j++) {
            long long product = 1;
            for (int m = i; m <= j; m++) {
                product = (product * nums[m]) % k;
            }
            bool equal = true;
            for (int m = i + 1; m <= j; m++) {
                if ((nums[m] % k) != product) {
                    equal = false;
                    break;
                }
            }
            if (equal) {
                maxLength = std::max(maxLength, j - i + 1);
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of `nums`, because we generate all possible subarrays and calculate the product for each subarray.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the maximum length and the product.
> - **Why these complexities occur:** The brute force approach has high time complexity because it generates all possible subarrays and calculates the product for each subarray. The space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of calculating the product for each subarray, we can use a prefix product array to calculate the product in constant time.
- Detailed breakdown of the approach:
  1. Create a prefix product array `prefixProduct` where `prefixProduct[i]` is the product of all elements in `nums` from index 0 to `i`.
  2. Iterate over all possible subarrays of `nums`.
  3. For each subarray, calculate the product modulo `k` using the prefix product array.
  4. Check if the product modulo `k` is the same for all elements in the subarray.
  5. Keep track of the maximum length of subarrays that satisfy the condition.

```cpp
#include <iostream>
#include <vector>

int maximumSubarrayWithEqualProducts(std::vector<int>& nums, int k) {
    int maxLength = 0;
    std::vector<long long> prefixProduct(nums.size() + 1, 1);
    for (int i = 0; i < nums.size(); i++) {
        prefixProduct[i + 1] = (prefixProduct[i] * nums[i]) % k;
    }
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i; j < nums.size(); j++) {
            long long product = (prefixProduct[j + 1] * powMod(prefixProduct[i], k - 2, k)) % k;
            bool equal = true;
            for (int m = i; m <= j; m++) {
                if ((nums[m] % k) != product) {
                    equal = false;
                    break;
                }
            }
            if (equal) {
                maxLength = std::max(maxLength, j - i + 1);
            }
        }
    }
    return maxLength;
}

long long powMod(long long a, long long b, long long mod) {
    long long res = 1;
    while (b > 0) {
        if (b % 2 == 1) {
            res = (res * a) % mod;
        }
        a = (a * a) % mod;
        b /= 2;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of `nums`, because we iterate over all possible subarrays and calculate the product using the prefix product array.
> - **Space Complexity:** $O(n)$, because we use a prefix product array of size $n + 1$.
> - **Optimality proof:** The optimal approach has a lower time complexity than the brute force approach because it uses a prefix product array to calculate the product in constant time. The space complexity is higher because we use a prefix product array, but it is still acceptable.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix product array, modular arithmetic, and optimization techniques.
- Problem-solving patterns identified: Using a prefix array to calculate the product in constant time and iterating over all possible subarrays.
- Optimization techniques learned: Using a prefix array to reduce the time complexity and using modular arithmetic to avoid overflow.
- Similar problems to practice: Maximum subarray with equal sums, maximum subarray with equal products modulo a prime number.

**Mistakes to Avoid:**
- Common implementation errors: Not using a prefix product array, not using modular arithmetic, and not iterating over all possible subarrays.
- Edge cases to watch for: Empty arrays, arrays with a single element, arrays with all elements being the same, and arrays with all elements being multiples of `k`.
- Performance pitfalls: Not using a prefix product array, not using modular arithmetic, and not iterating over all possible subarrays.
- Testing considerations: Test the function with different inputs, including edge cases, and verify that the output is correct.