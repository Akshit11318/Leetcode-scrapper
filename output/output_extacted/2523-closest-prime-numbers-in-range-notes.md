## Closest Prime Numbers in Range
**Problem Link:** https://leetcode.com/problems/closest-prime-numbers-in-range/description

**Problem Statement:**
- Given an integer `left` and an integer `right`, return the `closest` prime number to `left` in the range `[left, right]`. If there are multiple closest prime numbers, return the smallest one.
- Input format and constraints: `1 <= left <= right <= 10^6`
- Expected output format: The closest prime number to `left` in the range `[left, right]`.
- Key requirements and edge cases to consider: If `left` is a prime number, return `left`. If there are no prime numbers in the range, return `-1`.
- Example test cases with explanations:
  - `left = 1, right = 10`: The closest prime number to `1` is `2`, which is in the range `[1, 10]`.
  - `left = 10, right = 20`: The closest prime number to `10` is `11`, which is in the range `[10, 20]`.

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each number in the range `[left, right]` to see if it's a prime number.
- Step-by-step breakdown of the solution:
  1. Create a helper function `isPrime(n)` to check if a number `n` is prime.
  2. Iterate over the range `[left, right]` and check each number using the `isPrime(n)` function.
  3. Keep track of the closest prime number to `left` and its distance from `left`.
- Why this approach comes to mind first: It's a straightforward approach that checks each number in the range to see if it's prime.

```cpp
class Solution {
public:
    int closestPrime(int left, int right) {
        // Helper function to check if a number is prime
        auto isPrime = [](int n) {
            if (n <= 1) return false;
            for (int i = 2; i * i <= n; i++) {
                if (n % i == 0) return false;
            }
            return true;
        };

        int closest = -1;
        int minDiff = INT_MAX;
        for (int i = left; i <= right; i++) {
            if (isPrime(i)) {
                int diff = abs(i - left);
                if (diff < minDiff) {
                    minDiff = diff;
                    closest = i;
                }
            }
        }
        return closest;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \sqrt{n})$ where $n$ is the range `[right - left + 1]`. The reason is that for each number in the range, we're checking if it's prime using a loop that runs up to $\sqrt{n}$.
> - **Space Complexity:** $O(1)$ since we're only using a constant amount of space to store the closest prime number and its distance from `left`.
> - **Why these complexities occur:** The time complexity is high because we're checking each number in the range to see if it's prime, and the prime check itself takes $O(\sqrt{n})$ time.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each number in the range to see if it's prime, we can use a sieve to generate all prime numbers up to `right` and then find the closest one to `left`.
- Detailed breakdown of the approach:
  1. Create a boolean array `isPrime` of size `right + 1` and initialize all values to `true`.
  2. Iterate over the array and mark the multiples of each prime number as `false`.
  3. Find the closest prime number to `left` by iterating over the `isPrime` array.
- Proof of optimality: This approach has a time complexity of $O(n \log \log n)$, which is much faster than the brute force approach.

```cpp
class Solution {
public:
    int closestPrime(int left, int right) {
        vector<bool> isPrime(right + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= right; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= right; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        int closest = -1;
        int minDiff = INT_MAX;
        for (int i = left; i <= right; i++) {
            if (isPrime[i]) {
                int diff = abs(i - left);
                if (diff < minDiff) {
                    minDiff = diff;
                    closest = i;
                }
            }
        }
        return closest;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log \log n)$ where $n$ is the range `[right]`. The reason is that we're using a sieve to generate all prime numbers up to `right`, and the time complexity of the sieve is $O(n \log \log n)$.
> - **Space Complexity:** $O(n)$ since we're using a boolean array of size `right + 1` to store the prime numbers.
> - **Optimality proof:** This approach is optimal because it uses a sieve to generate all prime numbers up to `right`, which is the most efficient way to find all prime numbers in a given range.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sieve of Eratosthenes, prime number generation.
- Problem-solving patterns identified: Using a sieve to generate all prime numbers up to a given range, and then finding the closest one to a given number.
- Optimization techniques learned: Using a sieve to reduce the time complexity of generating prime numbers.
- Similar problems to practice: Generating all prime numbers up to a given range, finding the closest prime number to a given number.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `isPrime` array correctly, not marking the multiples of each prime number as `false`.
- Edge cases to watch for: When `left` is a prime number, when there are no prime numbers in the range.
- Performance pitfalls: Using a brute force approach to generate prime numbers, not using a sieve to reduce the time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases and large ranges.