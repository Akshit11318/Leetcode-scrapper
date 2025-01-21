## Design an Ordered Stream
**Problem Link:** https://leetcode.com/problems/design-an-ordered-stream/description

**Problem Statement:**
- Input format and constraints: The input will consist of an integer `id` and a string `value`. The `id` will be unique for each input.
- Expected output format: The function should return a list of strings for each input. The list should contain all the values that have been inserted so far in the correct order.
- Key requirements and edge cases to consider: The function should maintain the order of the input values based on their `id`. If a value is inserted with an `id` that is not the next expected `id`, the function should return an empty list.
- Example test cases with explanations: 
    - Example 1: 
        - Input: `["OrderedStream", "insert", "insert", "insert", "insert", "insert"]`
        - Output: `[[], ["a"], [], ["b", "c"]], ["d"], ["e"]]`
        - Explanation: The `id` values are inserted in the order 5, 3, 1, 2, 4. The function returns the values in the correct order as they are inserted.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach would involve sorting the input values based on their `id` after each insertion and returning the sorted list.
- Step-by-step breakdown of the solution:
    1. Create a data structure to store the input values with their corresponding `id`.
    2. After each insertion, sort the values based on their `id`.
    3. Return the sorted list of values.
- Why this approach comes to mind first: This approach is straightforward and easy to implement. However, it is not efficient for large inputs because sorting is an expensive operation.

```cpp
class OrderedStream {
public:
    vector<string> insert(int id, string value) {
        // Create a map to store the values with their id
        map<int, string> values;
        // Insert the value into the map
        values[id] = value;
        // Create a list to store the result
        vector<string> result;
        // Iterate over the map to get the values in order
        for (auto& pair : values) {
            // If the id is not the next expected id, return an empty list
            if (pair.first != id) {
                return {};
            }
            // Add the value to the result list
            result.push_back(pair.second);
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation after each insertion.
> - **Space Complexity:** $O(n)$ for storing the input values.
> - **Why these complexities occur:** The brute force approach involves sorting the input values after each insertion, which leads to high time complexity. The space complexity is due to the storage of the input values.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a data structure that maintains the order of the input values based on their `id`. A combination of a map and a pointer to the next expected `id` can achieve this.
- Detailed breakdown of the approach:
    1. Create a map to store the input values with their corresponding `id`.
    2. Initialize a pointer to the next expected `id`.
    3. After each insertion, check if the `id` is the next expected `id`. If it is, add the value to the result list and increment the pointer.
    4. If the `id` is not the next expected `id`, return an empty list.
- Proof of optimality: This approach has a time complexity of $O(1)$ for insertion and $O(n)$ for getting the result, where $n$ is the number of input values. This is optimal because we only iterate over the input values once.

```cpp
class OrderedStream {
private:
    map<int, string> values;
    int ptr;
public:
    vector<string> insert(int id, string value) {
        // Insert the value into the map
        values[id] = value;
        // Create a list to store the result
        vector<string> result;
        // Check if the id is the next expected id
        while (values.find(ptr) != values.end()) {
            // Add the value to the result list
            result.push_back(values[ptr]);
            // Increment the pointer
            ptr++;
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for insertion and $O(n)$ for getting the result.
> - **Space Complexity:** $O(n)$ for storing the input values.
> - **Optimality proof:** This approach is optimal because we only iterate over the input values once, and we use a map to store the values, which allows for efficient insertion and retrieval.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a map to store values with their corresponding `id`, and using a pointer to the next expected `id` to maintain order.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and using a combination of data structures to achieve the optimal solution.
- Optimization techniques learned: Using a map to store values and a pointer to the next expected `id` to reduce the time complexity.
- Similar problems to practice: Problems that involve maintaining order and using data structures to achieve optimal solutions.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the `id` is the next expected `id` before adding the value to the result list.
- Edge cases to watch for: Handling cases where the `id` is not the next expected `id`.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Testing the implementation with different input scenarios to ensure correctness and efficiency.