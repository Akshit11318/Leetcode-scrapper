## Find All Possible Stable Binary Arrays II

**Problem Link:** https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/description

**Problem Statement:**
- Input: An integer `n` representing the size of the binary array.
- Expected output: A list of all possible stable binary arrays of size `n`.
- Key requirements and edge cases to consider:
  - The input `n` is a positive integer.
  - A stable binary array is one where for every index `i`, if the element at `i` is 1, then the elements at `2*i` and `2*i + 1` must be 0.
- Example test cases with explanations:
  - For `n = 2`, the possible stable binary arrays are `[0,0]`, `[0,1]`, and `[1,0]`.
  - For `n = 3`, the possible stable binary arrays are `[0,0,0]`, `[0,0,1]`, `[0,1,0]`, and `[1,0,0]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible binary arrays of size `n` and check each one to see if it's stable.
- Step-by-step breakdown of the solution:
  1. Generate all possible binary arrays of size `n`.
  2. For each binary array, check if it's stable by iterating over each element.
  3. If the element is 1, check if the elements at `2*i` and `2*i + 1` are 0.
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it's not efficient for large values of `n`.

```cpp
vector<vector<int>> generateStableArrays(int n) {
    vector<vector<int>> result;
    int max = 1 << n; // 2^n
    for (int i = 0; i < max; i++) {
        vector<int> arr(n);
        for (int j = 0; j < n; j++) {
            arr[j] = (i >> j) & 1;
        }
        if (isStable(arr)) {
            result.push_back(arr);
        }
    }
    return result;
}

bool isStable(vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == 1) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            if (left < arr.size() && arr[left] == 1) {
                return false;
            }
            if (right < arr.size() && arr[right] == 1) {
                return false;
            }
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the binary array. The reason is that we generate all possible binary arrays of size $n$ (which is $2^n$) and for each array, we check if it's stable (which takes $O(n)$ time).
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the binary array. The reason is that we store all possible stable binary arrays of size $n$.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible binary arrays and check each one. The space complexity occurs because we store all possible stable binary arrays.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible binary arrays and checking if they're stable, we can generate only the stable binary arrays using a recursive approach.
- Detailed breakdown of the approach:
  1. Start with an empty binary array.
  2. For each position in the array, if it's not the child of a 1, we can either put a 0 or a 1.
  3. If we put a 1, then the children of this position must be 0.
- Proof of optimality: This approach generates only the stable binary arrays, so it's more efficient than the brute force approach.

```cpp
vector<vector<int>> generateStableArrays(int n) {
    vector<vector<int>> result;
    vector<int> arr(n);
    generateStableArraysHelper(arr, 0, result);
    return result;
}

void generateStableArraysHelper(vector<int>& arr, int index, vector<vector<int>>& result) {
    if (index == arr.size()) {
        result.push_back(arr);
        return;
    }
    if (isParentOne(arr, index)) {
        arr[index] = 0;
        generateStableArraysHelper(arr, index + 1, result);
    } else {
        arr[index] = 0;
        generateStableArraysHelper(arr, index + 1, result);
        arr[index] = 1;
        generateStableArraysHelper(arr, index + 1, result);
    }
}

bool isParentOne(vector<int>& arr, int index) {
    if (index == 0) {
        return false;
    }
    int parent = (index - 1) / 2;
    return arr[parent] == 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n/2})$, where $n$ is the size of the binary array. The reason is that we generate only the stable binary arrays using a recursive approach.
> - **Space Complexity:** $O(2^{n/2})$, where $n$ is the size of the binary array. The reason is that we store all possible stable binary arrays of size $n$.
> - **Optimality proof:** This approach generates only the stable binary arrays, so it's more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive approach, backtracking.
- Problem-solving patterns identified: Generating all possible solutions and checking if they're valid.
- Optimization techniques learned: Using a recursive approach to generate only the valid solutions.
- Similar problems to practice: Generating all possible binary trees, generating all possible permutations of a string.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the parent of a node is 1 before putting a 1 in the child node.
- Edge cases to watch for: The base case of the recursion, where the index is equal to the size of the array.
- Performance pitfalls: Generating all possible binary arrays and checking if they're stable, which has a time complexity of $O(2^n \cdot n)$.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure it generates all possible stable binary arrays.