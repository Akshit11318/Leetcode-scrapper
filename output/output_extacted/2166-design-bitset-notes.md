## Design Bitset
**Problem Link:** https://leetcode.com/problems/design-bitset/description

**Problem Statement:**
- Input format and constraints: The `Bitset` class will be instantiated and called as such: `Bitset(int size)`, `fix(int idx)`, `unfix(int idx)`, `flip()`, `all()`, `one()`, `count()`, `toString()`.
- Expected output format: Each method should return the expected output based on the state of the bitset.
- Key requirements and edge cases to consider: The bitset can be initialized with a size, and then various operations can be performed on it such as fixing, unfixing, flipping, and checking for all, one, or counting the number of ones.
- Example test cases with explanations: For example, initializing a bitset of size 5, fixing the 3rd index, flipping the bitset, and then checking if all bits are set.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to implement a bitset is by using an array of booleans where each boolean represents a bit.
- Step-by-step breakdown of the solution: 
  1. Initialize an array of booleans with the given size.
  2. Implement the `fix` method by setting the corresponding index in the array to true.
  3. Implement the `unfix` method by setting the corresponding index in the array to false.
  4. Implement the `flip` method by iterating through the array and flipping each bit.
  5. Implement the `all` method by checking if all bits in the array are true.
  6. Implement the `one` method by checking if at least one bit in the array is true.
  7. Implement the `count` method by counting the number of true bits in the array.
  8. Implement the `toString` method by converting the array of booleans into a string of '1's and '0's.
- Why this approach comes to mind first: It is straightforward and easy to understand, making it a natural first step.

```cpp
class Bitset {
private:
    vector<bool> bits;
    int countOnes;

public:
    Bitset(int size) : bits(size, false), countOnes(0) {}

    void fix(int idx) {
        if (!bits[idx]) {
            bits[idx] = true;
            countOnes++;
        }
    }

    void unfix(int idx) {
        if (bits[idx]) {
            bits[idx] = false;
            countOnes--;
        }
    }

    void flip() {
        for (int i = 0; i < bits.size(); i++) {
            bits[i] = !bits[i];
        }
        countOnes = bits.size() - countOnes;
    }

    bool all() {
        return countOnes == bits.size();
    }

    bool one() {
        return countOnes > 0;
    }

    int count() {
        return countOnes;
    }

    string toString() {
        string s;
        for (bool b : bits) {
            s += b ? '1' : '0';
        }
        return s;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for the `flip` method and $O(n)$ for the `toString` method where $n$ is the size of the bitset. All other methods have a time complexity of $O(1)$.
> - **Space Complexity:** $O(n)$ where $n$ is the size of the bitset.
> - **Why these complexities occur:** The time complexity is $O(n)$ for the `flip` and `toString` methods because we need to iterate through the entire array of bits. The space complexity is $O(n)$ because we need to store an array of $n$ bits.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a `bitset` data structure can optimize the space and time complexity of the solution. However, since we are implementing the `Bitset` class ourselves, we can use a single integer to represent the bits, taking advantage of the fact that most systems can handle 64-bit integers.
- Detailed breakdown of the approach: 
  1. Initialize a 64-bit integer to 0.
  2. Implement the `fix` method by using bitwise operations to set the corresponding bit.
  3. Implement the `unfix` method by using bitwise operations to clear the corresponding bit.
  4. Implement the `flip` method by using bitwise operations to flip all bits.
  5. Implement the `all` method by checking if all bits are set using bitwise operations.
  6. Implement the `one` method by checking if at least one bit is set using bitwise operations.
  7. Implement the `count` method by counting the number of set bits using bitwise operations.
  8. Implement the `toString` method by converting the integer into a string of '1's and '0's.
- Why further optimization is impossible: This approach uses a single 64-bit integer to represent the bits, which is the most space-efficient way to store 64 bits. The time complexity is also optimal because we are using bitwise operations, which are typically very fast.

```cpp
class Bitset {
private:
    uint64_t bits;
    int countOnes;

public:
    Bitset(int size) : bits(0), countOnes(0) {}

    void fix(int idx) {
        if (!(bits & (1ULL << idx))) {
            bits |= (1ULL << idx);
            countOnes++;
        }
    }

    void unfix(int idx) {
        if (bits & (1ULL << idx)) {
            bits &= ~(1ULL << idx);
            countOnes--;
        }
    }

    void flip() {
        bits = ~bits;
        countOnes = 64 - countOnes;
    }

    bool all() {
        return countOnes == 64;
    }

    bool one() {
        return countOnes > 0;
    }

    int count() {
        return countOnes;
    }

    string toString() {
        string s;
        for (int i = 63; i >= 0; i--) {
            s += ((bits >> i) & 1) ? '1' : '0';
        }
        return s;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all methods except `toString` which is $O(n)$ where $n$ is the number of bits.
> - **Space Complexity:** $O(1)$ because we are using a fixed-size integer to store the bits.
> - **Optimality proof:** This approach is optimal because it uses a single 64-bit integer to store the bits, which is the most space-efficient way to store 64 bits. The time complexity is also optimal because we are using bitwise operations, which are typically very fast.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, bitwise operations.
- Problem-solving patterns identified: Using a single integer to represent multiple bits.
- Optimization techniques learned: Using bitwise operations to optimize time and space complexity.
- Similar problems to practice: Other bit manipulation problems, such as checking if a number is a power of 2 or counting the number of set bits in a number.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as when the index is out of range.
- Edge cases to watch for: When the index is out of range, when the bitset is empty.
- Performance pitfalls: Using a naive approach that has a high time or space complexity.
- Testing considerations: Test the bitset with different sizes, test the `fix`, `unfix`, `flip`, `all`, `one`, `count`, and `toString` methods.