## Design Phone Directory

**Problem Link:** https://leetcode.com/problems/design-phone-directory/description

**Problem Statement:**
- Input format and constraints: Design a phone directory that allows adding and removing phone numbers, and checking if a number is available. The phone directory should support the following operations: `add`, `remove`, and `check`.
- Expected output format: Implement a class with the specified methods.
- Key requirements and edge cases to consider: Handle duplicate numbers, check for availability, and ensure correct removal.
- Example test cases with explanations:
  - Adding a number and checking its availability.
  - Removing a number and checking its availability after removal.
  - Adding duplicate numbers and checking for errors.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a simple data structure like a list or array to store phone numbers.
- Step-by-step breakdown of the solution:
  1. Create a class `PhoneDirectory` with methods `add`, `remove`, and `check`.
  2. In the `add` method, append the number to the list if it's available.
  3. In the `remove` method, find and remove the number from the list if it exists.
  4. In the `check` method, iterate through the list to check if the number is available.
- Why this approach comes to mind first: Simple and straightforward implementation.

```cpp
class PhoneDirectory {
private:
    vector<int> numbers;
public:
    PhoneDirectory(int maxNumbers) {
        for (int i = 0; i < maxNumbers; i++) {
            numbers.push_back(i);
        }
    }
    
    int add(int number) {
        if (find(numbers.begin(), numbers.end(), number) != numbers.end()) {
            return -1; // Number already exists
        }
        numbers.push_back(number);
        return number;
    }
    
    void remove(int number) {
        auto it = find(numbers.begin(), numbers.end(), number);
        if (it != numbers.end()) {
            numbers.erase(it);
        }
    }
    
    bool check(int number) {
        return find(numbers.begin(), numbers.end(), number) == numbers.end();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `add`, `remove`, and `check` operations, where $n$ is the maximum number of phone numbers.
> - **Space Complexity:** $O(n)$ for storing the phone numbers.
> - **Why these complexities occur:** Linear search and insertion/deletion operations in the vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a `set` data structure for efficient lookup, insertion, and deletion.
- Detailed breakdown of the approach:
  1. Create a class `PhoneDirectory` with methods `add`, `remove`, and `check`.
  2. In the `add` method, insert the number into the set if it's available.
  3. In the `remove` method, erase the number from the set if it exists.
  4. In the `check` method, use the `find` method to check if the number is available.
- Why further optimization is impossible: The `set` data structure provides the most efficient operations for this problem.

```cpp
class PhoneDirectory {
private:
    set<int> numbers;
    int maxNumbers;
    int nextAvailable;
public:
    PhoneDirectory(int maxNumbers) : maxNumbers(maxNumbers), nextAvailable(0) {
        for (int i = 0; i < maxNumbers; i++) {
            numbers.insert(i);
        }
    }
    
    int getAvailableNumber() {
        if (nextAvailable >= maxNumbers) {
            return -1; // No available numbers
        }
        return nextAvailable++;
    }
    
    int add(int number = -1) {
        if (number == -1) {
            number = getAvailableNumber();
            if (number == -1) {
                return -1; // No available numbers
            }
        } else if (numbers.find(number) != numbers.end()) {
            return -1; // Number already exists
        }
        numbers.erase(number);
        return number;
    }
    
    void remove(int number) {
        if (numbers.find(number) == numbers.end()) {
            numbers.insert(number);
        }
    }
    
    bool check(int number) {
        return numbers.find(number) != numbers.end();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `add`, `remove`, and `check` operations, where $n$ is the maximum number of phone numbers.
> - **Space Complexity:** $O(n)$ for storing the phone numbers.
> - **Optimality proof:** The `set` data structure provides the most efficient operations for this problem, with constant time complexity for insertion, deletion, and lookup.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using `set` data structure for efficient lookup, insertion, and deletion.
- Problem-solving patterns identified: Choosing the right data structure for the problem.
- Optimization techniques learned: Using `set` instead of `vector` for efficient operations.
- Similar problems to practice: Implementing other data structures, such as `map` or `queue`, for different problems.

**Mistakes to Avoid:**
- Common implementation errors: Using the wrong data structure for the problem.
- Edge cases to watch for: Handling duplicate numbers, checking for availability, and ensuring correct removal.
- Performance pitfalls: Using linear search and insertion/deletion operations in a vector.
- Testing considerations: Testing for edge cases, such as adding and removing the same number, and checking for availability after removal.