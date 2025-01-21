## 4Sum II

**Problem Link:** [https://leetcode.com/problems/4sum-ii/description](https://leetcode.com/problems/4sum-ii/description)

**Problem Statement:**
- Given four lists `A`, `B`, `C`, and `D` of size `n`, find the number of tuples `(i, j, k, l)` such that `A[i] + B[j] + C[k] + D[l] == 0`.
- The input lists are non-empty and contain only integers.
- The output should be the count of tuples that satisfy the given condition.
- Key requirements: Handle duplicate elements, consider all possible combinations, and optimize the solution for large inputs.

**Example Test Cases:**
- `A = [1, 2]`, `B = [-2, -1]`, `C = [-1, 2]`, `D = [0, 2]`. The output should be `2` because the tuples `(0, 1, 0, 1)` and `(1, 0, 0, 0)` satisfy the condition.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to use four nested loops to generate all possible tuples `(i, j, k, l)`.
- For each tuple, calculate the sum `A[i] + B[j] + C[k] + D[l]`.
- If the sum equals `0`, increment the count.

```cpp
int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
    int count = 0;
    int n = A.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                for (int l = 0; l < n; l++) {
                    if (A[i] + B[j] + C[k] + D[l] == 0) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the size of the input lists. This is because we have four nested loops, each iterating over the input lists.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count variable.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the four nested loops, making it inefficient for large inputs.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a hash map to store the sums of pairs from two lists and then use this map to find the pairs from the other two lists that sum to the negation of the stored sums.
- This approach reduces the time complexity from $O(n^4)$ to $O(n^2)$.
- We can use a `unordered_map` in C++ to implement the hash map.

```cpp
int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
    int count = 0;
    unordered_map<int, int> sumCount;
    int n = A.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            sumCount[A[i] + B[j]]++;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int sum = C[i] + D[j];
            if (sumCount.find(-sum) != sumCount.end()) {
                count += sumCount[-sum];
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input lists. This is because we have two pairs of nested loops, each iterating over the input lists.
> - **Space Complexity:** $O(n^2)$, as we use a hash map to store the sums of pairs from two lists.
> - **Optimality proof:** This approach is optimal because we reduce the number of iterations from $O(n^4)$ to $O(n^2)$ by using a hash map to store the sums of pairs.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the use of hash maps to optimize solutions.
- The optimal approach reduces the time complexity from $O(n^4)$ to $O(n^2)$.
- The problem requires careful consideration of edge cases, such as duplicate elements.

**Mistakes to Avoid:**
- Not considering the use of hash maps to optimize the solution.
- Not handling duplicate elements correctly.
- Not optimizing the solution for large inputs.

---