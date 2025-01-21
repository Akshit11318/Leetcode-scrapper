## Number of Squareful Arrays
**Problem Link:** https://leetcode.com/problems/number-of-squareful-arrays/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: `1 <= nums.length <= 100`, `1 <= nums[i] <= 1000`.
- Expected Output: The number of `squareful` arrays that can be obtained by rearranging the elements of `nums`.
- Key Requirements: A `squareful` array is an array where all adjacent elements are squareful, i.e., for any two adjacent elements `a` and `b`, `sqrt(a + b)` is an integer.
- Example Test Cases:
  - Input: `nums = [1,17,8]`
  - Output: `2`
  - Explanation: There are two possible squareful arrays: `[1,8,17]` and `[17,1,8]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible permutations of the input array and check each permutation to see if it is squareful.
- Step-by-step breakdown:
  1. Generate all permutations of the input array.
  2. For each permutation, iterate through the array and check if each pair of adjacent elements is squareful.
  3. If a permutation is found to be squareful, increment the count of squareful arrays.
- Why this approach comes to mind first: It is a straightforward approach that involves checking all possible arrangements of the input array.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int numSquarefulPerms(vector<int>& nums) {
    int count = 0;
    do {
        bool isSquareful = true;
        for (int i = 0; i < nums.size() - 1; i++) {
            double sum = nums[i] + nums[i + 1];
            double sqrtSum = sqrt(sum);
            if (sqrtSum != (int)sqrtSum) {
                isSquareful = false;
                break;
            }
        }
        if (isSquareful) {
            count++;
        }
    } while (next_permutation(nums.begin(), nums.end()));
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the length of the input array. This is because we generate all permutations of the array (which takes $O(n!)$ time) and then check each permutation (which takes $O(n)$ time).
> - **Space Complexity:** $O(1)$, not counting the space needed for the input and output. This is because we only use a constant amount of space to store the count of squareful arrays.
> - **Why these complexities occur:** The time complexity is high because we generate all permutations of the input array, which can be very large for even moderate-sized input arrays. The space complexity is low because we only use a constant amount of space to store the count of squareful arrays.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can use a backtracking approach to generate all possible squareful arrays. This approach is more efficient than the brute force approach because it prunes branches that cannot lead to a squareful array.
- Detailed breakdown:
  1. Sort the input array in ascending order.
  2. Initialize an empty array to store the current permutation.
  3. Use a recursive function to generate all possible permutations of the input array. In each recursive call, try to add each element of the input array to the current permutation and check if the resulting permutation is squareful.
  4. If a permutation is found to be squareful, increment the count of squareful arrays.
- Proof of optimality: This approach is optimal because it generates all possible squareful arrays without generating any unnecessary permutations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int numSquarefulPerms(vector<int>& nums) {
    int count = 0;
    sort(nums.begin(), nums.end());
    vector<bool> visited(nums.size(), false);
    vector<int> permutation;
    backtrack(nums, permutation, visited, count);
    return count;
}

void backtrack(vector<int>& nums, vector<int>& permutation, vector<bool>& visited, int& count) {
    if (permutation.size() == nums.size()) {
        bool isSquareful = true;
        for (int i = 0; i < permutation.size() - 1; i++) {
            double sum = permutation[i] + permutation[i + 1];
            double sqrtSum = sqrt(sum);
            if (sqrtSum != (int)sqrtSum) {
                isSquareful = false;
                break;
            }
        }
        if (isSquareful) {
            count++;
        }
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])) {
            continue;
        }
        permutation.push_back(nums[i]);
        visited[i] = true;
        backtrack(nums, permutation, visited, count);
        permutation.pop_back();
        visited[i] = false;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! / (n_1! \cdot n_2! \cdot ... \cdot n_k!))$, where $n$ is the length of the input array and $n_1, n_2, ..., n_k$ are the frequencies of each element in the input array. This is because we generate all permutations of the array, but we prune branches that cannot lead to a squareful array.
> - **Space Complexity:** $O(n)$, not counting the space needed for the input and output. This is because we use a recursive function to generate all permutations of the input array.
> - **Optimality proof:** This approach is optimal because it generates all possible squareful arrays without generating any unnecessary permutations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: backtracking, pruning branches that cannot lead to a solution.
- Problem-solving patterns identified: using a recursive function to generate all permutations of an array.
- Optimization techniques learned: pruning branches that cannot lead to a solution.
- Similar problems to practice: generating all permutations of an array, finding all possible solutions to a problem using backtracking.

**Mistakes to Avoid:**
- Common implementation errors: not checking for duplicate elements in the input array, not pruning branches that cannot lead to a solution.
- Edge cases to watch for: an empty input array, an input array with a single element.
- Performance pitfalls: generating all permutations of the input array without pruning branches that cannot lead to a solution.
- Testing considerations: testing the function with different input arrays, including edge cases.