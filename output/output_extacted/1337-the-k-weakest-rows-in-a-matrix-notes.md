## The K Weakest Rows in a Matrix

**Problem Link:** https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description

**Problem Statement:**
- Input: A `2D` array `mat` representing a matrix where each row is a soldier and each column represents whether the soldier has completed a task (1) or not (0), and an integer `k`.
- Constraints: 
  - `m == mat.length`
  - `n == mat[i].length`
  - `2 <= n <= 100`
  - `1 <= m <= 1000`
  - `k <= m`
- Expected Output: The indices of the `k` weakest rows in the matrix ordered from weakest to strongest.
- Key Requirements: 
  - Weakest rows are those with the least number of completed tasks (i.e., the least number of `1`s in the row).
  - In case of a tie, the row with the smaller index is considered weaker.

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate the strength of each row by counting the number of `1`s in each row and then sort the rows based on this strength and their original index.
- We can implement this by first calculating the strength of each row and storing it along with the row index, then sorting these pairs based on the strength and index.

```cpp
vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
    vector<pair<int, int>> rowStrengths;
    for (int i = 0; i < mat.size(); ++i) {
        int strength = 0;
        for (int j = 0; j < mat[i].size(); ++j) {
            strength += mat[i][j];
        }
        rowStrengths.push_back({strength, i});
    }
    
    sort(rowStrengths.begin(), rowStrengths.end(), [](const auto& a, const auto& b) {
        if (a.first == b.first) return a.second < b.second;
        return a.first < b.first;
    });
    
    vector<int> weakestRows;
    for (int i = 0; i < k; ++i) {
        weakestRows.push_back(rowStrengths[i].second);
    }
    
    return weakestRows;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n + m \cdot log(m))$ where $m$ is the number of rows and $n$ is the number of columns. The first term accounts for calculating the strength of each row, and the second term is for sorting the rows.
> - **Space Complexity:** $O(m)$ for storing the row strengths and indices.
> - **Why these complexities occur:** These complexities occur because we are iterating through each element in the matrix once to calculate row strengths and then sorting these strengths, which involves comparing and rearranging the rows.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight for the optimal solution is to use a `priority_queue` (or a similar data structure) to directly select the `k` weakest rows without needing to sort all rows.
- However, a more straightforward and efficient approach in terms of code simplicity and execution speed for this particular problem involves using a vector of pairs to store the strength and index of each row and then sorting this vector. The optimal approach in terms of minimizing operations involves using a partial sort or selecting the `k` smallest elements directly without fully sorting the vector, but for simplicity and given the constraints of the problem, a full sort is acceptable and straightforward to implement.

```cpp
vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
    vector<pair<int, int>> rowStrengths;
    for (int i = 0; i < mat.size(); ++i) {
        int strength = accumulate(mat[i].begin(), mat[i].end(), 0);
        rowStrengths.emplace_back(strength, i);
    }
    
    nth_element(rowStrengths.begin(), rowStrengths.begin() + k, rowStrengths.end(), [](const auto& a, const auto& b) {
        if (a.first == b.first) return a.second < b.second;
        return a.first < b.first;
    });
    
    vector<int> weakestRows;
    for (int i = 0; i < k; ++i) {
        weakestRows.push_back(rowStrengths[i].second);
    }
    
    return weakestRows;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n + k \cdot log(m))$ in the worst case for `nth_element`, but practically, it's closer to $O(m \cdot n + m)$ because `nth_element` has a linear average-case time complexity.
> - **Space Complexity:** $O(m)$ for storing the row strengths and indices.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find the `k` weakest rows without unnecessary comparisons or data structure overhead. The use of `nth_element` instead of a full sort reduces the time complexity significantly for large inputs where $k$ is much smaller than $m$.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and how they impact the choice of algorithm.
- Using `nth_element` for partial sorting when only a subset of the sorted data is needed.
- The trade-off between code simplicity and optimization for specific use cases.

**Mistakes to Avoid:**
- Incorrectly assuming that a full sort is always necessary when only a subset of the sorted data is needed.
- Not considering the average-case complexity of algorithms like `nth_element`.
- Failing to validate the input and handle edge cases properly.