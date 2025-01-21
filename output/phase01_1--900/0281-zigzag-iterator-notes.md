## Zigzag Iterator
**Problem Link:** [https://leetcode.com/problems/zigzag-iterator/description](https://leetcode.com/problems/zigzag-iterator/description)

**Problem Statement:**
- Input format and constraints: The problem requires creating an iterator that takes two vectors as input and returns elements in a zigzag pattern. The input vectors are `v1` and `v2`, and the goal is to create an iterator class `ZigzagIterator` with methods `next()` and `hasNext()`.
- Expected output format: The iterator should return elements in a zigzag pattern, alternating between `v1` and `v2`.
- Key requirements and edge cases to consider: The iterator should handle cases where one vector is longer than the other and should not return any elements once all elements from both vectors have been returned.
- Example test cases with explanations:
  - `v1 = [1, 2]`, `v2 = [3, 4]`: The iterator should return elements in the order `1, 3, 2, 4`.
  - `v1 = [1, 2, 3]`, `v2 = [4, 5]`: The iterator should return elements in the order `1, 4, 2, 5, 3`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves creating a new vector that contains all elements from both input vectors in a zigzag pattern. The `next()` method simply returns the next element from this new vector, and the `hasNext()` method checks if there are any remaining elements.
- Step-by-step breakdown of the solution:
  1. Create a new vector `result` that contains all elements from both input vectors in a zigzag pattern.
  2. Initialize an index `i` to keep track of the current position in the `result` vector.
  3. Implement the `next()` method to return the element at the current index `i` and increment `i`.
  4. Implement the `hasNext()` method to check if the current index `i` is within the bounds of the `result` vector.

```cpp
class ZigzagIterator {
private:
    vector<int> v1;
    vector<int> v2;
    vector<int> result;
    int i;
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        this->v1 = v1;
        this->v2 = v2;
        int size = max(v1.size(), v2.size());
        for (int j = 0; j < size; j++) {
            if (j < v1.size()) {
                result.push_back(v1[j]);
            }
            if (j < v2.size()) {
                result.push_back(v2[j]);
            }
        }
        i = 0;
    }

    int next() {
        return result[i++];
    }

    bool hasNext() {
        return i < result.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the sizes of the input vectors `v1` and `v2`, respectively. This is because we need to create a new vector that contains all elements from both input vectors.
> - **Space Complexity:** $O(n + m)$, as we need to store all elements from both input vectors in the new vector.
> - **Why these complexities occur:** The brute force approach requires creating a new vector that contains all elements from both input vectors, which leads to a time and space complexity of $O(n + m)$.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of creating a new vector that contains all elements from both input vectors, we can use two indices to keep track of the current position in each vector. This allows us to return elements in a zigzag pattern without storing all elements in a new vector.
- Detailed breakdown of the approach:
  1. Initialize two indices `i` and `j` to keep track of the current position in `v1` and `v2`, respectively.
  2. Implement the `next()` method to return the next element from the vector with the smaller index. If the smaller index is in `v1`, increment `i`. Otherwise, increment `j`.
  3. Implement the `hasNext()` method to check if there are any remaining elements in either `v1` or `v2`.
- Proof of optimality: This approach has a time complexity of $O(1)$ for both `next()` and `hasNext()` methods, as we only need to access the current element in each vector. The space complexity is $O(1)$, as we only need to store the two indices.

```cpp
class ZigzagIterator {
private:
    vector<int> v1;
    vector<int> v2;
    int i;
    int j;
    bool flag;
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        this->v1 = v1;
        this->v2 = v2;
        i = 0;
        j = 0;
        flag = true;
    }

    int next() {
        if (flag) {
            if (i < v1.size()) {
                flag = !flag;
                return v1[i++];
            } else {
                return v2[j++];
            }
        } else {
            if (j < v2.size()) {
                flag = !flag;
                return v2[j++];
            } else {
                return v1[i++];
            }
        }
    }

    bool hasNext() {
        return i < v1.size() || j < v2.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we only need to access the current element in each vector.
> - **Space Complexity:** $O(1)$, as we only need to store the two indices.
> - **Optimality proof:** This approach is optimal because we only need to access the current element in each vector, and we do not need to store all elements in a new vector.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using indices to keep track of the current position in each vector, and alternating between vectors to achieve a zigzag pattern.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (e.g., implementing `next()` and `hasNext()` methods separately).
- Optimization techniques learned: Avoiding unnecessary memory allocation and using indices to access elements in vectors.
- Similar problems to practice: Implementing iterators for other patterns (e.g., spiral, diagonal).

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases (e.g., empty vectors), and not handling cases where one vector is longer than the other.
- Edge cases to watch for: Empty vectors, vectors of different lengths, and cases where one vector is much longer than the other.
- Performance pitfalls: Using unnecessary memory allocation or iterating over vectors unnecessarily.
- Testing considerations: Testing the iterator with different input vectors, including edge cases and large inputs.