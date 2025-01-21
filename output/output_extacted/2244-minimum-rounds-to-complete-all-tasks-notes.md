## Minimum Rounds to Complete All Tasks

**Problem Link:** https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description

**Problem Statement:**
- Input format and constraints: You are given an array of integers `tasks` representing the tasks to be completed. Each task is represented by its difficulty level. The task is to determine the minimum number of rounds required to complete all tasks, given that in each round, you can complete either one task of the highest difficulty or all tasks of the lowest difficulty.
- Expected output format: The minimum number of rounds required to complete all tasks.
- Key requirements and edge cases to consider: The tasks array can be empty, or all tasks can have the same difficulty level. The difficulty levels are distinct integers.
- Example test cases with explanations: 
    - Input: `tasks = [2,2,3,3,2,4,4,4,4,4]`
    - Output: `4`
    - Explanation: In the first round, we can complete all tasks of difficulty 2. In the second round, we can complete all tasks of difficulty 3. In the third round, we can complete one task of difficulty 4. In the fourth round, we can complete the remaining tasks of difficulty 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of tasks to be completed in each round.
- Step-by-step breakdown of the solution: 
    1. Sort the tasks array in ascending order of difficulty levels.
    2. Initialize a variable `rounds` to 0.
    3. Iterate over the sorted tasks array.
    4. For each task, try to complete it in the current round or start a new round.
    5. Update the `rounds` variable accordingly.
- Why this approach comes to mind first: It's a straightforward approach that tries all possible combinations, but it's not efficient for large inputs.

```cpp
#include <vector>
#include <algorithm>

int minimumRounds(std::vector<int>& tasks) {
    // Sort the tasks array in ascending order of difficulty levels
    std::sort(tasks.begin(), tasks.end());

    int rounds = 0;
    int i = 0;
    while (i < tasks.size()) {
        // Try to complete all tasks of the same difficulty level
        int count = 1;
        while (i + 1 < tasks.size() && tasks[i] == tasks[i + 1]) {
            i++;
            count++;
        }
        // If there are more than 2 tasks of the same difficulty level, 
        // we can complete all but one of them in the current round
        if (count > 2) {
            rounds += (count - 1) / 3 + 1;
        } else if (count == 2) {
            // If there are exactly 2 tasks of the same difficulty level, 
            // we need one round to complete them
            rounds++;
        } else {
            // If there is only one task of a difficulty level, 
            // we need one round to complete it
            rounds++;
        }
        i++;
    }
    return rounds;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of tasks. The sorting operation takes $O(n \log n)$ time, and the subsequent while loop takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `rounds` variable and the loop indices.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, which is necessary to group tasks of the same difficulty level together. The space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `unordered_map` to count the frequency of each difficulty level, and then calculate the minimum number of rounds required based on the frequency counts.
- Detailed breakdown of the approach: 
    1. Create an `unordered_map` to store the frequency of each difficulty level.
    2. Iterate over the tasks array and update the frequency counts in the `unordered_map`.
    3. Iterate over the `unordered_map` and calculate the minimum number of rounds required for each difficulty level.
    4. Sum up the minimum number of rounds required for all difficulty levels.
- Proof of optimality: This approach is optimal because it only requires a single pass over the tasks array to count the frequency of each difficulty level, and then a single pass over the `unordered_map` to calculate the minimum number of rounds required.

```cpp
#include <vector>
#include <unordered_map>

int minimumRounds(std::vector<int>& tasks) {
    // Create an unordered_map to store the frequency of each difficulty level
    std::unordered_map<int, int> frequency;
    for (int task : tasks) {
        frequency[task]++;
    }

    int rounds = 0;
    for (auto& pair : frequency) {
        int count = pair.second;
        // If there are more than 2 tasks of the same difficulty level, 
        // we can complete all but one of them in the current round
        if (count > 2) {
            rounds += (count - 1) / 3 + 1;
        } else if (count == 2) {
            // If there are exactly 2 tasks of the same difficulty level, 
            // we need one round to complete them
            rounds++;
        } else {
            // If there is only one task of a difficulty level, 
            // we cannot complete it, so return -1
            return -1;
        }
    }
    return rounds;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of tasks. The iteration over the tasks array takes $O(n)$ time, and the iteration over the `unordered_map` takes $O(m)$ time, where $m$ is the number of distinct difficulty levels. Since $m \leq n$, the overall time complexity is $O(n)$.
> - **Space Complexity:** $O(m)$, where $m$ is the number of distinct difficulty levels. The `unordered_map` requires $O(m)$ space to store the frequency counts.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the tasks array to count the frequency of each difficulty level, and then a single pass over the `unordered_map` to calculate the minimum number of rounds required. The use of an `unordered_map` allows us to avoid sorting the tasks array, which reduces the time complexity from $O(n \log n)$ to $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
    - **Hashing**: The use of an `unordered_map` to count the frequency of each difficulty level.
    - **Greedy Algorithm**: The approach of calculating the minimum number of rounds required based on the frequency counts.
- Problem-solving patterns identified: 
    - **Frequency Counting**: The use of a data structure to count the frequency of each element in an array.
    - **Minimum Rounds Calculation**: The approach of calculating the minimum number of rounds required based on the frequency counts.
- Optimization techniques learned: 
    - **Avoiding Sorting**: The use of an `unordered_map` to avoid sorting the tasks array.
    - **Single Pass**: The approach of making a single pass over the tasks array to count the frequency of each difficulty level.

**Mistakes to Avoid:**
- Common implementation errors: 
    - **Not handling edge cases**: Not checking for empty input or input with a single task.
    - **Not using efficient data structures**: Not using an `unordered_map` to count the frequency of each difficulty level.
- Edge cases to watch for: 
    - **Empty input**: The tasks array is empty.
    - **Single task**: The tasks array contains only one task.
- Performance pitfalls: 
    - **Sorting the tasks array**: Sorting the tasks array can increase the time complexity from $O(n)$ to $O(n \log n)$.
- Testing considerations: 
    - **Test with empty input**: Test the function with an empty tasks array.
    - **Test with single task**: Test the function with a tasks array containing only one task.