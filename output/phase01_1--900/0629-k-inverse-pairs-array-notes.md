## K Inverse Pairs Array
**Problem Link:** [https://leetcode.com/problems/k-inverse-pairs-array/description](https://leetcode.com/problems/k-inverse-pairs-array/description)

**Problem Statement:**
- Input format: `n` and `k`, where `n` is the size of the array and `k` is the number of inverse pairs.
- Constraints: `1 <= n <= 1000` and `0 <= k <= n*(n-1)/2`.
- Expected output format: The `k`-th lexicographically smallest array with `n` elements and `k` inverse pairs.
- Key requirements and edge cases to consider: The array should contain distinct integers from `1` to `n`, and the number of inverse pairs should be exactly `k`.
- Example test cases with explanations: For `n = 3` and `k = 1`, the output should be `[2,1,3]`, which is the lexicographically smallest array with `3` elements and `1` inverse pair.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible permutations of the array and count the number of inverse pairs in each permutation.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the array using a recursive function or an iterative approach.
  2. For each permutation, count the number of inverse pairs by comparing each pair of elements.
  3. Store the permutations with `k` inverse pairs in a separate data structure.
  4. Sort the stored permutations lexicographically and return the `k`-th smallest one.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void generatePermutations(vector<int>& arr, int start, int end, vector<vector<int>>& permutations) {
    if (start == end) {
        permutations.push_back(arr);
    } else {
        for (int i = start; i <= end; i++) {
            swap(arr[start], arr[i]);
            generatePermutations(arr, start + 1, end, permutations);
            swap(arr[start], arr[i]);
        }
    }
}

int countInversePairs(const vector<int>& arr) {
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
            if (arr[i] > arr[j]) {
                count++;
            }
        }
    }
    return count;
}

vector<int> kInversePairs(int n, int k) {
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }

    vector<vector<int>> permutations;
    generatePermutations(arr, 0, n - 1, permutations);

    vector<vector<int>> kInversePairsPermutations;
    for (const auto& permutation : permutations) {
        if (countInversePairs(permutation) == k) {
            kInversePairsPermutations.push_back(permutation);
        }
    }

    sort(kInversePairsPermutations.begin(), kInversePairsPermutations.end());

    return kInversePairsPermutations[k - 1];
}

int main() {
    int n = 3;
    int k = 1;
    vector<int> result = kInversePairs(n, k);
    for (int num : result) {
        cout << num << " ";
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n^2)$, where $n!$ is the number of permutations and $n^2$ is the time complexity of counting inverse pairs in each permutation.
> - **Space Complexity:** $O(n! \cdot n)$, where $n!$ is the number of permutations and $n$ is the size of each permutation.
> - **Why these complexities occur:** The brute force approach generates all permutations of the array, which results in a time complexity of $O(n!)$, and then counts the number of inverse pairs in each permutation, which takes $O(n^2)$ time.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use dynamic programming to store the number of inverse pairs for each subarray.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` where `dp[i][j]` represents the number of ways to arrange the first `i` elements with `j` inverse pairs.
  2. Initialize `dp[0][0] = 1`, since there is one way to arrange an empty array with no inverse pairs.
  3. For each `i` from `1` to `n`, and each `j` from `0` to `k`, calculate `dp[i][j]` by considering the number of ways to place the `i`-th element in the array.
  4. The `k`-th lexicographically smallest array with `n` elements and `k` inverse pairs can be constructed by tracing back the `dp` array.

```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<int> kInversePairs(int n, int k) {
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
    dp[0][0] = 1;

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= k; j++) {
            for (int p = 0; p <= i && p * (i - p) <= j; p++) {
                if (j - p * (i - p) >= 0) {
                    dp[i][j] += dp[i - 1][j - p * (i - p)];
                }
            }
        }
    }

    vector<int> result(n);
    int remainingK = k;
    for (int i = n - 1; i >= 0; i--) {
        for (int p = 0; p <= i; p++) {
            if (remainingK - p * (i - p) >= 0 && dp[i][remainingK - p * (i - p)] > 0) {
                result[i] = p + 1;
                remainingK -= p * (i - p);
                break;
            }
        }
    }

    return result;
}

int main() {
    int n = 3;
    int k = 1;
    vector<int> result = kInversePairs(n, k);
    for (int num : result) {
        cout << num << " ";
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the size of the array and $k$ is the number of inverse pairs.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the size of the array and $k$ is the number of inverse pairs.
> - **Optimality proof:** The dynamic programming approach stores the number of inverse pairs for each subarray, which reduces the time complexity from $O(n! \cdot n^2)$ to $O(n^2 \cdot k)$. This is the optimal solution, as it uses the minimum amount of time and space required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, permutation generation, and inverse pair counting.
- Problem-solving patterns identified: using dynamic programming to store intermediate results and reducing the time complexity of the algorithm.
- Optimization techniques learned: using a 2D array to store the number of inverse pairs for each subarray and tracing back the array to construct the lexicographically smallest array.

**Mistakes to Avoid:**
- Common implementation errors: incorrect initialization of the `dp` array, incorrect calculation of `dp[i][j]`, and incorrect tracing back of the `dp` array.
- Edge cases to watch for: handling the case where `k` is 0 or `n` is 1.
- Performance pitfalls: using a brute force approach with a high time complexity, not using dynamic programming to store intermediate results.
- Testing considerations: testing the algorithm with different inputs, including edge cases, and verifying the correctness of the output.