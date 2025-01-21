## Closest Divisors
**Problem Link:** [https://leetcode.com/problems/closest-divisors/description](https://leetcode.com/problems/closest-divisors/description)

**Problem Statement:**
- Input format: Two integers `num`
- Constraints: $1 \leq num \leq 10^6$
- Expected output format: An array of two integers, representing the closest divisors of `num + k` and `num + k + 1`, where `k` is the smallest non-negative integer such that both `num + k` and `num + k + 1` are not prime.
- Key requirements and edge cases to consider: 
  - Find the smallest `k` such that both `num + k` and `num + k + 1` are not prime.
  - Handle cases where `num` is close to a large prime number.
- Example test cases with explanations: 
  - For `num = 8`, the closest divisors are `[9, 10]` because `8 + 1 = 9` and `8 + 2 = 10` are the smallest non-prime numbers greater than `8`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each number greater than `num` to see if it is prime or not. If a number is not prime, find its closest divisor.
- Step-by-step breakdown of the solution:
  1. Start from `num` and check each number to see if it is prime.
  2. For each number, check if it is prime by testing divisibility up to its square root.
  3. If a number is not prime, find its closest divisor by checking all numbers up to its square root.
- Why this approach comes to mind first: It is a straightforward approach that checks each number individually.

```cpp
#include <vector>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

vector<int> closestDivisors(int num) {
    int k = 0;
    while (true) {
        if (!isPrime(num + k) && !isPrime(num + k + 1)) break;
        k++;
    }
    int n1 = num + k, n2 = num + k + 1;
    int d1 = n1, d2 = n2;
    for (int i = 1; i * i <= n1; i++) {
        if (n1 % i == 0) {
            d1 = i;
            break;
        }
    }
    for (int i = 1; i * i <= n2; i++) {
        if (n2 % i == 0) {
            d2 = i;
            break;
        }
    }
    return {d1, d2};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot \sqrt{num + k})$, where $k$ is the smallest non-negative integer such that both `num + k` and `num + k + 1` are not prime.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is high because we are checking each number individually and testing divisibility up to its square root.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a prime-checking function to find the smallest `k` such that both `num + k` and `num + k + 1` are not prime. We can also use a divisor-finding function to find the closest divisors of `num + k` and `num + k + 1`.
- Detailed breakdown of the approach:
  1. Create a boolean array `isPrime` of size `num + 100000` to store whether each number is prime or not.
  2. Use the Sieve of Eratosthenes algorithm to mark all prime numbers in the `isPrime` array.
  3. Start from `num` and check each number to see if it is prime. If a number is not prime, find its closest divisor.
- Proof of optimality: This approach is optimal because we are using a sieve to mark all prime numbers, which has a time complexity of $O(n \log \log n)$. We are also using a divisor-finding function to find the closest divisors, which has a time complexity of $O(\sqrt{n})$.

```cpp
#include <vector>
using namespace std;

vector<int> closestDivisors(int num) {
    const int MAXN = num + 100000;
    vector<bool> isPrime(MAXN, true);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i * i < MAXN; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j < MAXN; j += i) {
                isPrime[j] = false;
            }
        }
    }
    int k = 0;
    while (true) {
        if (!isPrime[num + k] && !isPrime[num + k + 1]) break;
        k++;
    }
    int n1 = num + k, n2 = num + k + 1;
    int d1 = n1, d2 = n2;
    for (int i = 1; i * i <= n1; i++) {
        if (n1 % i == 0) {
            d1 = i;
            break;
        }
    }
    for (int i = 1; i * i <= n2; i++) {
        if (n2 % i == 0) {
            d2 = i;
            break;
        }
    }
    return {d1, d2};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log \log n + \sqrt{n})$, where $n$ is the input number.
> - **Space Complexity:** $O(n)$, as we are using a boolean array of size $n$.
> - **Optimality proof:** This approach is optimal because we are using a sieve to mark all prime numbers, which has a time complexity of $O(n \log \log n)$. We are also using a divisor-finding function to find the closest divisors, which has a time complexity of $O(\sqrt{n})$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sieve of Eratosthenes, prime-checking, divisor-finding.
- Problem-solving patterns identified: Using a sieve to mark all prime numbers, using a divisor-finding function to find the closest divisors.
- Optimization techniques learned: Using a sieve to reduce the time complexity of prime-checking, using a divisor-finding function to reduce the time complexity of finding the closest divisors.
- Similar problems to practice: Prime-checking, divisor-finding, sieve algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `isPrime` array correctly, not marking all prime numbers in the `isPrime` array.
- Edge cases to watch for: Handling cases where `num` is close to a large prime number.
- Performance pitfalls: Not using a sieve to mark all prime numbers, not using a divisor-finding function to find the closest divisors.
- Testing considerations: Testing the code with large input numbers, testing the code with edge cases.