## Flattening Nested List Iterator
**Problem Link:** https://leetcode.com/problems/flatten-nested-list-iterator/description

**Problem Statement:**
- Input format and constraints: Given a nested list of integers, implement an iterator to flatten it.
- Expected output format: The iterator should return integers in a flattened sequence.
- Key requirements and edge cases to consider:
  - Handling nested lists of varying depths.
  - Handling empty lists and null elements.
- Example test cases with explanations:
  - Example 1: `[[1,1],2,[3]]` should return integers in the sequence `1, 1, 2, 3`.
  - Example 2: `[1,[4,[6]]]` should return integers in the sequence `1, 4, 6`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: A straightforward approach is to recursively flatten the list and store the integers in a vector.
- Step-by-step breakdown of the solution:
  1. Define a recursive function to flatten the list.
  2. If the current element is an integer, add it to the vector.
  3. If the current element is a list, recursively call the function on each element of the list.
- Why this approach comes to mind first: It directly addresses the problem statement by flattening the list.

```cpp
class NestedIterator {
private:
    vector<int> flattened;
    int index;

public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        flatten(nestedList);
        index = 0;
    }

    void flatten(vector<NestedInteger> &nestedList) {
        for (auto &ni : nestedList) {
            if (ni.isInteger()) {
                flattened.push_back(ni.getInteger());
            } else {
                flatten(ni.getList());
            }
        }
    }

    int next() {
        if (hasNext()) {
            return flattened[index++];
        }
        return -1; // or throw an exception
    }

    bool hasNext() {
        return index < flattened.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the total number of integers in the nested list, because we visit each integer once during the flattening process.
> - **Space Complexity:** $O(N)$, as we store all integers in the `flattened` vector.
> - **Why these complexities occur:** The recursive flattening process requires visiting each integer, leading to linear time complexity. Storing all integers in a vector results in linear space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of storing all integers in a vector, we can use a stack to store the nested lists and integers. This allows us to lazily evaluate the next integer only when needed.
- Detailed breakdown of the approach:
  1. Initialize a stack with the input nested list.
  2. In the `hasNext()` function, pop elements from the stack and push their contents back onto the stack until an integer is found or the stack is empty.
  3. In the `next()` function, return the top integer from the stack and remove it.
- Proof of optimality: This approach minimizes memory usage by only storing the necessary elements in the stack.

```cpp
class NestedIterator {
private:
    stack<NestedInteger> s;

public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        for (auto it = nestedList.rbegin(); it != nestedList.rend(); ++it) {
            s.push(*it);
        }
    }

    int next() {
        NestedInteger top = s.top();
        s.pop();
        return top.getInteger();
    }

    bool hasNext() {
        while (!s.empty() && !s.top().isInteger()) {
            vector<NestedInteger> list = s.top().getList();
            s.pop();
            for (auto it = list.rbegin(); it != list.rend(); ++it) {
                s.push(*it);
            }
        }
        return !s.empty();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the total number of integers in the nested list, because we visit each integer once during the iteration process. However, the `hasNext()` function may perform additional work to find the next integer.
> - **Space Complexity:** $O(N)$, as in the worst case, the stack may store all integers.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to iterate over the nested list, and it uses a stack to efficiently manage the iteration process.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive flattening, lazy evaluation, and stack-based iteration.
- Problem-solving patterns identified: Breaking down complex problems into simpler ones, using data structures like stacks and vectors to manage complexity.
- Optimization techniques learned: Minimizing memory usage by using lazy evaluation and efficient data structures.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases like empty lists or null elements.
- Edge cases to watch for: Nested lists with varying depths, empty lists, and null elements.
- Performance pitfalls: Using inefficient data structures or algorithms that result in high time or space complexity.
- Testing considerations: Thoroughly testing the iterator with different input scenarios to ensure correctness.