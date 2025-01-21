## First Unique Number
**Problem Link:** https://leetcode.com/problems/first-unique-number/description

**Problem Statement:**
- Input format and constraints: You are given a `UniqueNumber` class with methods `add` and `firstUnique`. The `add` method takes an integer as input and adds it to the internal data structure. The `firstUnique` method returns the first unique number in the data structure, or -1 if no unique number exists.
- Expected output format: The `firstUnique` method should return an integer representing the first unique number.
- Key requirements and edge cases to consider: The data structure should efficiently handle a large number of `add` operations and `firstUnique` queries.
- Example test cases with explanations:
  - `UniqueNumber uniqueNumber; uniqueNumber.add(2); uniqueNumber.add(3); uniqueNumber.add(5);` The `firstUnique` method should return 2.
  - `UniqueNumber uniqueNumber; uniqueNumber.add(7); uniqueNumber.add(3); uniqueNumber.add(5); uniqueNumber.add(5); uniqueNumber.add(7); uniqueNumber.add(4);` The `firstUnique` method should return 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can store all the numbers in a vector and then iterate through the vector to find the first unique number.
- Step-by-step breakdown of the solution:
  1. Create a vector to store all the numbers.
  2. In the `add` method, push the number onto the vector.
  3. In the `firstUnique` method, iterate through the vector and check if the count of each number is 1. If it is, return that number.
- Why this approach comes to mind first: It is simple and straightforward, but it is not efficient for large inputs.

```cpp
class UniqueNumber {
public:
    vector<int> nums;
    void add(int num) {
        nums.push_back(num);
    }
    int firstUnique() {
        for (int num : nums) {
            int count = 0;
            for (int n : nums) {
                if (n == num) count++;
            }
            if (count == 1) return num;
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of `add` operations. This is because in the `firstUnique` method, we are iterating through the vector for each number.
> - **Space Complexity:** $O(n)$, where $n$ is the number of `add` operations. This is because we are storing all the numbers in the vector.
> - **Why these complexities occur:** The brute force approach has high time complexity because of the nested loops in the `firstUnique` method. The space complexity is linear because we are storing all the numbers in the vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use an unordered_map to store the count of each number and a queue to store the order of the numbers.
- Detailed breakdown of the approach:
  1. Create an unordered_map to store the count of each number.
  2. Create a queue to store the order of the numbers.
  3. In the `add` method, increment the count of the number in the map and push the number onto the queue.
  4. In the `firstUnique` method, iterate through the queue and check if the count of the number is 1. If it is, return that number.
- Why further optimization is impossible: This approach has the best possible time and space complexity.

```cpp
class UniqueNumber {
public:
    unordered_map<int, int> count;
    queue<int> q;
    void add(int num) {
        count[num]++;
        q.push(num);
    }
    int firstUnique() {
        while (!q.empty()) {
            if (count[q.front()] == 1) return q.front();
            q.pop();
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for the `add` method and $O(n)$ for the `firstUnique` method, where $n$ is the number of `add` operations. This is because we are using an unordered_map to store the count of each number and a queue to store the order of the numbers.
> - **Space Complexity:** $O(n)$, where $n$ is the number of `add` operations. This is because we are storing all the numbers in the map and queue.
> - **Optimality proof:** This approach has the best possible time and space complexity because we are using the most efficient data structures for the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using an unordered_map to store the count of each number and a queue to store the order of the numbers.
- Problem-solving patterns identified: Using a combination of data structures to solve a problem.
- Optimization techniques learned: Using an unordered_map to reduce the time complexity of the `add` method and a queue to reduce the time complexity of the `firstUnique` method.
- Similar problems to practice: Other problems that involve using a combination of data structures to solve a problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the number is already in the map before incrementing its count.
- Edge cases to watch for: When the queue is empty, the `firstUnique` method should return -1.
- Performance pitfalls: Using a nested loop to iterate through the numbers, which can result in high time complexity.
- Testing considerations: Testing the `add` and `firstUnique` methods separately and together to ensure they are working correctly.