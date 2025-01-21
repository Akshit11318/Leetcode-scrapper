## Queue Reconstruction by Height

**Problem Link:** https://leetcode.com/problems/queue-reconstruction-by-height/description

**Problem Statement:**
- Input format: A 2D array `people` where `people[i] = [h_i, k_i]`, representing the height `h_i` and the number of people `k_i` in front of this person who have a height greater than or equal to `h_i`.
- Constraints: `1 <= people.length <= 1000`, `0 <= h_i <= 10^6`, `0 <= k_i < people.length`.
- Expected output format: A 2D array representing the reconstructed queue.
- Key requirements and edge cases to consider: 
    - The input array `people` is not guaranteed to be sorted.
    - The height `h_i` can be the same for different people, in which case the order is determined by `k_i`.
    - The number of people `k_i` in front of a person with a certain height is not necessarily consecutive.
- Example test cases with explanations:
    - `people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]`: The reconstructed queue should be `[[5,0],[7,0],[5,2],[6,1],[7,1],[4,4]]`.
    - `people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]`: The reconstructed queue should be `[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]`.

### Brute Force Approach

**Explanation:**
- The brute force approach involves trying all possible permutations of the `people` array and checking if the permutation satisfies the given conditions.
- We can use a recursive function to generate all permutations and a helper function to check if a permutation is valid.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> reconstructQueue(std::vector<std::vector<int>>& people) {
        std::sort(people.begin(), people.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            if (a[0] == b[0]) {
                return a[1] < b[1];
            }
            return a[0] > b[0];
        });
        
        std::vector<std::vector<int>> result;
        for (const auto& person : people) {
            result.insert(result.begin() + person[1], person);
        }
        return result;
    }
};
```

However, this brute force approach is not efficient and is not suitable for large inputs.

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ due to the generation of all permutations, where $n$ is the number of people.
> - **Space Complexity:** $O(n)$ for storing the permutations.
> - **Why these complexities occur:** The brute force approach tries all possible permutations, resulting in an exponential time complexity.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves sorting the `people` array in descending order of height and then in ascending order of the number of people in front of each person.
- We then iterate through the sorted array and insert each person at the position specified by the number of people in front of them.
- This approach ensures that the reconstructed queue satisfies the given conditions.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> reconstructQueue(std::vector<std::vector<int>>& people) {
        std::sort(people.begin(), people.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            if (a[0] == b[0]) {
                return a[1] < b[1];
            }
            return a[0] > b[0];
        });
        
        std::vector<std::vector<int>> result;
        for (const auto& person : people) {
            result.insert(result.begin() + person[1], person);
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ due to the insertion of people at specific positions, where $n$ is the number of people.
> - **Space Complexity:** $O(n)$ for storing the reconstructed queue.
> - **Optimality proof:** This approach is optimal because it ensures that the reconstructed queue satisfies the given conditions and has a time complexity that is quadratic in the number of people.

### Final Notes

**Learning Points:**
- The importance of sorting and ordering in solving problems involving relative positions or priorities.
- The use of custom comparators to sort arrays based on multiple criteria.
- The technique of inserting elements at specific positions in a vector.

**Mistakes to Avoid:**
- Assuming that the input array is already sorted or ordered.
- Failing to consider edge cases, such as people with the same height or people with no one in front of them.
- Using inefficient algorithms, such as generating all permutations, to solve the problem.