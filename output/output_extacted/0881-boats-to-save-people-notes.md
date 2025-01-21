## Boats to Save People

**Problem Link:** https://leetcode.com/problems/boats-to-save-people/description

**Problem Statement:**
- Input format and constraints: The problem takes two inputs: a vector of integers `people` representing the weights of people and an integer `limit` representing the maximum weight a boat can hold. The goal is to return the minimum number of boats required to save all people.
- Expected output format: The function should return an integer representing the minimum number of boats required.
- Key requirements and edge cases to consider: The weights of people are non-negative integers, and the maximum weight a boat can hold is a positive integer. The function should handle edge cases such as an empty input vector or a limit of 0.
- Example test cases with explanations:
  - Input: `people = [1,2], limit = 3`, Output: `1` (One boat can hold both people)
  - Input: `people = [3,2,2,1], limit = 3`, Output: `3` (One boat for the person with weight 3, one boat for the person with weight 2 and the person with weight 1, and one boat for the last person with weight 2)
  - Input: `people = [3,5,3,4], limit = 5`, Output: `4` (One boat for each person)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of people and boats to find the minimum number of boats required.
- Step-by-step breakdown of the solution:
  1. Sort the people in descending order of their weights.
  2. Iterate over all possible combinations of people and boats.
  3. For each combination, check if the total weight of the people in the boat exceeds the limit.
  4. If it does, try a different combination.
  5. Keep track of the minimum number of boats required.
- Why this approach comes to mind first: The brute force approach is often the most straightforward solution, but it can be inefficient for large inputs.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    sort(people.begin(), people.end());
    int boats = 0;
    int i = 0, j = people.size() - 1;
    while (i <= j) {
        if (people[i] + people[j] <= limit) {
            i++;
        }
        j--;
        boats++;
    }
    return boats;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of people. This is because we sort the people in descending order of their weights.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the number of boats and the indices.
> - **Why these complexities occur:** The time complexity occurs because we sort the people, and the space complexity occurs because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a two-pointer technique to find the minimum number of boats required. We start by sorting the people in ascending order of their weights. Then, we use two pointers, one at the beginning of the array and one at the end, to try to put the heaviest person and the lightest person in the same boat.
- Detailed breakdown of the approach:
  1. Sort the people in ascending order of their weights.
  2. Initialize two pointers, one at the beginning of the array and one at the end.
  3. While the pointers have not crossed each other, try to put the heaviest person and the lightest person in the same boat.
  4. If the total weight of the two people exceeds the limit, move the pointer at the end towards the beginning.
  5. Otherwise, move both pointers.
- Proof of optimality: This approach is optimal because it ensures that we use the minimum number of boats required to save all people. By trying to put the heaviest person and the lightest person in the same boat, we minimize the number of boats required.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int numRescueBoats(vector<int>& people, int limit) {
    sort(people.rbegin(), people.rend());
    int boats = 0;
    int i = 0, j = people.size() - 1;
    while (i <= j) {
        if (people[i] + people[j] <= limit) {
            j--;
        }
        i++;
        boats++;
    }
    return boats;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of people. This is because we sort the people in descending order of their weights.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the number of boats and the indices.
> - **Optimality proof:** The time complexity occurs because we sort the people, and the space complexity occurs because we only use a constant amount of space. This approach is optimal because it ensures that we use the minimum number of boats required to save all people.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, sorting.
- Problem-solving patterns identified: Using a two-pointer technique to find the minimum number of boats required.
- Optimization techniques learned: Sorting the people in ascending order of their weights to minimize the number of boats required.
- Similar problems to practice: Other problems that involve using a two-pointer technique to find the minimum or maximum of something.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the total weight of the two people exceeds the limit before moving the pointers.
- Edge cases to watch for: Handling the case where the input vector is empty or the limit is 0.
- Performance pitfalls: Not using a two-pointer technique to find the minimum number of boats required, which can lead to inefficient solutions.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it works correctly.