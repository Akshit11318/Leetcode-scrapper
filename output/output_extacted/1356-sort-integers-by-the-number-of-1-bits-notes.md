## Sort Integers by The Number of 1 Bits
**Problem Link:** https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description

**Problem Statement:**
- Input format: An array of integers `arr` with a length of `n`.
- Constraints: `1 <= n <= 100`, `0 <= arr[i] <= 10^4`.
- Expected output format: A sorted array of integers based on the number of 1 bits in their binary representation.
- Key requirements: Sort the array such that for any two elements `x` and `y`, if the number of 1 bits in `x` is less than the number of 1 bits in `y`, then `x` comes before `y`. If the number of 1 bits is the same, then the smaller number comes first.
- Example test cases: 
  - Input: `arr = [0,1,2,3,4,5,6,7,8]`
  - Output: `[0,1,2,4,8,3,5,6,7]`
  - Explanation: The number of 1 bits in the binary representation of each number is `[0,1,1,2,1,2,2,3,1]`. Sorting based on this gives the output.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to calculate the number of 1 bits for each number in the array and then sort the array based on this count and the value itself.
- Step-by-step breakdown:
  1. Calculate the number of 1 bits for each number in the array.
  2. Create pairs of the number and its 1 bit count.
  3. Sort these pairs based on the 1 bit count and then the number itself.
  4. Extract the sorted numbers from the pairs.

```cpp
#include <vector>
#include <algorithm>

int countOneBits(int num) {
    int count = 0;
    while (num) {
        count += num & 1;
        num >>= 1;
    }
    return count;
}

std::vector<int> sortByBits(std::vector<int>& arr) {
    std::vector<std::pair<int, int>> pairs;
    for (int num : arr) {
        pairs.push_back({num, countOneBits(num)});
    }
    std::sort(pairs.begin(), pairs.end(), [](const auto& a, const auto& b) {
        if (a.second == b.second) return a.first < b.first;
        return a.second < b.second;
    });
    std::vector<int> result;
    for (auto& pair : pairs) {
        result.push_back(pair.first);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + n \cdot b)$, where $n$ is the number of elements in the array and $b$ is the average number of bits in each number. The sorting operation takes $O(n \log n)$, and calculating the number of 1 bits for each number takes $O(n \cdot b)$.
> - **Space Complexity:** $O(n)$, for storing the pairs of numbers and their 1 bit counts.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation and the calculation of 1 bits for each number. The space complexity is due to the additional space needed to store the pairs.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a custom comparator in the sorting algorithm that compares the number of 1 bits in each number and then the number itself.
- Detailed breakdown:
  1. Define a custom comparator function that takes two numbers, calculates their 1 bit counts, and compares them.
  2. Use this comparator in the `std::sort` algorithm to sort the array directly.

```cpp
#include <vector>
#include <algorithm>

int countOneBits(int num) {
    int count = 0;
    while (num) {
        count += num & 1;
        num >>= 1;
    }
    return count;
}

std::vector<int> sortByBits(std::vector<int>& arr) {
    std::sort(arr.begin(), arr.end(), [](int a, int b) {
        int countA = countOneBits(a);
        int countB = countOneBits(b);
        if (countA == countB) return a < b;
        return countA < countB;
    });
    return arr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n \cdot b)$, where $n$ is the number of elements and $b$ is the average number of bits in each number. The sorting operation with the custom comparator takes this time.
> - **Space Complexity:** $O(1)$, since the sorting is done in-place and no additional space is needed that scales with input size.
> - **Optimality proof:** This is optimal because it minimizes the number of operations needed to sort the array based on the number of 1 bits in each number and then the number itself, leveraging the efficiency of the standard sorting algorithm.

---

### Final Notes

**Learning Points:**
- Custom comparators can be used to sort arrays based on complex criteria.
- Understanding the time and space complexity of algorithms is crucial for optimizing performance.
- The `std::sort` algorithm in C++ is highly efficient and can be used with custom comparators for complex sorting tasks.

**Mistakes to Avoid:**
- Not considering the time complexity of calculating the number of 1 bits for each number in the array.
- Not using a custom comparator to simplify the sorting process.
- Not considering the space complexity and the implications of creating additional data structures.