## Most Frequent IDs
**Problem Link:** https://leetcode.com/problems/most-frequent-ids/description

**Problem Statement:**
- Input format: You are given a table `ids` with columns `id` and `frequency`, where `id` is the ID of an item and `frequency` is the frequency of the item.
- Constraints: The table `ids` has at least one row and at most 100 rows. Each `id` is unique, and `frequency` is a positive integer.
- Expected output format: Return the ID with the highest frequency. If there are multiple IDs with the same highest frequency, return the one with the smallest ID.
- Key requirements and edge cases to consider: Handling ties in frequency, ensuring the smallest ID is returned in case of a tie.
- Example test cases with explanations:
  - Example 1: If the table `ids` contains two rows with IDs 1 and 2 and frequencies 2 and 1 respectively, the output should be 1 because it has the highest frequency.
  - Example 2: If the table `ids` contains two rows with IDs 1 and 2 and frequencies 2 and 2 respectively, the output should be 1 because it has the smallest ID among the IDs with the highest frequency.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to sort the table `ids` in descending order based on `frequency` and then in ascending order based on `id`. This way, the first row will always have the highest frequency and the smallest ID.
- Step-by-step breakdown of the solution:
  1. Sort the table `ids` based on `frequency` in descending order and `id` in ascending order.
  2. Return the `id` of the first row.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Item {
    int id;
    int frequency;
};

bool compareItems(const Item& a, const Item& b) {
    if (a.frequency == b.frequency) {
        return a.id < b.id;
    }
    return a.frequency > b.frequency;
}

int mostFrequentId(std::vector<Item>& ids) {
    std::sort(ids.begin(), ids.end(), compareItems);
    return ids[0].id;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rows in the table `ids`. This is because we are using the `std::sort` function, which has a time complexity of $O(n \log n)$.
> - **Space Complexity:** $O(1)$, if we consider the input table `ids` as part of the output. If we don't consider the input table, the space complexity is $O(n)$ for the sorting algorithm's auxiliary space.
> - **Why these complexities occur:** The time complexity occurs because we are using the `std::sort` function, which has a time complexity of $O(n \log n)$. The space complexity occurs because the sorting algorithm uses auxiliary space to store temporary results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting the entire table, we can simply iterate through the table and keep track of the ID with the highest frequency. If we find a tie in frequency, we update the ID to the smaller one.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the ID with the highest frequency and the highest frequency itself.
  2. Iterate through the table `ids`.
  3. For each row, check if the frequency is higher than the current highest frequency. If it is, update the highest frequency and the corresponding ID.
  4. If the frequency is equal to the current highest frequency, update the ID to the smaller one.
- Proof of optimality: This approach is optimal because it only requires a single pass through the table, resulting in a time complexity of $O(n)$.

```cpp
#include <iostream>
#include <vector>

struct Item {
    int id;
    int frequency;
};

int mostFrequentId(std::vector<Item>& ids) {
    int maxFrequency = 0;
    int resultId = 0;
    for (const auto& item : ids) {
        if (item.frequency > maxFrequency) {
            maxFrequency = item.frequency;
            resultId = item.id;
        } else if (item.frequency == maxFrequency) {
            resultId = std::min(resultId, item.id);
        }
    }
    return resultId;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table `ids`. This is because we are only iterating through the table once.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the table, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and variable updates.
- Problem-solving patterns identified: Keeping track of the maximum or minimum value in a dataset.
- Optimization techniques learned: Avoiding unnecessary sorting or comparisons.
- Similar problems to practice: Finding the maximum or minimum value in a dataset, or finding the most frequent element in a dataset.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize variables, or using incorrect conditional statements.
- Edge cases to watch for: Ties in frequency, or empty datasets.
- Performance pitfalls: Using unnecessary sorting or comparisons, or using inefficient data structures.
- Testing considerations: Testing the function with different datasets, including edge cases and large datasets.