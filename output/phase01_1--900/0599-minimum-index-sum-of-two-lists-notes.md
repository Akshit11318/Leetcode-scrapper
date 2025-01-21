## Minimum Index Sum of Two Lists

**Problem Link:** https://leetcode.com/problems/minimum-index-sum-of-two-lists/description

**Problem Statement:**
- Input format and constraints: Two lists of strings representing restaurant names, with constraints on the number of restaurants and the length of their names.
- Expected output format: A list of restaurant names with the minimum index sum.
- Key requirements and edge cases to consider: 
    - Handling cases where a restaurant appears in both lists but with different indices.
    - Handling cases where a restaurant appears in only one list.
    - Handling cases where there are multiple restaurants with the same name but different indices in the same list.
- Example test cases with explanations:
    - `["Shogun", "Tapioca Express", "Burger King", "KFC"]` and `["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]`
    - `["Shogun", "Tapioca Express", "Burger King", "KFC"]` and `["KFC", "Shogun", "Burger King"]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a brute force solution that iterates through all possible pairs of restaurants from the two lists, calculates the sum of their indices, and keeps track of the pair(s) with the minimum sum.
- Step-by-step breakdown of the solution:
    1. Initialize variables to store the minimum index sum and the corresponding restaurant names.
    2. Iterate through all possible pairs of restaurants from the two lists.
    3. For each pair, calculate the sum of their indices.
    4. Update the minimum index sum and the corresponding restaurant names if the current sum is smaller.
- Why this approach comes to mind first: It's a straightforward solution that doesn't require any additional data structures or complex algorithms.

```cpp
vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
    int minSum = INT_MAX;
    vector<string> result;
    for (int i = 0; i < list1.size(); i++) {
        for (int j = 0; j < list2.size(); j++) {
            if (list1[i] == list2[j]) {
                int sum = i + j;
                if (sum < minSum) {
                    minSum = sum;
                    result.clear();
                    result.push_back(list1[i]);
                } else if (sum == minSum) {
                    result.push_back(list1[i]);
                }
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ and $m$ are the sizes of the input lists. This is because we have two nested loops that iterate through each list.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output. This is because we only use a constant amount of space to store the minimum index sum and the result.
> - **Why these complexities occur:** The time complexity occurs because we have to iterate through all possible pairs of restaurants. The space complexity occurs because we only need a constant amount of space to store the minimum index sum and the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a hash map to store the indices of the restaurants in the first list, and then iterate through the second list to find the restaurants with the minimum index sum.
- Detailed breakdown of the approach:
    1. Create a hash map to store the indices of the restaurants in the first list.
    2. Initialize variables to store the minimum index sum and the corresponding restaurant names.
    3. Iterate through the second list, and for each restaurant, check if it exists in the hash map.
    4. If it exists, calculate the sum of its indices in the two lists.
    5. Update the minimum index sum and the corresponding restaurant names if the current sum is smaller.
- Proof of optimality: This approach has a time complexity of $O(n + m)$, which is optimal because we have to iterate through each list at least once.

```cpp
vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
    unordered_map<string, int> map;
    for (int i = 0; i < list1.size(); i++) {
        map[list1[i]] = i;
    }
    int minSum = INT_MAX;
    vector<string> result;
    for (int i = 0; i < list2.size(); i++) {
        if (map.count(list2[i])) {
            int sum = map[list2[i]] + i;
            if (sum < minSum) {
                minSum = sum;
                result.clear();
                result.push_back(list2[i]);
            } else if (sum == minSum) {
                result.push_back(list2[i]);
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the sizes of the input lists. This is because we have to iterate through each list once.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the first list. This is because we use a hash map to store the indices of the restaurants in the first list.
> - **Optimality proof:** This approach is optimal because we have to iterate through each list at least once, and the hash map allows us to look up the indices of the restaurants in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, iteration, and optimization.
- Problem-solving patterns identified: Using hash maps to store and look up data, and iterating through lists to find the minimum or maximum value.
- Optimization techniques learned: Using hash maps to reduce the time complexity of the solution.
- Similar problems to practice: Other problems that involve finding the minimum or maximum value in a list, or using hash maps to store and look up data.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a key exists in the hash map before trying to access its value.
- Edge cases to watch for: Handling cases where a restaurant appears in both lists but with different indices, or handling cases where a restaurant appears in only one list.
- Performance pitfalls: Using a brute force approach that has a high time complexity, or using a data structure that is not optimized for the problem.
- Testing considerations: Testing the solution with different input cases, including edge cases and boundary cases.