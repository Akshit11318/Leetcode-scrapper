## Sort Integers by The Power Value
**Problem Link:** https://leetcode.com/problems/sort-integers-by-the-power-value/description

**Problem Statement:**
- Input format and constraints: Given an integer array `arr`, the task is to sort the integers in ascending order based on the number of set bits in their binary representation. If two integers have the same number of set bits, the smaller integer comes first.
- Expected output format: The function should return the sorted array `arr`.
- Key requirements and edge cases to consider: 
  - The input array `arr` contains only non-negative integers.
  - The length of `arr` can vary, and it may contain duplicate integers.
  - The function should be efficient in terms of time and space complexity.
- Example test cases with explanations:
  - For the input `arr = [0,1,2,3,4,5,6,7,8]`, the output should be `[0,1,2,4,8,3,5,6,7]`.
  - For the input `arr = [9,4,2,7,3]`, the output should be `[2,3,4,7,9]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to calculate the number of set bits for each integer in the array and then sort the array based on this count.
- Step-by-step breakdown of the solution:
  1. Iterate over each integer in the array and calculate its binary representation.
  2. Count the number of set bits (1's) in the binary representation.
  3. Store the count of set bits along with the corresponding integer in a new data structure (e.g., a vector of pairs).
  4. Sort the new data structure based on the count of set bits and then by the integer value itself.
  5. Extract the sorted integers from the data structure and return them as the result.
- Why this approach comes to mind first: It directly addresses the problem statement by calculating the set bits for each integer and sorting based on that count.

```cpp
#include <vector>
#include <algorithm>

int countSetBits(int n) {
    int count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
    return count;
}

std::vector<int> sortByBits(std::vector<int>& arr) {
    std::vector<std::pair<int, int>> countAndNum;
    for (int num : arr) {
        countAndNum.push_back({countSetBits(num), num});
    }
    std::sort(countAndNum.begin(), countAndNum.end());
    std::vector<int> result;
    for (auto& pair : countAndNum) {
        result.push_back(pair.second);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + n \cdot b)$, where $n$ is the number of elements in the array and $b$ is the average number of bits in the binary representation of the integers. The $n \log n$ term comes from sorting, and the $n \cdot b$ term comes from counting set bits for each integer.
> - **Space Complexity:** $O(n)$, for storing the count of set bits and the corresponding integers in a new data structure.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation and the calculation of set bits for each integer. The space complexity is due to the additional data structure needed to store the counts and integers before sorting.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using a separate data structure to store the counts and integers, we can use a custom comparator in the sorting function that directly compares the number of set bits for two integers. If the counts are equal, it compares the integers themselves.
- Detailed breakdown of the approach:
  1. Define a custom comparator function that takes two integers as input.
  2. Within the comparator, calculate the number of set bits for each integer using a bit manipulation technique.
  3. Compare the counts of set bits; if they are equal, compare the integers themselves.
  4. Use this custom comparator in the sorting algorithm.
- Proof of optimality: This approach is optimal because it avoids the need for an additional data structure, reducing space complexity, and it directly sorts the array based on the required criteria without unnecessary intermediate steps.
- Why further optimization is impossible: The time complexity is dominated by the sorting operation, which is $O(n \log n)$ in the best case for comparison-based sorting algorithms. The bit manipulation to count set bits is $O(b)$, but since $b$ is typically much smaller than $n$ and is a constant for a given system, it does not affect the overall time complexity.

```cpp
#include <vector>
#include <algorithm>

int countSetBits(int n) {
    int count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
    return count;
}

bool customComparator(int a, int b) {
    int countA = countSetBits(a);
    int countB = countSetBits(b);
    if (countA == countB) {
        return a < b;
    }
    return countA < countB;
}

std::vector<int> sortByBits(std::vector<int>& arr) {
    std::sort(arr.begin(), arr.end(), customComparator);
    return arr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n \cdot b)$, where $n$ is the number of elements in the array and $b$ is the average number of bits in the binary representation of the integers. The $n \log n$ term comes from sorting, and the $b$ term comes from counting set bits within the comparator.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, because the sorting is done in-place and no additional data structures are used that scale with input size.
> - **Optimality proof:** The time complexity is optimal for a comparison-based sorting algorithm, and the space complexity is optimal because the sorting is done in-place.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Custom comparators in sorting, bit manipulation to count set bits.
- Problem-solving patterns identified: Using custom comparators to simplify sorting based on complex criteria.
- Optimization techniques learned: Avoiding unnecessary data structures, using in-place sorting.
- Similar problems to practice: Other problems involving custom sorting criteria, bit manipulation.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as when the input array is empty or contains only one element.
- Edge cases to watch for: Arrays with duplicate integers, arrays with integers that have the same number of set bits.
- Performance pitfalls: Using inefficient algorithms for counting set bits or sorting.
- Testing considerations: Thoroughly testing the function with various input scenarios, including edge cases.