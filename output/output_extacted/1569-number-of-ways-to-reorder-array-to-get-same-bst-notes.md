## Number of Ways to Reorder Array to Get Same BST

**Problem Link:** https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description

**Problem Statement:**
- Input format: An array of unique integers `arr`.
- Constraints: `1 <= arr.length <= 1000`, `0 <= arr[i] <= 10^6`.
- Expected output format: The number of ways to reorder `arr` to get the same binary search tree (BST) structure.
- Key requirements and edge cases to consider: All elements in `arr` must be unique, and the BST must be a valid binary search tree.
- Example test cases with explanations:
  - Example 1: `arr = [2,1,3]`, output: `1`. There is only one way to reorder the array to get the same BST structure.
  - Example 2: `arr = [3,9]`, output: `1`. There is only one way to reorder the array to get the same BST structure.
  - Example 3: `arr = [3,9,5]`, output: `2`. There are two ways to reorder the array to get the same BST structure.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible permutations of the input array and count the number of permutations that result in the same BST structure.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the input array.
  2. For each permutation, construct a BST.
  3. Compare the constructed BST with the original BST.
  4. If the two BSTs are the same, increment the count of valid permutations.
- Why this approach comes to mind first: It is a straightforward approach that involves trying all possible solutions and checking if they meet the required conditions.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int numOfWays(vector<int>& arr) {
    int n = arr.size();
    vector<int> original = arr;
    sort(original.begin(), original.end());
    int count = 0;
    
    do {
        vector<int> temp = arr;
        sort(temp.begin(), temp.end());
        
        // Check if the two BSTs are the same
        if (isSameBST(original, temp)) {
            count++;
        }
    } while (next_permutation(arr.begin(), arr.end()));
    
    return count;
}

bool isSameBST(vector<int>& arr1, vector<int>& arr2) {
    // Check if the two BSTs are the same
    if (arr1.size() != arr2.size()) {
        return false;
    }
    
    for (int i = 0; i < arr1.size(); i++) {
        if (arr1[i] != arr2[i]) {
            return false;
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n \log n)$, where $n$ is the size of the input array. The reason for this complexity is that we are generating all permutations of the input array (which takes $O(n!)$ time) and then sorting each permutation (which takes $O(n \log n)$ time).
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. The reason for this complexity is that we need to store the input array and the original BST.
> - **Why these complexities occur:** The brute force approach involves trying all possible permutations of the input array and checking if they meet the required conditions. This results in a high time complexity due to the large number of permutations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The number of ways to reorder the array to get the same BST structure is equal to the number of ways to arrange the left and right subtrees of the BST.
- Detailed breakdown of the approach:
  1. Find the root of the BST.
  2. Recursively find the roots of the left and right subtrees.
  3. Calculate the number of ways to arrange the left and right subtrees.
- Proof of optimality: This approach is optimal because it avoids trying all possible permutations of the input array and instead uses the structure of the BST to calculate the number of valid permutations.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int numOfWays(vector<int>& arr) {
    int n = arr.size();
    vector<int> original = arr;
    sort(original.begin(), original.end());
    
    return calculateWays(original);
}

int calculateWays(vector<int>& arr) {
    if (arr.size() <= 2) {
        return 1;
    }
    
    int root = arr[0];
    vector<int> left, right;
    
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] < root) {
            left.push_back(arr[i]);
        } else {
            right.push_back(arr[i]);
        }
    }
    
    int leftWays = calculateWays(left);
    int rightWays = calculateWays(right);
    
    // Calculate the number of ways to arrange the left and right subtrees
    int arrangeWays = combination(left.size() + right.size(), left.size());
    
    return leftWays * rightWays * arrangeWays;
}

int combination(int n, int k) {
    // Calculate the number of combinations of n items taken k at a time
    int result = 1;
    
    for (int i = 1; i <= k; i++) {
        result = result * (n - i + 1) / i;
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. The reason for this complexity is that we are recursively calculating the number of ways to arrange the left and right subtrees.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. The reason for this complexity is that we need to store the input array and the recursive call stack.
> - **Optimality proof:** This approach is optimal because it avoids trying all possible permutations of the input array and instead uses the structure of the BST to calculate the number of valid permutations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, dynamic programming, and combinatorics.
- Problem-solving patterns identified: Using the structure of the BST to calculate the number of valid permutations.
- Optimization techniques learned: Avoiding unnecessary computations by using the structure of the BST.
- Similar problems to practice: Problems involving combinatorics and recursion.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not using recursion correctly.
- Edge cases to watch for: Empty input array, input array with only one element.
- Performance pitfalls: Trying all possible permutations of the input array, not using the structure of the BST to calculate the number of valid permutations.
- Testing considerations: Testing the function with different input arrays, including edge cases.