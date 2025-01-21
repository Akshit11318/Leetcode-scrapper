## Array of Doubled Pairs

**Problem Link:** https://leetcode.com/problems/array-of-doubled-pairs/description

**Problem Statement:**
- Input format: An integer array `changed`.
- Constraints: $1 \leq n \leq 10^4$, where $n$ is the length of the array `changed`.
- Expected output format: A boolean indicating whether it is possible to construct an array of doubled pairs from the input array.
- Key requirements: Determine if we can construct an array where every element is doubled, such that each element appears twice in the array.
- Example test cases:
  - Input: `changed = [1,2]`
    Output: `false`
  - Input: `changed = [3,1,3,6]`
    Output: `false`
  - Input: `changed = [2,1,2,6]`
    Output: `false`
  - Input: `changed = [4,-2,2,-4]`
    Output: `true`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible combinations of pairs to see if we can form a valid array of doubled pairs.
- We can sort the array first, then try to form pairs by iterating through the array and checking if we can find a matching pair for each element.
- This approach comes to mind first because it directly addresses the requirement of forming pairs and checking for their existence.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool canConstruct(vector<int>& changed) {
    sort(changed.begin(), changed.end());
    for (int i = 0; i < changed.size(); i++) {
        int count = 0;
        for (int j = 0; j < changed.size(); j++) {
            if (changed[i] == changed[j]) {
                count++;
            }
            if (changed[i] * 2 == changed[j]) {
                count--;
            }
        }
        if (count > 0) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array `changed`. This is because we have two nested loops iterating over the array.
> - **Space Complexity:** $O(1)$, not including the space needed for sorting, which is $O(n)$ in the worst case for some sorting algorithms. We are only using a constant amount of space to store the count variable.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic, while the space complexity remains constant because we are not using any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight here is to use a `unordered_map` to store the frequency of each number and its double.
- We iterate through the array, and for each number, we check if its double is present in the map. If it is, we decrement the count of the double. If not, we increment the count of the current number.
- This approach ensures that we are considering all possible pairs and their doubles in a single pass through the array.
- We then check if all counts in the map are zero, indicating that all numbers have been paired with their doubles.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

bool canConstruct(vector<int>& changed) {
    unordered_map<int, int> count;
    for (int num : changed) {
        if (count.find(num * 2) != count.end() && count[num * 2] > 0) {
            count[num * 2]--;
        } else {
            count[num]++;
        }
    }
    for (auto& pair : count) {
        if (pair.second != 0) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array `changed`. This is because we are making a single pass through the array.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store every element in the `unordered_map`.
> - **Optimality proof:** This is optimal because we must at least look at each element once to determine if it can be paired with its double, and we are doing so in a single pass through the array.

---

### Final Notes

**Learning Points:**
- The importance of using the right data structure for the problem. In this case, an `unordered_map` allows us to efficiently store and retrieve the frequency of numbers and their doubles.
- The value of considering all possible pairs in a single pass through the array to minimize time complexity.
- The need to validate the counts of all numbers at the end to ensure that all numbers have been paired with their doubles.

**Mistakes to Avoid:**
- Not considering all possible pairs of numbers and their doubles.
- Not using an efficient data structure to store and retrieve the frequency of numbers.
- Not validating the counts of all numbers at the end to ensure that all numbers have been paired with their doubles.