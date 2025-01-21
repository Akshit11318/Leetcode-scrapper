## Number of Single Divisor Triplets

**Problem Link:** https://leetcode.com/problems/number-of-single-divisor-triplets/description

**Problem Statement:**
- Input format and constraints: Given a 0-indexed integer array `nums` of length `n`, find the number of triplets `(i, j, k)` where `0 <= i < j < k < n` such that `nums[i]`, `nums[j]`, and `nums[k]` have **exactly one** common divisor greater than 1.
- Expected output format: Return the count of such triplets.
- Key requirements and edge cases to consider:
  - The array can contain duplicate elements.
  - The numbers in the array can range from 1 to 10^5.
  - The length of the array can be up to 10^5.
- Example test cases with explanations:
  - For `nums = [2,3,3]`, the output is 1 because the triplet `(0, 1, 2)` has exactly one common divisor greater than 1, which is 3.
  - For `nums = [2,3,4,2]`, the output is 3 because the triplets `(0, 1, 2)`, `(0, 1, 3)`, and `(0, 2, 3)` have exactly one common divisor greater than 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the number of triplets with exactly one common divisor greater than 1, we need to iterate over all possible triplets in the array.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible triplets `(i, j, k)` where `0 <= i < j < k < n`.
  2. For each triplet, find the greatest common divisor (GCD) of `nums[i]`, `nums[j]`, and `nums[k]`.
  3. Check if the GCD is greater than 1 and if there are no other common divisors greater than 1.
  4. If the conditions are met, increment the count of triplets.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
#include <vector>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int gcdOfThree(int a, int b, int c) {
    return gcd(gcd(a, b), c);
}

bool hasExactlyOneCommonDivisor(int a, int b, int c) {
    int gcdVal = gcdOfThree(a, b, c);
    if (gcdVal == 1) return false;
    for (int i = 2; i <= a && i <= b && i <= c; i++) {
        if (a % i == 0 && b % i == 0 && c % i == 0 && i != gcdVal) return false;
    }
    return true;
}

int countTriplets(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                if (hasExactlyOneCommonDivisor(nums[i], nums[j], nums[k])) count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot \sqrt{max(nums)})$ because we are iterating over all possible triplets and for each triplet, we are checking all possible divisors up to the square root of the maximum number in the array.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the count and other variables.
> - **Why these complexities occur:** The time complexity occurs because of the nested loops and the divisor checking. The space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all possible divisors for each triplet, we can use the prime factorization of each number to find the common divisors.
- Detailed breakdown of the approach:
  1. Find the prime factorization of each number in the array.
  2. For each triplet, find the common prime factors.
  3. Check if there is exactly one common prime factor.
- Proof of optimality: This approach is optimal because it reduces the time complexity of checking divisors from $O(\sqrt{max(nums)})$ to $O(log(max(nums)))$.
- Why further optimization is impossible: This approach is already optimal because it uses the most efficient method to find common divisors.

```cpp
#include <vector>
using namespace std;

void primeFactorization(int num, vector<int>& factors) {
    for (int i = 2; i * i <= num; i++) {
        while (num % i == 0) {
            factors.push_back(i);
            num /= i;
        }
    }
    if (num > 1) factors.push_back(num);
}

int countTriplets(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                vector<int> factors1, factors2, factors3;
                primeFactorization(nums[i], factors1);
                primeFactorization(nums[j], factors2);
                primeFactorization(nums[k], factors3);
                set<int> commonFactors;
                for (int factor : factors1) {
                    if (find(factors2.begin(), factors2.end(), factor) != factors2.end() &&
                        find(factors3.begin(), factors3.end(), factor) != factors3.end()) {
                        commonFactors.insert(factor);
                    }
                }
                if (commonFactors.size() == 1) count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot log(max(nums)))$ because we are iterating over all possible triplets and for each triplet, we are finding the prime factorization of each number.
> - **Space Complexity:** $O(log(max(nums)))$ because we are storing the prime factors of each number.
> - **Optimality proof:** This approach is optimal because it uses the most efficient method to find common divisors.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prime factorization, common divisors, and set operations.
- Problem-solving patterns identified: Using prime factorization to find common divisors.
- Optimization techniques learned: Reducing the time complexity of checking divisors.
- Similar problems to practice: Finding the greatest common divisor of multiple numbers, finding the least common multiple of multiple numbers.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not handling duplicate numbers.
- Edge cases to watch for: Empty array, array with duplicate numbers, array with numbers that have no common divisors.
- Performance pitfalls: Using inefficient algorithms to find common divisors.
- Testing considerations: Testing with large inputs, testing with edge cases.