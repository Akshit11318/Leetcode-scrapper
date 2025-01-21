## RLE Iterator

**Problem Link:** [https://leetcode.com/problems/rle-iterator/description](https://leetcode.com/problems/rle-iterator/description)

**Problem Statement:**
- Input format: The input is a list of integers `A` where each pair of integers represents a run-length encoding (RLE) of a sequence. The first integer in each pair is the count, and the second integer is the value.
- Constraints: `2 <= A.length <= 1000`, `A.length % 2 == 0`, `0 <= A[i] <= 10^9`, `A[0]` and `A[1]` are not zero.
- Expected output format: Implement an iterator class `RLEIterator` that supports two methods:
  - `next(int n)`: Returns the next value from the sequence if `n` is within the current run-length. If `n` exceeds the current run-length, move to the next run-length and return the value. If `n` exceeds the total length of the sequence, return `-1`.
  - `hasNext(int n)`: Returns `true` if `n` is within the current run-length or can be accommodated by moving to subsequent run-lengths, and `false` otherwise.
- Key requirements and edge cases to consider:
  - Handling cases where `n` exceeds the current run-length but not the total sequence length.
  - Ensuring the iterator moves correctly between run-lengths.
  - Returning `-1` when `n` exceeds the total sequence length.
- Example test cases with explanations:
  - `RLEIterator rleIterator = new RLEIterator([3,8,0,9,2,5]); rleIterator.next(2); rleIterator.next(1); rleIterator.next(1);` should return `8, 8, 5`.
  - `rleIterator.hasNext(2); rleIterator.hasNext(3);` should return `false, false` because there are not enough elements left in the sequence.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One might start by iterating through the sequence each time `next(int n)` is called, decrementing `n` until it reaches zero or the end of the sequence is encountered.
- Step-by-step breakdown of the solution:
  1. Initialize an index `i` to keep track of the current position in the sequence.
  2. When `next(int n)` is called, iterate from the current index `i` through the sequence, decrementing `n` by the count of each run-length until `n` reaches zero or the end of the sequence is reached.
  3. If `n` becomes zero, return the value of the current run-length. If `n` exceeds the remaining length of the sequence, return `-1`.
- Why this approach comes to mind first: It directly simulates the process described in the problem statement but is inefficient because it involves repeated iteration through the sequence.

```cpp
class RLEIterator {
private:
    vector<int> A;
    int index;
public:
    RLEIterator(vector<int>& A) {
        this->A = A;
        index = 0;
    }
    
    int next(int n) {
        while (index < A.size()) {
            if (n <= A[index]) {
                A[index] -= n;
                return A[index + 1];
            } else {
                n -= A[index];
                index += 2;
            }
        }
        return -1;
    }
    
    bool hasNext(int n) {
        while (index < A.size()) {
            if (n <= A[index]) {
                return true;
            } else {
                n -= A[index];
                index += 2;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{n}{2} + k)$ where $n$ is the total length of the sequence and $k$ is the number of `next` or `hasNext` operations. Each operation could potentially scan the entire sequence in the worst case.
> - **Space Complexity:** $O(1)$, excluding the input sequence, because we only use a constant amount of space to store the index and other variables.
> - **Why these complexities occur:** The brute force approach scans the sequence for each operation, leading to high time complexity. Space complexity is low because we do not allocate any additional data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of scanning the sequence from the beginning for each operation, we can maintain a pointer to the current run-length and update it as we consume elements from the sequence.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `index` to track the current run-length and `remaining` to track how many elements are remaining in the current run-length.
  2. When `next(int n)` is called, first check if `n` is within the `remaining` count of the current run-length. If so, subtract `n` from `remaining` and return the value of the current run-length.
  3. If `n` exceeds `remaining`, subtract `remaining` from `n` and move to the next run-length by incrementing `index` by 2. Repeat this process until `n` is within a run-length or the end of the sequence is reached.
- Proof of optimality: This approach minimizes the number of operations by only moving the pointer when necessary and avoiding repeated scans of the sequence.

```cpp
class RLEIterator {
private:
    vector<int> A;
    int index;
public:
    RLEIterator(vector<int>& A) {
        this->A = A;
        index = 0;
    }
    
    int next(int n) {
        while (index < A.size()) {
            if (n <= A[index]) {
                A[index] -= n;
                return A[index + 1];
            } else {
                n -= A[index];
                index += 2;
            }
        }
        return -1;
    }
    
    bool hasNext(int n) {
        while (index < A.size()) {
            if (n <= A[index]) {
                return true;
            } else {
                n -= A[index];
                index += 2;
            }
        }
        return false;
    }
};
```

However, to make this solution truly optimal and avoid the confusion with the brute force, we should initialize `remaining` with the count of the first run-length and update it accordingly as we consume elements:

```cpp
class RLEIterator {
private:
    vector<int> A;
    int index;
    int remaining;
public:
    RLEIterator(vector<int>& A) {
        this->A = A;
        index = 0;
        remaining = A[index];
    }
    
    int next(int n) {
        while (index < A.size()) {
            if (n <= remaining) {
                remaining -= n;
                return A[index + 1];
            } else {
                n -= remaining;
                index += 2;
                if (index < A.size()) {
                    remaining = A[index];
                }
            }
        }
        return -1;
    }
    
    bool hasNext(int n) {
        while (index < A.size()) {
            if (n <= remaining) {
                return true;
            } else {
                n -= remaining;
                index += 2;
                if (index < A.size()) {
                    remaining = A[index];
                }
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$ where $k$ is the number of `next` or `hasNext` operations. Each operation potentially moves the pointer once.
> - **Space Complexity:** $O(1)$, excluding the input sequence, because we only use a constant amount of space to store the index and `remaining`.
> - **Optimality proof:** This solution is optimal because it minimizes the number of operations by maintaining a pointer to the current position in the sequence and only moving it when necessary.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Run-length encoding, iterator design, and pointer management.
- Problem-solving patterns identified: The importance of maintaining a pointer or index to the current position in a sequence to avoid repeated scans.
- Optimization techniques learned: Minimizing the number of operations by only updating the pointer when necessary.
- Similar problems to practice: Other iterator or pointer-based problems, such as designing an iterator for a specific data structure.

**Mistakes to Avoid:**
- Common implementation errors: Failing to update the `remaining` count correctly or not checking for the end of the sequence.
- Edge cases to watch for: Handling cases where `n` exceeds the current run-length but not the total sequence length, and ensuring the iterator moves correctly between run-lengths.
- Performance pitfalls: Using a brute force approach that scans the sequence for each operation, leading to high time complexity.
- Testing considerations: Thoroughly testing the iterator with various sequences and `next`/`hasNext` operations to ensure correct behavior.