## Check If Array Pairs Are Divisible By K
**Problem Link:** https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description

**Problem Statement:**
- Input: An integer array `A` and an integer `k`.
- Constraints: `1 <= A.length <= 10^5` and `1 <= k <= 10^5`.
- Expected output: A boolean indicating whether the array can be divided into pairs such that each pair's sum is divisible by `k`.
- Key requirements: The array must be divided into pairs, and the sum of each pair must be divisible by `k`.
- Edge cases: An empty array, an array with an odd length, or an array with pairs that cannot be divided evenly by `k`.

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible pairs of elements in the array.
- We can generate all permutations of the array and check each pair's sum to see if it's divisible by `k`.
- However, this approach is inefficient due to its high time complexity.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool canArrange(vector<int>& A, int k) {
    // Sort the array
    sort(A.begin(), A.end());

    // Try all possible pairs
    for (int i = 0; i < A.size(); i++) {
        for (int j = i + 1; j < A.size(); j++) {
            if ((A[i] + A[j]) % k == 0) {
                // Remove the pair from the array
                A.erase(A.begin() + j);
                A.erase(A.begin() + i);
                i--;
                break;
            }
        }
        if (A.size() == 0) return true;
    }
    return A.size() == 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot n!)$, where $n$ is the length of the array. This is because we're trying all permutations of the array and checking each pair's sum.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the array. This is because we're storing the array and its permutations.
> - **Why these complexities occur:** The high time complexity is due to trying all permutations of the array, which results in a factorial number of operations.

### Optimal Approach (Required)
**Explanation:**
- The key insight is that we only need to consider the remainders of the elements in the array when divided by `k`.
- We can use a hash map to store the frequency of each remainder.
- For each remainder `i`, we need to find a remainder `k - i` such that their sum is divisible by `k`.
- If we can find such pairs for all elements, then the array can be divided into pairs such that each pair's sum is divisible by `k`.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

bool canArrange(vector<int>& A, int k) {
    unordered_map<int, int> remainderCount;
    for (int num : A) {
        int remainder = num % k;
        if (remainder < 0) remainder += k; // Handle negative numbers
        remainderCount[remainder]++;
    }

    for (int i = 1; i <= k / 2; i++) {
        if (remainderCount[i] != remainderCount[k - i]) return false;
    }
    return remainderCount[0] % 2 == 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array. This is because we're iterating over the array once to count the remainders.
> - **Space Complexity:** $O(k)$, where $k$ is the divisor. This is because we're storing the frequency of each remainder in a hash map.
> - **Optimality proof:** This approach is optimal because we're only considering the necessary information (the remainders of the elements) and using a hash map to store and compare the frequencies efficiently.

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: hash maps, remainders, and frequency counting.
- Problem-solving patterns identified: using remainders to simplify the problem and finding pairs with a specific property.
- Optimization techniques learned: using a hash map to store and compare frequencies efficiently.

**Mistakes to Avoid:**
- Common implementation errors: not handling negative numbers correctly, not checking for empty arrays or arrays with an odd length.
- Edge cases to watch for: arrays with pairs that cannot be divided evenly by `k`, arrays with a large number of elements.
- Performance pitfalls: using inefficient algorithms or data structures, such as trying all permutations of the array.
- Testing considerations: testing the function with different inputs, including edge cases and large arrays.