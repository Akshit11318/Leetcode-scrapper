## Smallest Number in Infinite Set
**Problem Link:** https://leetcode.com/problems/smallest-number-in-infinite-set/description

**Problem Statement:**
- Input format: An infinite set is represented as a set of integers, and you are given a list of integers `nums` representing the numbers that have been added to the set.
- Constraints: The numbers in `nums` are distinct and non-negative.
- Expected output format: Implement the `SmallestInfiniteSet` class with methods `addNum` and `popSmallest`.
- Key requirements and edge cases to consider: The set should always return the smallest number that has not been added yet when `popSmallest` is called, and numbers added via `addNum` should be excluded from future `popSmallest` calls.
- Example test cases with explanations:
    - `SmallestInfiniteSet s; s.addNum(1); s.addNum(2); s.popSmallest(); s.popSmallest(); s.popSmallest(); s.addNum(3); s.addNum(5); s.popSmallest(); s.popSmallest();`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the smallest number in the infinite set, we can start from 1 and keep checking if the number is in the set or not.
- Step-by-step breakdown of the solution:
    1. Initialize an empty set to store the numbers added via `addNum`.
    2. In the `popSmallest` method, start from 1 and keep incrementing until we find a number that is not in the set.
- Why this approach comes to mind first: It's straightforward and doesn't require any complex data structures or algorithms.

```cpp
class SmallestInfiniteSet {
public:
    set<int> added;
    
    SmallestInfiniteSet() {}
    
    void addNum(int num) {
        added.insert(num);
    }
    
    int popSmallest() {
        int num = 1;
        while (added.count(num)) {
            num++;
        }
        added.insert(num);
        return num;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the set. This is because in the worst-case scenario, we might have to iterate over all elements in the set to find the smallest number.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the set. This is because we are storing all the numbers in the set.
> - **Why these complexities occur:** These complexities occur because we are using a simple set to store the numbers and iterating over the set to find the smallest number.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a combination of a set and a variable to keep track of the smallest number that has not been added yet.
- Detailed breakdown of the approach:
    1. Initialize a set to store the numbers added via `addNum`.
    2. Initialize a variable `smallest` to 1, which represents the smallest number that has not been added yet.
    3. In the `addNum` method, add the number to the set.
    4. In the `popSmallest` method, if the `smallest` number is in the set, increment it until we find a number that is not in the set. Then, add the `smallest` number to the set and return it.
- Proof of optimality: This approach is optimal because we are only iterating over the set when necessary, and we are using a constant amount of extra space to store the `smallest` variable.

```cpp
class SmallestInfiniteSet {
public:
    set<int> added;
    int smallest;
    
    SmallestInfiniteSet() : smallest(1) {}
    
    void addNum(int num) {
        added.insert(num);
    }
    
    int popSmallest() {
        if (added.count(smallest)) {
            while (added.count(smallest)) {
                smallest++;
            }
        }
        int res = smallest;
        added.insert(smallest);
        smallest++;
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `addNum` and $O(n)$ for `popSmallest` in the worst case, where $n$ is the number of elements in the set.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the set.
> - **Optimality proof:** This approach is optimal because we are only iterating over the set when necessary, and we are using a constant amount of extra space to store the `smallest` variable.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a combination of a set and a variable to keep track of the smallest number that has not been added yet.
- Problem-solving patterns identified: Iterating over a set to find the smallest number, and using a variable to keep track of the smallest number.
- Optimization techniques learned: Using a constant amount of extra space to store the `smallest` variable, and only iterating over the set when necessary.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the `smallest` number is in the set before incrementing it.
- Edge cases to watch for: When the `smallest` number is in the set, and when the set is empty.
- Performance pitfalls: Iterating over the set unnecessarily, and using too much extra space.
- Testing considerations: Testing the `addNum` and `popSmallest` methods separately, and testing the class with different inputs and edge cases.