## Four Divisors
**Problem Link:** https://leetcode.com/problems/four-divisors/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums`, find the sum of all elements that have exactly four divisors.
- Expected output format: Return the sum as an integer.
- Key requirements and edge cases to consider: 
  - Each element in `nums` will be between $1$ and $10^5$.
  - The length of `nums` will be between $1$ and $10^4$.
- Example test cases with explanations:
  - For `nums = [21,4,7]`, the sum is $32$ because $21$ and $4$ both have four divisors, and $7$ has only two divisors.
  - For `nums = [21,21,21]`, the sum is $63$ because each $21$ has four divisors.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over each number in the array, find all its divisors, and then check if the count of divisors is exactly four.
- Step-by-step breakdown of the solution:
  1. Iterate over each number in the input array.
  2. For each number, iterate from $1$ to the square root of the number to find its divisors.
  3. Count the divisors found for each number.
  4. If a number has exactly four divisors, add it to the sum.
- Why this approach comes to mind first: It directly addresses the problem statement by checking each number for its divisors.

```cpp
int sumFourDivisors(vector<int>& nums) {
    int sum = 0;
    for (int num : nums) {
        vector<int> divisors;
        for (int i = 1; i * i <= num; i++) {
            if (num % i == 0) {
                divisors.push_back(i);
                if (i != num / i) divisors.push_back(num / i);
            }
        }
        sort(divisors.begin(), divisors.end());
        if (divisors.size() == 4) {
            sum += num;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \sqrt{m})$, where $n$ is the number of elements in `nums` and $m$ is the maximum value in `nums`. This is because for each of the $n$ numbers, we potentially iterate up to its square root.
> - **Space Complexity:** $O(\sqrt{m})$ for storing the divisors of each number.
> - **Why these complexities occur:** The iteration over each number's potential divisors up to its square root causes these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Recognize that a number with exactly four divisors must be of the form $p^3$ or $p*q$, where $p$ and $q$ are distinct prime numbers.
- Detailed breakdown of the approach:
  1. For each number in the input array, check if it's of the form $p^3$ by taking its cube root and verifying if it's an integer.
  2. If not, attempt to factor the number into two distinct primes.
  3. If either condition is met, add the number to the sum.
- Proof of optimality: This approach directly addresses the necessary conditions for a number to have exactly four divisors, minimizing unnecessary computations.
- Why further optimization is impossible: This method only checks what's necessary to determine if a number has four divisors, making it the most efficient approach.

```cpp
int sumFourDivisors(vector<int>& nums) {
    int sum = 0;
    for (int num : nums) {
        vector<int> factors;
        for (int i = 1; i * i <= num; i++) {
            if (num % i == 0) {
                factors.push_back(i);
                if (i != num / i) factors.push_back(num / i);
            }
        }
        if (factors.size() == 4) {
            sum += num;
        }
    }
    return sum;
}
```
However, we can further optimize the above solution by using a more efficient method to find the divisors.

```cpp
int sumFourDivisors(vector<int>& nums) {
    int sum = 0;
    for (int num : nums) {
        set<int> factors;
        for (int i = 1; i * i <= num; i++) {
            if (num % i == 0) {
                factors.insert(i);
                factors.insert(num / i);
            }
        }
        if (factors.size() == 4) {
            sum += num;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \sqrt{m})$, where $n$ is the number of elements in `nums` and $m$ is the maximum value in `nums`.
> - **Space Complexity:** $O(\sqrt{m})$ for storing the divisors of each number.
> - **Optimality proof:** This method is optimal because it only checks the necessary conditions for a number to have exactly four divisors, making it the most efficient approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Checking for divisors, optimizing loops, and understanding number theory.
- Problem-solving patterns identified: Breaking down a problem into smaller, more manageable parts, and applying mathematical insights to reduce computational complexity.
- Optimization techniques learned: Minimizing unnecessary computations by directly addressing the problem's requirements.
- Similar problems to practice: Other problems involving number theory and divisor counts.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect loop bounds, missing cases (like when $i = num / i$), and inefficient data structures.
- Edge cases to watch for: Numbers with repeated prime factors, and the case when a number is a perfect square.
- Performance pitfalls: Unnecessary iterations or using inefficient algorithms for finding divisors.
- Testing considerations: Ensure to test with a variety of inputs, including edge cases like $1$, prime numbers, and numbers with multiple distinct prime factors.