## Number of Flowers in Full Bloom
**Problem Link:** https://leetcode.com/problems/number-of-flowers-in-full-bloom/description

**Problem Statement:**
- Input format and constraints: Given a 2D array `flowers` where `flowers[i] = [plantTime, bloomTime, wiltTime]`, representing the time when the flower will be planted, bloom, and wilt. The goal is to find the maximum number of flowers that will be in full bloom at any given time.
- Expected output format: The maximum number of flowers that will be in full bloom at any given time.
- Key requirements and edge cases to consider: The flowers can be planted, bloom, and wilt at any time, and the goal is to find the maximum number of flowers that will be in full bloom at any given time. We need to consider the time complexity and space complexity of the solution.
- Example test cases with explanations: For example, if `flowers = [[1, 10, 2], [5, 11, 3], [11, 12, 2]]`, the maximum number of flowers in full bloom is 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate over each flower and check if it is in full bloom at any given time.
- Step-by-step breakdown of the solution:
  1. Sort the flowers by their plant time.
  2. Initialize a variable `max_bloom` to store the maximum number of flowers in full bloom.
  3. Iterate over each flower and check if it is in full bloom at any given time.
  4. Update `max_bloom` if the current number of flowers in full bloom is greater than `max_bloom`.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the nested loops.

```cpp
#include <vector>
#include <algorithm>

int numberOfFlowersInFullBloom(std::vector<std::vector<int>>& flowers) {
    int max_bloom = 0;
    for (int i = 0; i < flowers.size(); i++) {
        int bloom_count = 0;
        for (int j = 0; j < flowers.size(); j++) {
            if (flowers[i][1] <= flowers[j][2] && flowers[j][1] <= flowers[i][2]) {
                bloom_count++;
            }
        }
        max_bloom = std::max(max_bloom, bloom_count);
    }
    return max_bloom;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of flowers. This is because we have nested loops that iterate over each flower.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum number of flowers in full bloom.
> - **Why these complexities occur:** The nested loops cause the high time complexity, while the constant space usage results in a low space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over each flower and checking if it is in full bloom at any given time, we can use a sweep line approach to find the maximum number of flowers in full bloom.
- Detailed breakdown of the approach:
  1. Sort the flowers by their bloom time.
  2. Initialize a variable `max_bloom` to store the maximum number of flowers in full bloom.
  3. Initialize a variable `current_bloom` to store the current number of flowers in full bloom.
  4. Iterate over each flower and update `current_bloom` and `max_bloom` accordingly.
- Proof of optimality: This approach has a time complexity of $O(n \log n)$, which is optimal because we need to sort the flowers.

```cpp
#include <vector>
#include <algorithm>

int numberOfFlowersInFullBloom(std::vector<std::vector<int>>& flowers) {
    std::vector<std::pair<int, int>> events;
    for (const auto& flower : flowers) {
        events.push_back({flower[1], 1});
        events.push_back({flower[2], -1});
    }
    std::sort(events.begin(), events.end());
    int max_bloom = 0;
    int current_bloom = 0;
    for (const auto& event : events) {
        current_bloom += event.second;
        max_bloom = std::max(max_bloom, current_bloom);
    }
    return max_bloom;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of flowers. This is because we sort the events.
> - **Space Complexity:** $O(n)$, as we store the events in a vector.
> - **Optimality proof:** This approach is optimal because we need to sort the events, and the time complexity of sorting is $O(n \log n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sweep line approach, sorting.
- Problem-solving patterns identified: Using a sweep line approach to find the maximum number of flowers in full bloom.
- Optimization techniques learned: Reducing the time complexity by using a sweep line approach.
- Similar problems to practice: Problems that involve finding the maximum number of elements in a given range, such as the "Maximum Number of Flowers in Full Bloom" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the events correctly, not updating the `current_bloom` and `max_bloom` variables correctly.
- Edge cases to watch for: Flowers that bloom and wilt at the same time, flowers that have the same bloom time.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases and large inputs.