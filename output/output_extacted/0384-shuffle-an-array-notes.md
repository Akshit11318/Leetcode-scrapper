## Fisher-Yates Shuffle Algorithm Implementation
**Problem Link:** https://leetcode.com/problems/shuffle-an-array/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `n` representing the number of elements in the array.
- Constraints: The array contains `n` elements and each element is unique.
- Expected Output: A shuffled version of the input array.
- Key Requirements: Implement the `Solution` class with methods `shuffle` and `reset`.
- Edge Cases: Handle cases where the input array is empty or contains only one element.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to simply randomize the order of elements in the array.
- However, a brute force approach would involve generating all possible permutations of the array and then randomly selecting one of them.
- This approach comes to mind first because it directly addresses the requirement of shuffling the array.

```cpp
class Solution {
public:
    vector<int> nums;
    Solution(vector<int>& nums) {
        this->nums = nums;
    }
    
    vector<int> reset() {
        return nums;
    }
    
    vector<int> shuffle() {
        vector<int> shuffled = nums;
        random_shuffle(shuffled.begin(), shuffled.end());
        return shuffled;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. The `random_shuffle` function has a linear time complexity.
> - **Space Complexity:** $O(n)$, because we are creating a copy of the input array.
> - **Why these complexities occur:** The time complexity is linear because we are iterating over the entire array to shuffle its elements. The space complexity is also linear because we are creating a copy of the input array.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use the Fisher-Yates shuffle algorithm, which is an unbiased shuffling algorithm.
- This algorithm works by iterating over the array from the last element to the first, and for each element, it swaps it with a randomly chosen element from the unshuffled part of the array.
- This approach ensures that all permutations are equally likely, making it an unbiased shuffling algorithm.

```cpp
class Solution {
public:
    vector<int> nums;
    Solution(vector<int>& nums) {
        this->nums = nums;
    }
    
    vector<int> reset() {
        return nums;
    }
    
    vector<int> shuffle() {
        vector<int> shuffled = nums;
        for (int i = shuffled.size() - 1; i > 0; i--) {
            int j = rand() % (i + 1);
            swap(shuffled[i], shuffled[j]);
        }
        return shuffled;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. The Fisher-Yates shuffle algorithm has a linear time complexity.
> - **Space Complexity:** $O(n)$, because we are creating a copy of the input array.
> - **Optimality proof:** The Fisher-Yates shuffle algorithm is optimal because it has a linear time complexity and it is an unbiased shuffling algorithm, meaning that all permutations are equally likely.

---

### Final Notes

**Learning Points:**
- The Fisher-Yates shuffle algorithm is an unbiased shuffling algorithm that ensures all permutations are equally likely.
- This algorithm has a linear time complexity, making it efficient for large inputs.
- The `random_shuffle` function in C++ is not an unbiased shuffling algorithm and should be avoided in favor of the Fisher-Yates shuffle algorithm.

**Mistakes to Avoid:**
- Using the `random_shuffle` function, which is not an unbiased shuffling algorithm.
- Not creating a copy of the input array, which can modify the original array.
- Not using the Fisher-Yates shuffle algorithm, which is the optimal shuffling algorithm.