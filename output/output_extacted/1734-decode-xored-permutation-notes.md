## Decode Xored Permutation

**Problem Link:** https://leetcode.com/problems/decode-xored-permutation/description

**Problem Statement:**
- Input: An array of integers `encoded` representing the XOR of all numbers from 1 to n, where n is the length of `encoded`.
- Constraints: `1 <= encoded.length <= 5 * 10^4`, `encoded.length` is even.
- Expected Output: An array of integers representing the original permutation.
- Key Requirements: The XOR of all numbers from 1 to n is 0 if n is even, and n if n is odd. We can use this property to find the original permutation.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible permutations and check if the XOR of each number in the permutation matches the given encoded array.
- This approach is straightforward but inefficient due to its high time complexity.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> decode(std::vector<int>& encoded) {
    int n = encoded.size() + 1;
    std::vector<int> perm(n);
    for (int i = 1; i <= n; i++) {
        perm[i - 1] = i;
    }
    std::vector<int> result;
    do {
        std::vector<int> temp(n - 1);
        for (int i = 1; i < n; i++) {
            temp[i - 1] = perm[i - 1] ^ perm[i];
        }
        if (temp == encoded) {
            result = perm;
            break;
        }
    } while (std::next_permutation(perm.begin(), perm.end()));
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the length of `encoded` plus one. This is because we are trying all possible permutations of numbers from 1 to n.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `encoded` plus one. This is because we need to store the current permutation and the result.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it tries all possible permutations, which is exponential in the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that the XOR of all numbers from 1 to n is 0 if n is even, and n if n is odd. We can use this property to find the original permutation.
- We can calculate the XOR of all numbers from 1 to n, and then use this value to find the original permutation.

```cpp
std::vector<int> decode(std::vector<int>& encoded) {
    int n = encoded.size() + 1;
    int xor_all = 0;
    for (int i = 1; i <= n; i++) {
        xor_all ^= i;
    }
    int xor_even = 0;
    for (int i = 1; i < encoded.size(); i += 2) {
        xor_even ^= encoded[i];
    }
    std::vector<int> perm(n);
    perm[0] = xor_all ^ xor_even;
    for (int i = 1; i < n; i++) {
        perm[i] = perm[i - 1] ^ encoded[i - 1];
    }
    return perm;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `encoded` plus one. This is because we need to iterate over the input array once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `encoded` plus one. This is because we need to store the result.
> - **Optimality proof:** The optimal approach has a linear time complexity because we only need to iterate over the input array once to find the original permutation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: XOR properties, permutation reconstruction.
- Problem-solving patterns identified: using properties of XOR to simplify the problem.
- Optimization techniques learned: reducing the time complexity from exponential to linear.
- Similar problems to practice: problems involving XOR and permutation reconstruction.

**Mistakes to Avoid:**
- Common implementation errors: incorrect calculation of XOR, incorrect reconstruction of the permutation.
- Edge cases to watch for: handling the case where n is even or odd.
- Performance pitfalls: using a brute force approach with high time complexity.
- Testing considerations: testing the solution with different input sizes and values.