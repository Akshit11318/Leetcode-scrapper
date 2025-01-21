## Find Array Given Subset Sums

**Problem Link:** https://leetcode.com/problems/find-array-given-subset-sums/description

**Problem Statement:**
- Input: A list of unique integers representing subset sums and an integer target sum.
- Constraints: The length of the subset sums list is between 1 and 20, and each subset sum is between 1 and 10^6.
- Expected Output: The original array of integers that sum up to the target sum.
- Key Requirements: The array should contain only positive integers, and the sum of any subset of the array should match one of the given subset sums.

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of positive integers to form an array and check if the sum of any subset of the array matches the given subset sums.
- This approach involves generating all possible arrays of varying lengths, calculating the sum of all subsets of each array, and checking for a match with the given subset sums.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

void generateArrays(int maxLength, std::vector<int>& subsetSums, int targetSum) {
    for (int length = 1; length <= maxLength; ++length) {
        std::vector<int> array(length);
        generateArray(array, 0, subsetSums, targetSum);
    }
}

void generateArray(std::vector<int>& array, int index, std::vector<int>& subsetSums, int targetSum) {
    if (index == array.size()) {
        std::vector<int> subsetSumList;
        generateSubsetSums(array, subsetSumList);
        if (isMatch(subsetSumList, subsetSums)) {
            printArray(array);
            return;
        }
    } else {
        for (int i = 1; i <= targetSum; ++i) {
            array[index] = i;
            generateArray(array, index + 1, subsetSums, targetSum - i);
        }
    }
}

void generateSubsetSums(const std::vector<int>& array, std::vector<int>& subsetSumList) {
    int n = array.size();
    for (int mask = 0; mask < (1 << n); ++mask) {
        int subsetSum = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                subsetSum += array[i];
            }
        }
        subsetSumList.push_back(subsetSum);
    }
    std::sort(subsetSumList.begin(), subsetSumList.end());
}

bool isMatch(const std::vector<int>& subsetSumList, const std::vector<int>& subsetSums) {
    if (subsetSumList.size() != subsetSums.size()) {
        return false;
    }
    for (int i = 0; i < subsetSumList.size(); ++i) {
        if (subsetSumList[i] != subsetSums[i]) {
            return false;
        }
    }
    return true;
}

void printArray(const std::vector<int>& array) {
    for (int num : array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m \log m)$, where $n$ is the length of the subset sums list and $m$ is the maximum subset sum. The $2^n$ factor comes from generating all subsets of the array, $n$ is the length of the array, and $m \log m$ is the time complexity of sorting the subset sums.
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the subset sums list. The space complexity comes from storing all subsets of the array.
> - **Why these complexities occur:** The brute force approach involves generating all possible arrays and calculating the sum of all subsets of each array, resulting in exponential time and space complexity.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a bitmask to represent the subsets of the array and iterate through all possible bitmasks to generate the subset sums.
- This approach avoids the need to generate all possible arrays and calculates the subset sums directly using the bitmask.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

void findArray(std::vector<int>& subsetSums, int targetSum) {
    int n = subsetSums.size();
    std::vector<int> array;
    for (int mask = 1; mask < (1 << n); ++mask) {
        int subsetSum = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                subsetSum += subsetSums[i];
            }
        }
        if (subsetSum <= targetSum) {
            array.push_back(subsetSum);
            targetSum -= subsetSum;
        }
    }
    if (targetSum > 0) {
        array.push_back(targetSum);
    }
    printArray(array);
}

void printArray(const std::vector<int>& array) {
    for (int num : array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the subset sums list. The $2^n$ factor comes from iterating through all possible bitmasks, and $n$ is the length of the subset sums list.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the subset sums list. The space complexity comes from storing the array.
> - **Optimality proof:** This approach is optimal because it avoids the need to generate all possible arrays and calculates the subset sums directly using the bitmask, resulting in a significant reduction in time and space complexity.

### Final Notes

**Learning Points:**
- The problem requires generating all possible subset sums of an array and checking if they match the given subset sums.
- The optimal approach uses a bitmask to represent the subsets of the array and iterates through all possible bitmasks to generate the subset sums.
- The time and space complexity of the optimal approach are significantly better than the brute force approach.

**Mistakes to Avoid:**
- Generating all possible arrays and calculating the sum of all subsets of each array, resulting in exponential time and space complexity.
- Not using a bitmask to represent the subsets of the array, resulting in inefficient iteration through all possible subsets.
- Not checking if the subset sums match the given subset sums, resulting in incorrect output.