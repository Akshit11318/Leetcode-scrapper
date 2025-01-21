## Peeking Iterator
**Problem Link:** https://leetcode.com/problems/peeking-iterator/description

**Problem Statement:**
- Input format and constraints: You are given an iterator class with `next()` and `hasNext()` methods, and you need to create a `PeekingIterator` class that allows you to `peek()` at the next element without consuming it.
- Expected output format: The `PeekingIterator` class should support `next()`, `hasNext()`, and `peek()` methods.
- Key requirements and edge cases to consider: The `peek()` method should return the next element in the iterator without consuming it. If there are no more elements, `hasNext()` should return `false`.
- Example test cases with explanations:
  - Creating a `PeekingIterator` from an iterator and calling `next()`, `hasNext()`, and `peek()` methods.
  - Checking the behavior when there are no more elements in the iterator.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One possible approach is to store the next element in a variable when `hasNext()` is called, and then return this stored element when `peek()` is called.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `nextElement` to store the next element in the iterator.
  2. When `hasNext()` is called, check if `nextElement` is set. If not, call the underlying iterator's `next()` method to get the next element and store it in `nextElement`.
  3. When `peek()` is called, return the stored `nextElement`.
  4. When `next()` is called, return the stored `nextElement` and reset `nextElement` to `nullptr`.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be the most efficient solution.

```cpp
class PeekingIterator {
private:
    Iterator& iterator;
    int nextElement;

public:
    PeekingIterator(Iterator& iterator) : iterator(iterator), nextElement(0) {}

    int peek() {
        if (!nextElement) {
            nextElement = iterator.next();
        }
        return nextElement;
    }

    int next() {
        if (!nextElement) {
            return iterator.next();
        } else {
            int temp = nextElement;
            nextElement = 0;
            return temp;
        }
    }

    bool hasNext() {
        if (!nextElement) {
            nextElement = iterator.hasNext() ? iterator.next() : 0;
        }
        return nextElement != 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `peek()` and `next()`, $O(1)$ for `hasNext()` if `nextElement` is set, and $O(1)$ for `hasNext()` if `nextElement` is not set (since we call the underlying iterator's `next()` method).
> - **Space Complexity:** $O(1)$ since we only store a single element.
> - **Why these complexities occur:** The time complexity is $O(1)$ because we only perform a constant number of operations in each method. The space complexity is $O(1)$ because we only store a single element.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing the next element in a variable, we can store a boolean flag to indicate whether we have already peeked at the next element.
- Detailed breakdown of the approach:
  1. Initialize a boolean flag `hasPeeked` to `false`.
  2. When `peek()` is called, if `hasPeeked` is `false`, call the underlying iterator's `next()` method to get the next element and store it in a variable. Set `hasPeeked` to `true`.
  3. When `next()` is called, if `hasPeeked` is `true`, return the stored element and reset `hasPeeked` to `false`. Otherwise, call the underlying iterator's `next()` method to get the next element.
  4. When `hasNext()` is called, if `hasPeeked` is `true`, return `true`. Otherwise, call the underlying iterator's `hasNext()` method to check if there are more elements.
- Proof of optimality: This approach is optimal because we only store a single boolean flag and a single element, and we only call the underlying iterator's methods when necessary.

```cpp
class PeekingIterator {
private:
    Iterator& iterator;
    bool hasPeeked;
    int peekedElement;

public:
    PeekingIterator(Iterator& iterator) : iterator(iterator), hasPeeked(false) {}

    int peek() {
        if (!hasPeeked) {
            hasPeeked = true;
            peekedElement = iterator.next();
        }
        return peekedElement;
    }

    int next() {
        if (hasPeeked) {
            hasPeeked = false;
            return peekedElement;
        } else {
            return iterator.next();
        }
    }

    bool hasNext() {
        if (hasPeeked) {
            return true;
        } else {
            return iterator.hasNext();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `peek()`, $O(1)$ for `next()`, and $O(1)$ for `hasNext()`.
> - **Space Complexity:** $O(1)$ since we only store a single boolean flag and a single element.
> - **Optimality proof:** This approach is optimal because we only store a constant amount of information and we only call the underlying iterator's methods when necessary.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a boolean flag to indicate whether we have already peeked at the next element.
- Problem-solving patterns identified: Using a variable to store the next element in the iterator.
- Optimization techniques learned: Avoiding unnecessary calls to the underlying iterator's methods.
- Similar problems to practice: Implementing a custom iterator class.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to reset the `hasPeeked` flag after calling `next()`.
- Edge cases to watch for: Handling the case where there are no more elements in the iterator.
- Performance pitfalls: Calling the underlying iterator's methods unnecessarily.
- Testing considerations: Testing the `peek()` method with and without calling `next()` afterwards.