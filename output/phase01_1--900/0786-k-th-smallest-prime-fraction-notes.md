## K-th Smallest Prime Fraction

**Problem Link:** https://leetcode.com/problems/k-th-smallest-prime-fraction/description

**Problem Statement:**
- Input format and constraints: Given a sorted array of distinct integers `arr` and an integer `k`, return the k-th smallest prime fraction. The prime fraction is a fraction where the numerator and denominator are both prime numbers.
- Expected output format: The k-th smallest prime fraction in the form of a string, where the numerator and denominator are separated by a slash.
- Key requirements and edge cases to consider: The input array `arr` is sorted and contains distinct integers. The integer `k` is a positive integer.
- Example test cases with explanations:
  - Example 1: Input: `arr = [1,2,3,5], k = 3`, Output: `"2/5"`. Explanation: The prime fractions are `["1/2", "1/3", "2/3", "1/5", "2/5", "3/5"]`. The 3rd smallest prime fraction is `"2/5"`.
  - Example 2: Input: `arr = [1,7], k = 1`, Output: `"1/7"`. Explanation: The prime fractions are `["1/7"]`. The 1st smallest prime fraction is `"1/7"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible fractions with the given array and then filtering out the ones that are not prime fractions.
- Step-by-step breakdown of the solution:
  1. Generate all possible fractions with the given array.
  2. Filter out the fractions that are not prime fractions.
  3. Sort the prime fractions in ascending order.
  4. Return the k-th smallest prime fraction.
- Why this approach comes to mind first: The brute force approach is often the most straightforward solution, and it can be used as a starting point to develop more efficient solutions.

```cpp
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

std::string kthSmallestPrimeFraction(std::vector<int>& arr, int k) {
    std::vector<std::pair<int, int>> fractions;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
            if (isPrime(arr[i]) && isPrime(arr[j])) {
                fractions.push_back({arr[i], arr[j]});
            }
        }
    }
    std::sort(fractions.begin(), fractions.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
        return a.first * b.second < a.second * b.first;
    });
    return std::to_string(fractions[k - 1].first) + "/" + std::to_string(fractions[k - 1].second);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log n)$, where $n$ is the size of the input array. The reason is that we generate all possible fractions ($O(n^2)$) and then sort them ($O(n \log n)$).
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the input array. The reason is that we store all possible fractions in a vector.
> - **Why these complexities occur:** The brute force approach involves generating all possible fractions and then sorting them, which results in a high time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to store the fractions and their corresponding values. The priority queue will allow us to efficiently extract the smallest fraction.
- Detailed breakdown of the approach:
  1. Initialize a priority queue to store the fractions and their corresponding values.
  2. Push the initial fractions into the priority queue.
  3. Pop the smallest fraction from the priority queue and push the next fraction into the queue.
  4. Repeat step 3 until we have popped $k$ fractions from the queue.
  5. The last popped fraction is the k-th smallest prime fraction.
- Proof of optimality: The priority queue ensures that we always pop the smallest fraction, which means that we are guaranteed to find the k-th smallest prime fraction in $O(k \log n)$ time.
- Why further optimization is impossible: The priority queue is the most efficient data structure for this problem, and we are already using it optimally.

```cpp
#include <queue>
#include <vector>
#include <string>
#include <iostream>

struct Fraction {
    int numerator;
    int denominator;
    double value;
    Fraction(int n, int d) : numerator(n), denominator(d), value((double)n / d) {}
    bool operator<(const Fraction& other) const {
        return value > other.value;
    }
};

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

std::string kthSmallestPrimeFraction(std::vector<int>& arr, int k) {
    std::priority_queue<Fraction> queue;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
            if (isPrime(arr[i]) && isPrime(arr[j])) {
                queue.push(Fraction(arr[i], arr[j]));
            }
        }
    }
    for (int i = 0; i < k - 1; i++) {
        queue.pop();
    }
    Fraction result = queue.top();
    return std::to_string(result.numerator) + "/" + std::to_string(result.denominator);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log k)$, where $n$ is the size of the input array and $k$ is the input integer. The reason is that we push all possible fractions into the priority queue ($O(n^2)$) and then pop $k$ fractions from the queue ($O(k \log n)$).
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the input array. The reason is that we store all possible fractions in a priority queue.
> - **Optimality proof:** The priority queue ensures that we always pop the smallest fraction, which means that we are guaranteed to find the k-th smallest prime fraction in $O(n^2 \log k)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues, sorting, and prime number checking.
- Problem-solving patterns identified: Using a priority queue to efficiently extract the smallest fraction.
- Optimization techniques learned: Using a priority queue to reduce the time complexity.
- Similar problems to practice: Other problems that involve finding the k-th smallest element in a sorted array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for prime numbers correctly, not handling edge cases properly.
- Edge cases to watch for: Empty input array, $k$ is larger than the number of prime fractions.
- Performance pitfalls: Using a naive approach that has a high time complexity.
- Testing considerations: Testing the function with different input arrays and values of $k$.