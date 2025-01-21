## Advantage Shuffle
**Problem Link:** https://leetcode.com/problems/advantage-shuffle/description

**Problem Statement:**
- Input: Two integer arrays `A` and `B` of the same length, where `A` has distinct elements.
- Constraints: `1 <= A.length == B.length <= 10^5`, and `0 <= A[i], B[i] <= 10^9`.
- Expected output: An array of the same length as `A` and `B`, where each element is an element from `B` and each element in `B` is used exactly once.
- Key requirements: The goal is to maximize the number of indices `i` such that `A[i] > B[i]`.
- Edge cases: When `A` and `B` have different lengths, or when `A` has duplicate elements.

**Example Test Cases:**

* `A = [2, 7, 11, 15]`, `B = [1, 10, 4, 11]`, the output should be `[1, 11, 4, 10]`.
* `A = [12, 24, 8, 32]`, `B = [13, 25, 32, 11]`, the output should be `[24, 8, 12, 32]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible permutations of `B` and check which one maximizes the number of indices where `A[i] > B[i]`.
- This approach involves generating all permutations of `B`, which has a time complexity of `O(n!)`, where `n` is the length of `B`.
- Then, for each permutation, we compare the elements of `A` and the permutation of `B` to count the number of indices where `A[i] > B[i]`.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void bruteForce(vector<int>& A, vector<int>& B) {
    int n = A.size();
    vector<int> maxPerm = B;
    int maxCount = 0;

    // Generate all permutations of B
    do {
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (A[i] > B[i]) {
                count++;
            }
        }

        // Update maxCount and maxPerm if a better permutation is found
        if (count > maxCount) {
            maxCount = count;
            maxPerm = B;
        }
    } while (next_permutation(B.begin(), B.end()));

    // Print the permutation that maximizes the count
    for (int i = 0; i < n; i++) {
        cout << maxPerm[i] << " ";
    }
    cout << endl;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where `n` is the length of `B`, due to generating all permutations of `B`.
> - **Space Complexity:** $O(n)$, for storing the permutation and other variables.
> - **Why these complexities occur:** The brute force approach generates all permutations of `B`, which has a factorial time complexity. This makes the approach impractical for large inputs.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a greedy approach to match the smallest element in `B` with the largest element in `A` that is still greater than the smallest element in `B`.
- This approach involves sorting both `A` and `B`, then iterating through `A` and `B` to find the optimal matches.
- We use two pointers, one for `A` and one for `B`, to keep track of the current elements being compared.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> advantageCount(vector<int>& A, vector<int>& B) {
    int n = A.size();
    vector<int> result(n);
    vector<pair<int, int>> sortedB;

    // Create a sorted list of pairs (B[i], i) to keep track of the original indices
    for (int i = 0; i < n; i++) {
        sortedB.push_back({B[i], i});
    }

    // Sort A and sortedB in descending order
    sort(A.begin(), A.end(), greater<int>());
    sort(sortedB.begin(), sortedB.end(), greater<pair<int, int>>());

    int left = 0, right = n - 1;
    for (int i = 0; i < n; i++) {
        // If the current element in A is greater than the current element in B,
        // assign the current element in B to the result
        if (A[i] > sortedB[i].first) {
            result[sortedB[i].second] = sortedB[i].first;
        } else {
            // Otherwise, assign the smallest element in B that is not yet assigned
            result[sortedB[right].second] = sortedB[i].first;
            right--;
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where `n` is the length of `A` and `B`, due to sorting `A` and `B`.
> - **Space Complexity:** $O(n)$, for storing the sorted list of pairs and the result.
> - **Optimality proof:** The greedy approach ensures that we maximize the number of indices where `A[i] > B[i]`, as we always choose the smallest element in `B` that is not yet assigned when `A[i]` is not greater than the current element in `B`.

---

### Final Notes

**Learning Points:**
- The importance of sorting and using greedy approaches to solve problems efficiently.
- How to use two pointers to keep track of the current elements being compared.
- The concept of creating a sorted list of pairs to keep track of the original indices.

**Mistakes to Avoid:**
- Not considering the edge cases where `A` and `B` have different lengths or `A` has duplicate elements.
- Not using a greedy approach to maximize the number of indices where `A[i] > B[i]`.
- Not using two pointers to keep track of the current elements being compared.