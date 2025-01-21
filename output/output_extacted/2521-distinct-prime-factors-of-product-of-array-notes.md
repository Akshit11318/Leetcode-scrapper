## Distinct Prime Factors of Product of Array

**Problem Link:** https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^4`, `1 <= nums[i] <= 10^6`.
- Expected Output: The number of distinct prime factors of the product of all numbers in the array.
- Key Requirements: Identify all prime factors of the product of the array elements and count the distinct ones.
- Edge Cases: Empty array, array with a single element, array with all elements being the same.

Example Test Cases:
- Input: `nums = [2, 4, 3, 9]`
  - Output: `4` (Distinct prime factors: 2, 3)
- Input: `nums = [2, 2, 2]`
  - Output: `1` (Distinct prime factor: 2)

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating the product of all numbers in the array and then finding all prime factors of this product.
- Step-by-step breakdown:
  1. Calculate the product of all numbers in the array.
  2. Find all prime factors of the product.
  3. Count the distinct prime factors.
- Why this approach comes to mind first: It directly addresses the problem statement by first calculating the product and then finding its prime factors.

```cpp
#include <iostream>
#include <set>
#include <vector>

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

std::set<int> primeFactors(int n) {
    std::set<int> factors;
    for (int i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            factors.insert(i);
            n /= i;
        }
    }
    if (n > 1) factors.insert(n);
    return factors;
}

int distinctPrimeFactors(std::vector<int>& nums) {
    long long product = 1;
    for (int num : nums) {
        product *= num;
    }
    std::set<int> factors = primeFactors(product);
    return factors.size();
}

int main() {
    std::vector<int> nums = {2, 4, 3, 9};
    std::cout << distinctPrimeFactors(nums) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \sqrt{max(nums)} + \sqrt{product})$, where $n$ is the number of elements in the array, $max(nums)$ is the maximum number in the array, and $product$ is the product of all numbers in the array. This is because we iterate through each number to calculate the product and then find its prime factors.
> - **Space Complexity:** $O(n + \sqrt{product})$, for storing the product and its prime factors.
> - **Why these complexities occur:** The calculation of the product and finding its prime factors are the main contributors to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of calculating the product of all numbers and then finding its prime factors, we can find the prime factors of each number in the array and then count the distinct ones across all numbers.
- Detailed breakdown:
  1. Iterate through each number in the array.
  2. For each number, find its prime factors.
  3. Store the distinct prime factors in a set.
  4. Return the size of the set as the number of distinct prime factors.
- Proof of optimality: This approach avoids calculating the large product and directly finds the prime factors of each number, reducing the time and space complexity.

```cpp
#include <iostream>
#include <set>
#include <vector>

std::set<int> primeFactors(int n) {
    std::set<int> factors;
    for (int i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            factors.insert(i);
            n /= i;
        }
    }
    if (n > 1) factors.insert(n);
    return factors;
}

int distinctPrimeFactors(std::vector<int>& nums) {
    std::set<int> distinctFactors;
    for (int num : nums) {
        std::set<int> factors = primeFactors(num);
        distinctFactors.insert(factors.begin(), factors.end());
    }
    return distinctFactors.size();
}

int main() {
    std::vector<int> nums = {2, 4, 3, 9};
    std::cout << distinctPrimeFactors(nums) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \sqrt{max(nums)})$, where $n$ is the number of elements in the array and $max(nums)$ is the maximum number in the array. This is because we find the prime factors of each number individually.
> - **Space Complexity:** $O(n + \sqrt{max(nums)})$, for storing the distinct prime factors.
> - **Optimality proof:** This approach is optimal because it minimizes the operations required to find the distinct prime factors by processing each number individually and using a set to automatically eliminate duplicates.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prime factorization, use of sets for storing distinct elements.
- Problem-solving patterns identified: Breaking down a problem into smaller, more manageable parts (finding prime factors of each number instead of the product).
- Optimization techniques learned: Avoiding unnecessary calculations (calculating the product of all numbers), using data structures efficiently (sets for distinct elements).
- Similar problems to practice: Finding prime factors of a number, counting distinct elements in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for division by zero, not handling edge cases (empty array, array with a single element).
- Edge cases to watch for: Empty array, array with all elements being the same.
- Performance pitfalls: Calculating the product of all numbers, which can lead to large intermediate results and increased time complexity.
- Testing considerations: Test with arrays of varying sizes, with different types of numbers (primes, composites), and edge cases.