## Smallest Index With Equal Value

**Problem Link:** https://leetcode.com/problems/smallest-index-with-equal-value/description

**Problem Statement:**
- Input: Two integer arrays `index` and `value`
- Constraints: Both arrays have the same length, and the elements in `index` are distinct.
- Expected Output: An array of integers where for each index `i`, the output at `i` is the smallest index `j` such that `index[j] == i` and `value[j] == value[i]`.
- Key Requirements:
  - For each index `i`, find the smallest index `j` that satisfies both conditions.
  - If no such index `j` exists, the value at `i` in the output should be `-1`.
- Example Test Cases:
  - `index = [0,1,2]`, `value = [0,1,2]`: The output should be `[0,1,2]` because for each index `i`, the smallest index `j` that satisfies both conditions is `i` itself.
  - `index = [0,0,1,2]`, `value = [0,1,2,1]`: The output should be `[0,-1,2,-1]` because for `index[0] = 0` and `value[0] = 0`, the smallest such index is `0`. For `index[1] = 0` and `value[1] = 1`, no such index exists, so it's `-1`. For `index[2] = 1` and `value[2] = 2`, the smallest such index is `2`. For `index[3] = 2` and `value[3] = 1`, no such index exists, so it's `-1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through each element in the `index` array and for each element, iterate through the entire array again to find the smallest index that satisfies both conditions.
- This approach is straightforward but inefficient for large inputs.

```cpp
vector<int> smallestEqual(vector<int>& index, vector<int>& value) {
    int n = index.size();
    vector<int> result(n, -1);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (index[j] == i && value[j] == value[i]) {
                result[i] = j;
                break;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input arrays. This is because for each element, we potentially iterate through the entire array.
> - **Space Complexity:** $O(n)$, for the output array.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity, and the output array leads to the linear space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to iterate through the arrays only once and keep track of the smallest index for each value and its corresponding index in the `index` array.
- We use a map to store the smallest index found so far for each value and its corresponding index.

```cpp
vector<int> smallestEqual(vector<int>& index, vector<int>& value) {
    int n = index.size();
    vector<int> result(n, -1);
    map<pair<int, int>, int> smallestIndex;
    for (int i = 0; i < n; i++) {
        if (smallestIndex.find({index[i], value[i]}) != smallestIndex.end()) {
            result[i] = smallestIndex[{index[i], value[i]}];
        } else {
            smallestIndex[{index[i], value[i]}] = i;
        }
    }
    return result;
}
```

However, the above optimal approach can be further optimized by directly checking if the current index matches the value and updating the result array accordingly, without the need for a map.

```cpp
vector<int> smallestEqual(vector<int>& index, vector<int>& value) {
    int n = index.size();
    vector<int> result(n, -1);
    for (int i = 0; i < n; i++) {
        if (index[i] == value[i]) {
            result[i] = i;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (index[i] == index[j] && value[i] == value[j] && result[i] == -1) {
                result[i] = j;
                break;
            }
        }
    }
    return result;
}
```

But the most optimal solution is to simply iterate through the array and directly find the smallest index that matches both the index and value.

```cpp
vector<int> smallestEqual(vector<int>& index, vector<int>& value) {
    int n = index.size();
    vector<int> result(n, -1);
    for (int i = 0; i < n; i++) {
        if (index[i] == value[i]) {
            result[index[i]] = i;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input arrays. This is because we make a single pass through the arrays.
> - **Space Complexity:** $O(n)$, for the output array.
> - **Optimality proof:** This is the best possible complexity because we must at least read the input once, which takes $O(n)$ time.

---

### Final Notes

**Learning Points:**
- The importance of iterating through the input only once to achieve optimal time complexity.
- Using the properties of the input (distinct indices) to simplify the solution.
- Avoiding unnecessary data structures and focusing on the essential operations required to solve the problem.

**Mistakes to Avoid:**
- Overcomplicating the solution with unnecessary data structures or operations.
- Not leveraging the given constraints (distinct indices) to simplify the solution.
- Not considering the possibility of a single pass through the input to achieve optimal time complexity.