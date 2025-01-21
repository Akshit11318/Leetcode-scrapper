## Prime Pairs With Target Sum

**Problem Link:** https://leetcode.com/problems/prime-pairs-with-target-sum/description

**Problem Statement:**
- Given a list of `n` integers and a target sum `target`, find all pairs of prime numbers in the list that add up to `target`.
- Input format: `n` integers and a target sum `target`.
- Expected output format: List of pairs of prime numbers that sum up to `target`.
- Key requirements and edge cases to consider:
  - A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
  - Each input integer is within the range of 1 to 1000.
  - The target sum `target` is within the range of 2 to 2000.
- Example test cases with explanations:
  - For the input `[1, 2, 3, 4, 5]` and `target = 8`, the output should be `[[3, 5]]` because 3 and 5 are the only pair of prime numbers that add up to 8.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find all pairs of prime numbers that sum up to the target, we need to first identify all prime numbers in the list, and then check every possible pair to see if their sum equals the target.
- Step-by-step breakdown of the solution:
  1. Create a function to check if a number is prime.
  2. Iterate through the list to find all prime numbers.
  3. For each prime number, iterate through the rest of the list to find another prime number such that their sum equals the target.
  4. If such a pair is found, add it to the result list.
- Why this approach comes to mind first: It is the most straightforward approach, directly addressing the problem statement without considering optimizations.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> primePairs(vector<int>& nums, int target) {
        vector<vector<int>> result;
        for (int i = 0; i < nums.size(); ++i) {
            if (isPrime(nums[i])) {
                for (int j = i + 1; j < nums.size(); ++j) {
                    if (isPrime(nums[j]) && nums[i] + nums[j] == target) {
                        result.push_back({nums[i], nums[j]});
                    }
                }
            }
        }
        return result;
    }

    bool isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i * i <= num; ++i) {
            if (num % i == 0) return false;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot \sqrt{max(nums)})$ where $n$ is the number of elements in the input list and $max(nums)$ is the maximum number in the list. This is because for each element, we potentially check every other element and for each check, we verify if a number is prime which takes up to $\sqrt{max(nums)}$ time.
> - **Space Complexity:** $O(n)$ for storing the result.
> - **Why these complexities occur:** The nested loops for checking pairs and the prime check function contribute to the time complexity. The space complexity is due to storing the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every pair and verifying if both numbers are prime, we can first generate all prime numbers up to the maximum possible value in the input list, and then use a hash set to store these primes for efficient lookup.
- Detailed breakdown of the approach:
  1. Generate all prime numbers up to the maximum possible value (1000 in this case) using the Sieve of Eratosthenes algorithm.
  2. Store these prime numbers in a hash set for $O(1)$ lookup time.
  3. Iterate through the input list, and for each number, check if it and the difference between the target and the current number are both in the hash set of primes.
  4. If they are, add the pair to the result list.
- Proof of optimality: This approach minimizes the time complexity by avoiding redundant prime checks and using a hash set for fast lookup.

```cpp
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<vector<int>> primePairs(vector<int>& nums, int target) {
        vector<vector<int>> result;
        unordered_set<int> primes = generatePrimes(1000);
        
        for (int num : nums) {
            if (primes.count(num) && primes.count(target - num) && num <= target - num) {
                result.push_back({num, target - num});
            }
        }
        return result;
    }

    unordered_set<int> generatePrimes(int maxNum) {
        vector<bool> isPrime(maxNum + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= maxNum; ++i) {
            if (isPrime[i]) {
                for (int j = i * i; j <= maxNum; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        unordered_set<int> primes;
        for (int i = 2; i <= maxNum; ++i) {
            if (isPrime[i]) {
                primes.insert(i);
            }
        }
        return primes;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + max(nums) \cdot log(log(max(nums))))$ where $n$ is the number of elements in the input list and $max(nums)$ is the maximum number in the list. The Sieve of Eratosthenes algorithm takes $O(max(nums) \cdot log(log(max(nums))))$ time, and then we iterate through the list which takes $O(n)$ time.
> - **Space Complexity:** $O(max(nums))$ for storing the prime numbers.
> - **Optimality proof:** This approach is optimal because it minimizes the time complexity by using the Sieve of Eratosthenes to generate primes and a hash set for fast lookup, avoiding redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sieve of Eratosthenes for generating prime numbers, hash sets for efficient lookup.
- Problem-solving patterns identified: Preprocessing data (generating primes) to speed up subsequent operations.
- Optimization techniques learned: Using hash sets for $O(1)$ lookup, minimizing redundant calculations.
- Similar problems to practice: Other problems involving prime numbers, such as finding the nth prime number or checking if a number is prime.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the Sieve of Eratosthenes or hash set operations.
- Edge cases to watch for: Handling the case where the input list is empty or contains no prime numbers.
- Performance pitfalls: Using inefficient algorithms for generating primes or checking pairs.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases.