## Prime Subtraction Operation

**Problem Link:** https://leetcode.com/problems/prime-subtraction-operation/description

**Problem Statement:**
- Input format and constraints: Given two integers, `num1` and `num2`, and an integer array `nums`, return the maximum number of operations that can be performed to make `num1` and `num2` equal by only performing prime subtractions from `num1` and `num2`, where the subtraction values are chosen from the `nums` array.
- Expected output format: The maximum number of operations.
- Key requirements and edge cases to consider: The numbers in the `nums` array are distinct, and each number can only be used once.
- Example test cases with explanations: For example, if `num1 = 6`, `num2 = 10`, and `nums = [2, 4, 6]`, we can perform the following operations: `10 - 6 = 4`, `6 - 4 = 2`, and `4 - 2 = 2`, resulting in `num1 = num2 = 2` after 3 operations.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of subtractions from `num1` and `num2` using the numbers in the `nums` array.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the `nums` array.
  2. For each permutation, try to subtract the numbers from `num1` and `num2` in the order of the permutation.
  3. Keep track of the maximum number of operations that result in `num1` and `num2` being equal.
- Why this approach comes to mind first: It is a straightforward way to explore all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

int primeSubtractionOperation(int num1, int num2, vector<int>& nums) {
    int maxOperations = 0;
    sort(nums.begin(), nums.end(), greater<int>());
    vector<int> primes;
    for (int num : nums) {
        if (isPrime(num)) primes.push_back(num);
    }
    vector<vector<int>> permutations;
    function<void(int, vector<int>, vector<int>)> generatePermutations =
        [&](int index, vector<int> current, vector<int> remaining) {
            if (index == primes.size()) {
                permutations.push_back(current);
                return;
            }
            for (int i = index; i < primes.size(); ++i) {
                swap(primes[index], primes[i]);
                current.push_back(primes[index]);
                generatePermutations(index + 1, current, remaining);
                current.pop_back();
                swap(primes[index], primes[i]);
            }
        };
    generatePermutations(0, {}, primes);
    for (auto permutation : permutations) {
        int operations = 0;
        int n1 = num1, n2 = num2;
        for (int prime : permutation) {
            if (n1 >= prime) {
                n1 -= prime;
                operations++;
            }
            if (n2 >= prime) {
                n2 -= prime;
                operations++;
            }
            if (n1 == n2) break;
        }
        maxOperations = max(maxOperations, operations);
    }
    return maxOperations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$ where $n$ is the number of prime numbers in the `nums` array, because we generate all permutations of the prime numbers.
> - **Space Complexity:** $O(n)$ for storing the permutations.
> - **Why these complexities occur:** The brute force approach explores all possible combinations of subtractions, resulting in exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to subtract the largest prime number from `num1` and `num2` in each step.
- Detailed breakdown of the approach:
  1. Sort the `nums` array in descending order.
  2. Initialize `operations` to 0.
  3. While `num1` and `num2` are not equal:
     - For each number in the sorted `nums` array:
        - If the number is prime and can be subtracted from both `num1` and `num2`, subtract it and increment `operations`.
        - If `num1` and `num2` are equal, break the loop.
- Proof of optimality: The greedy approach ensures that we subtract the largest prime number possible in each step, resulting in the maximum number of operations.
- Why further optimization is impossible: The greedy approach is optimal because it always chooses the largest prime number that can be subtracted from both `num1` and `num2`, resulting in the maximum number of operations.

```cpp
int primeSubtractionOperation(int num1, int num2, vector<int>& nums) {
    int operations = 0;
    sort(nums.begin(), nums.end(), greater<int>());
    for (int num : nums) {
        if (isPrime(num)) {
            if (num1 >= num && num2 >= num) {
                num1 -= num;
                num2 -= num;
                operations++;
            }
            if (num1 == num2) break;
        }
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \sqrt{n})$ where $n$ is the size of the `nums` array, because we sort the array and check each number for primality.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the `operations` variable.
> - **Optimality proof:** The greedy approach ensures that we subtract the largest prime number possible in each step, resulting in the maximum number of operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithms, sorting, and primality testing.
- Problem-solving patterns identified: Using a greedy approach to solve optimization problems.
- Optimization techniques learned: Sorting and primality testing can be used to optimize the solution.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for primality before subtracting a number.
- Edge cases to watch for: When `num1` and `num2` are already equal, or when the `nums` array is empty.
- Performance pitfalls: Using a brute force approach instead of a greedy approach.
- Testing considerations: Test the solution with different inputs, including edge cases.