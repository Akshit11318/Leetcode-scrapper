## Sort By
**Problem Link:** https://leetcode.com/problems/sort-by/description

**Problem Statement:**
- Input format and constraints: The problem requires sorting an array of integers based on their frequency and then by their values.
- Expected output format: The sorted array.
- Key requirements and edge cases to consider: Handling duplicate elements, maintaining relative order of elements with the same frequency.
- Example test cases with explanations:
    - Input: `[1,1,2,2,3]`
      Output: `[1,1,2,2,3]`
    - Input: `[4,5,5,6]`
      Output: `[5,5,4,6]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Use a hash map to count the frequency of each number, then sort the numbers based on their frequency and value.
- Step-by-step breakdown of the solution:
    1. Count the frequency of each number using a hash map.
    2. Create a vector of pairs, where each pair contains the frequency and value of a number.
    3. Sort the vector of pairs based on the frequency and value.
    4. Create the final sorted array by iterating over the sorted vector of pairs.
- Why this approach comes to mind first: It is a straightforward solution that uses common data structures and algorithms.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> sortBy(vector<int>& nums) {
    unordered_map<int, int> freq;
    for (int num : nums) {
        freq[num]++;
    }

    vector<pair<int, int>> pairs;
    for (auto& it : freq) {
        pairs.push_back({it.second, it.first});
    }

    sort(pairs.begin(), pairs.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        if (a.first == b.first) {
            return a.second < b.second;
        }
        return a.first > b.first;
    });

    vector<int> sorted;
    for (const auto& pair : pairs) {
        for (int i = 0; i < pair.first; i++) {
            sorted.push_back(pair.second);
        }
    }

    return sorted;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of unique elements. This is because we are sorting the vector of pairs.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique elements. This is because we are storing the frequency of each number in a hash map and the vector of pairs.
> - **Why these complexities occur:** The time complexity occurs because we are sorting the vector of pairs, and the space complexity occurs because we are storing the frequency of each number and the vector of pairs.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a hash map to count the frequency of each number, then use a custom comparator to sort the numbers based on their frequency and value.
- Detailed breakdown of the approach:
    1. Count the frequency of each number using a hash map.
    2. Sort the numbers based on their frequency and value using a custom comparator.
- Proof of optimality: This solution is optimal because it uses a hash map to count the frequency of each number in $O(n)$ time, and then sorts the numbers in $O(n \log n)$ time using a custom comparator.
- Why further optimization is impossible: This solution is already optimal because it uses the most efficient data structures and algorithms available.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> sortBy(vector<int>& nums) {
    unordered_map<int, int> freq;
    for (int num : nums) {
        freq[num]++;
    }

    sort(nums.begin(), nums.end(), [&](int a, int b) {
        if (freq[a] == freq[b]) {
            return a < b;
        }
        return freq[a] > freq[b];
    });

    return nums;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements. This is because we are sorting the numbers using a custom comparator.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique elements. This is because we are storing the frequency of each number in a hash map.
> - **Optimality proof:** This solution is optimal because it uses a hash map to count the frequency of each number in $O(n)$ time, and then sorts the numbers in $O(n \log n)$ time using a custom comparator.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, custom comparators, sorting algorithms.
- Problem-solving patterns identified: Using hash maps to count frequencies, using custom comparators to sort complex data structures.
- Optimization techniques learned: Using hash maps to reduce time complexity, using custom comparators to simplify sorting logic.
- Similar problems to practice: Sorting arrays based on multiple criteria, counting frequencies of elements in arrays.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not handling duplicate elements correctly.
- Edge cases to watch for: Handling empty arrays, handling arrays with duplicate elements.
- Performance pitfalls: Using inefficient data structures or algorithms, not optimizing for time complexity.
- Testing considerations: Testing with different input sizes, testing with different edge cases.