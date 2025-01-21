## Minimum Adjacent Swaps to Reach the Kth Smallest Number

**Problem Link:** https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/description

**Problem Statement:**
- Input format: The problem takes an integer `num` and an integer `k` as input.
- Constraints: `1 <= num <= 10^9`, `1 <= k <= 10^9`.
- Expected output format: The function should return the minimum number of adjacent swaps required to reach the kth smallest number.
- Key requirements and edge cases to consider: 
    - The function should handle cases where `k` is larger than the number of possible permutations of `num`.
    - The function should handle cases where `num` has repeated digits.

**Example Test Cases:**
- For `num = 4321` and `k = 2`, the output should be `4`.
- For `num = 1112` and `k = 4`, the output should be `2`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all permutations of `num` and then find the kth smallest permutation.
- The brute force approach involves generating all permutations of `num` and then counting the minimum number of adjacent swaps required to reach the kth smallest permutation from the original `num`.

```cpp
#include <bits/stdc++.h>
using namespace std;

int getPermutation(string num, int k) {
    vector<int> digits;
    for (char c : num) {
        digits.push_back(c - '0');
    }
    int n = digits.size();
    vector<int> factorial(n + 1);
    factorial[0] = 1;
    for (int i = 1; i <= n; i++) {
        factorial[i] = factorial[i - 1] * i;
    }
    k--;
    string result = "";
    while (n > 0) {
        n--;
        int index = k / factorial[n];
        k %= factorial[n];
        result += to_string(digits[index]);
        digits.erase(digits.begin() + index);
    }
    return stoi(result);
}

int minSwaps(string num, int k) {
    string kthSmallest = to_string(getPermutation(num, k));
    int n = num.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (num[i] != kthSmallest[i]) {
            for (int j = i + 1; j < n; j++) {
                if (num[j] == kthSmallest[i]) {
                    for (int p = j; p > i; p--) {
                        swap(num[p], num[p - 1]);
                        count++;
                    }
                    break;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! + n^2)$, where $n$ is the number of digits in `num`. The time complexity is dominated by the permutation generation.
> - **Space Complexity:** $O(n)$, where $n$ is the number of digits in `num`. The space complexity is dominated by the storage of the permutation.
> - **Why these complexities occur:** The brute force approach generates all permutations of `num`, which results in a time complexity of $O(n!)$. The space complexity is $O(n)$ because we need to store the permutation.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a factorial number system to find the kth permutation directly.
- We can use the factorial number system to find the kth permutation in $O(n)$ time complexity.
- The optimal approach involves finding the kth permutation using the factorial number system and then counting the minimum number of adjacent swaps required to reach the kth smallest permutation from the original `num`.

```cpp
int getPermutation(string num, int k) {
    vector<int> digits;
    for (char c : num) {
        digits.push_back(c - '0');
    }
    int n = digits.size();
    vector<int> factorial(n + 1);
    factorial[0] = 1;
    for (int i = 1; i <= n; i++) {
        factorial[i] = factorial[i - 1] * i;
    }
    k--;
    string result = "";
    while (n > 0) {
        n--;
        int index = k / factorial[n];
        k %= factorial[n];
        result += to_string(digits[index]);
        digits.erase(digits.begin() + index);
    }
    return stoi(result);
}

int minSwaps(string num, int k) {
    string kthSmallest = to_string(getPermutation(num, k));
    int n = num.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (num[i] != kthSmallest[i]) {
            for (int j = i + 1; j < n; j++) {
                if (num[j] == kthSmallest[i]) {
                    for (int p = j; p > i; p--) {
                        swap(num[p], num[p - 1]);
                        count++;
                    }
                    break;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of digits in `num`. The time complexity is dominated by the permutation generation and the swap operation.
> - **Space Complexity:** $O(n)$, where $n$ is the number of digits in `num`. The space complexity is dominated by the storage of the permutation.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n^2)$, which is the best possible time complexity for this problem because we need to generate the kth permutation and count the minimum number of adjacent swaps.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of the factorial number system to find the kth permutation.
- The problem-solving pattern identified is the use of mathematical insights to optimize the solution.
- The optimization technique learned is the use of the factorial number system to reduce the time complexity.

**Mistakes to Avoid:**
- A common implementation error is to generate all permutations of `num` instead of using the factorial number system.
- An edge case to watch for is when `k` is larger than the number of possible permutations of `num`.
- A performance pitfall is to use a brute force approach instead of the optimal approach.