## Maximum Height by Stacking Cuboids
**Problem Link:** https://leetcode.com/problems/maximum-height-by-stacking-cuboids/description

**Problem Statement:**
- Input format and constraints: Given a list of `n` cuboids, where each cuboid `i` is represented as an array of three integers `[a, b, c]`, representing the dimensions of the cuboid.
- Expected output format: The maximum height that can be achieved by stacking the cuboids.
- Key requirements and edge cases to consider: 
    - The cuboids can be rotated to any orientation.
    - A cuboid can be placed on top of another cuboid if the top face of the lower cuboid is a rectangle that is at least as large as the bottom face of the upper cuboid.
- Example test cases with explanations: 
    - For example, given `cuboids = [[50,45,20],[95,37,53],[45,23,12]]`, the maximum height is `190`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the maximum height, we can try all possible rotations and orderings of the cuboids.
- Step-by-step breakdown of the solution:
    1. Generate all possible rotations for each cuboid.
    2. For each rotation of each cuboid, try placing it on top of every other cuboid.
    3. For each configuration, calculate the total height.
- Why this approach comes to mind first: It seems straightforward to consider all possibilities, but this approach quickly becomes impractical due to its high computational complexity.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int maxHeight(vector<vector<int>>& cuboids) {
    int n = cuboids.size();
    vector<vector<int>> rotations;
    
    // Generate all possible rotations for each cuboid
    for (auto& cuboid : cuboids) {
        vector<int> dims = {cuboid[0], cuboid[1], cuboid[2]};
        sort(dims.begin(), dims.end());
        rotations.push_back(dims);
    }
    
    int max_height = 0;
    
    // Try all possible orderings and rotations
    do {
        int height = 0;
        vector<vector<int>> current_cuboids = rotations;
        
        // Try placing each cuboid on top of the previous one
        for (int i = 0; i < n; i++) {
            vector<int> top = current_cuboids[i];
            bool placed = false;
            
            for (int j = 0; j < i; j++) {
                vector<int> bottom = current_cuboids[j];
                if (bottom[0] >= top[0] && bottom[1] >= top[1]) {
                    height += top[2];
                    placed = true;
                    break;
                }
            }
            
            if (!placed) {
                height += top[2];
            }
        }
        
        max_height = max(max_height, height);
    } while (next_permutation(rotations.begin(), rotations.end()));
    
    return max_height;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot 3^n)$, where $n$ is the number of cuboids, due to generating all permutations and rotations.
> - **Space Complexity:** $O(n)$, for storing the current configuration of cuboids.
> - **Why these complexities occur:** The brute force approach tries all possible orderings and rotations of the cuboids, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the maximum height that can be achieved with each cuboid as the base.
- Detailed breakdown of the approach:
    1. Sort the cuboids by their base area in descending order.
    2. For each cuboid, try placing it on top of every previous cuboid.
    3. Update the maximum height that can be achieved with each cuboid as the base.
- Proof of optimality: This approach ensures that we consider all possible configurations of cuboids, while avoiding redundant calculations.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int maxHeight(vector<vector<int>>& cuboids) {
    int n = cuboids.size();
    
    // Sort the cuboids by their base area in descending order
    for (auto& cuboid : cuboids) {
        sort(cuboid.begin(), cuboid.end());
    }
    
    sort(cuboids.begin(), cuboids.end(), [](vector<int>& a, vector<int>& b) {
        return a[0] * a[1] > b[0] * b[1];
    });
    
    vector<int> heights(n, 0);
    
    // Try placing each cuboid on top of every previous cuboid
    for (int i = 0; i < n; i++) {
        heights[i] = cuboids[i][2];
        
        for (int j = 0; j < i; j++) {
            if (cuboids[j][0] >= cuboids[i][0] && cuboids[j][1] >= cuboids[i][1]) {
                heights[i] = max(heights[i], heights[j] + cuboids[i][2]);
            }
        }
    }
    
    return *max_element(heights.begin(), heights.end());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of cuboids, due to the nested loops.
> - **Space Complexity:** $O(n)$, for storing the maximum heights.
> - **Optimality proof:** This approach ensures that we consider all possible configurations of cuboids, while avoiding redundant calculations, resulting in optimal time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, sorting, and permutation.
- Problem-solving patterns identified: breaking down complex problems into smaller sub-problems, using memoization to avoid redundant calculations.
- Optimization techniques learned: reducing the search space by sorting and pruning.
- Similar problems to practice: other dynamic programming problems, such as the `0/1 Knapsack Problem` and `Longest Common Subsequence`.

**Mistakes to Avoid:**
- Common implementation errors: incorrect indexing, missing base cases, and incorrect pruning.
- Edge cases to watch for: empty input, duplicate cuboids, and cuboids with zero height.
- Performance pitfalls: using inefficient data structures, such as linked lists, and not optimizing the search space.
- Testing considerations: testing with large inputs, testing with edge cases, and testing with random inputs.