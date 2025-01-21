## Minimize the Maximum Adjacent Element Difference

**Problem Link:** https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: The input array will have at least two elements and at most $10^5$ elements, with each element being an integer in the range $[0, 10^5]$.
- Expected Output: The minimum maximum difference between any two adjacent elements that can be achieved by rearranging the elements in the array.
- Key Requirements: The goal is to minimize the maximum difference between adjacent elements, and we can rearrange the elements in any order to achieve this.
- Edge Cases: Consider arrays with duplicate elements or arrays where the maximum element is significantly larger than the rest.

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible permutations of the array to find the arrangement that minimizes the maximum adjacent difference.
- Step-by-step breakdown:
  1. Generate all permutations of the input array.
  2. For each permutation, calculate the maximum difference between any two adjacent elements.
  3. Keep track of the minimum maximum difference found across all permutations.

```cpp
#include <algorithm>
#include <vector>

using namespace std;

int minMaxDiff(vector<int>& nums) {
    int n = nums.size();
    int minMaxDiff = INT_MAX;
    // Generate all permutations
    do {
        int maxDiff = 0;
        for (int i = 0; i < n - 1; i++) {
            maxDiff = max(maxDiff, abs(nums[i] - nums[i + 1]));
        }
        minMaxDiff = min(minMaxDiff, maxDiff);
    } while (next_permutation(nums.begin(), nums.end()));
    return minMaxDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the number of elements in the array. The reason is that generating all permutations takes $O(n!)$ time, and for each permutation, we calculate the maximum difference in $O(n)$ time.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, since we only use a constant amount of space to store the minimum maximum difference.
> - **Why these complexities occur:** The brute force approach involves generating all permutations, which inherently leads to exponential time complexity due to the nature of permutations.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing that the problem can be solved by sorting the array and then distributing the elements in a way that minimizes the maximum adjacent difference.
- Detailed breakdown of the approach:
  1. Sort the input array in ascending order.
  2. Initialize two pointers, one at the beginning and one at the end of the sorted array.
  3. Create a new array where we alternately pick elements from the beginning and end of the sorted array, moving the pointers accordingly.
- Proof of optimality: This approach ensures that the maximum difference between any two adjacent elements is minimized because it distributes the largest and smallest elements in a way that they are never adjacent, thus minimizing the maximum gap.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int minimumAdjacentDifference(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<int> result(n);
    int left = 0, right = n - 1;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            result[i] = nums[left++];
        } else {
            result[i] = nums[right--];
        }
    }
    int maxDiff = 0;
    for (int i = 0; i < n - 1; i++) {
        maxDiff = max(maxDiff, abs(result[i] - result[i + 1]));
    }
    return maxDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the array. This is because sorting the array takes $O(n \log n)$ time, and the subsequent steps take linear time.
> - **Space Complexity:** $O(n)$, for storing the result array.
> - **Optimality proof:** This approach is optimal because it minimizes the maximum adjacent difference by distributing the elements in a way that ensures the smallest possible gaps between adjacent elements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, array manipulation, and optimization techniques.
- Problem-solving patterns identified: Recognizing the need to distribute elements to minimize gaps.
- Optimization techniques learned: Using sorting to facilitate the optimization of the maximum adjacent difference.

**Mistakes to Avoid:**
- Not considering the exponential time complexity of generating all permutations.
- Not recognizing the importance of sorting in simplifying the problem.
- Not optimizing the distribution of elements to minimize the maximum adjacent difference.

---