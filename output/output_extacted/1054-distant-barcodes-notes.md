## Distant Barcodes
**Problem Link:** https://leetcode.com/problems/distant-barcodes/description

**Problem Statement:**
- Input format and constraints: The problem takes a list of integers representing `barcodes` and an integer `k` as input, where `k` is the minimum distance required between two identical barcodes. The `barcodes` list contains integers from 1 to `n`, where `n` is the number of unique barcodes.
- Expected output format: The function should return a rearranged list of `barcodes` such that the distance between any two identical barcodes is at least `k`.
- Key requirements and edge cases to consider: If it's impossible to rearrange the barcodes to meet the condition, return an empty list. The function should handle cases where `k` is 0 or greater, and where the number of occurrences of a barcode is greater than `k`.
- Example test cases with explanations:
  - Input: `barcodes = [1,1,1,2,2,3], k = 2`, Output: `[1,2,3,1,2,1]`
  - Input: `barcodes = [1,1,1,1,2,2,3,3], k = 3`, Output: `[]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach is to use a brute force method, trying all possible permutations of the `barcodes` list and checking if each permutation meets the condition of having a distance of at least `k` between any two identical barcodes.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the `barcodes` list.
  2. For each permutation, iterate through the list to check if the distance between any two identical barcodes is at least `k`.
  3. If a permutation meets the condition, return it. If no permutation meets the condition, return an empty list.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isValidPermutation(vector<int>& barcodes, int k) {
    for (int i = 0; i < barcodes.size(); i++) {
        for (int j = i + 1; j < barcodes.size(); j++) {
            if (barcodes[i] == barcodes[j] && j - i <= k) {
                return false;
            }
        }
    }
    return true;
}

vector<int> rearrangeBarcodesBruteForce(vector<int>& barcodes, int k) {
    sort(barcodes.begin(), barcodes.end());
    do {
        if (isValidPermutation(barcodes, k)) {
            return barcodes;
        }
    } while (next_permutation(barcodes.begin(), barcodes.end()));
    return {};
}

int main() {
    vector<int> barcodes = {1,1,1,2,2,3};
    int k = 2;
    vector<int> result = rearrangeBarcodesBruteForce(barcodes, k);
    for (int num : result) {
        cout << num << " ";
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n^2)$, where $n$ is the number of barcodes. The reason for this complexity is that we generate all permutations of the `barcodes` list (which takes $O(n!)$ time) and then check each permutation to see if it meets the condition (which takes $O(n^2)$ time).
> - **Space Complexity:** $O(n)$, where $n$ is the number of barcodes. This is because we need to store the `barcodes` list and any additional space required for the permutation generation.
> - **Why these complexities occur:** The brute force approach has high time and space complexities due to the generation of all permutations and the subsequent checks for each permutation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution uses a priority queue to store the barcodes and their frequencies. We first count the frequency of each barcode and store them in a priority queue. Then, we start building the result list by popping the barcode with the highest frequency from the queue and appending it to the result list. We also keep track of the last `k` barcodes we have appended to the result list to ensure that we do not append the same barcode again within a distance of `k`.
- Detailed breakdown of the approach:
  1. Count the frequency of each barcode.
  2. Create a priority queue to store the barcodes and their frequencies.
  3. Initialize an empty result list and a queue to store the last `k` barcodes.
  4. While the priority queue is not empty, pop the barcode with the highest frequency and append it to the result list.
  5. If the queue of last `k` barcodes is full, remove the oldest barcode from the queue.
  6. If the priority queue is empty and the queue of last `k` barcodes is not empty, it means we cannot rearrange the barcodes to meet the condition, so return an empty list.

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

vector<int> rearrangeBarcodes(vector<int>& barcodes, int k) {
    unordered_map<int, int> freq;
    for (int num : barcodes) {
        freq[num]++;
    }
    
    priority_queue<pair<int, int>> pq;
    for (auto& it : freq) {
        pq.push({it.second, it.first});
    }
    
    vector<int> result;
    queue<int> lastK;
    
    while (!pq.empty()) {
        auto top = pq.top();
        pq.pop();
        result.push_back(top.second);
        top.first--;
        
        if (!lastK.empty()) {
            int num = lastK.front();
            lastK.pop();
            if (freq[num] > 0) {
                pq.push({freq[num], num});
            }
        }
        
        if (top.first > 0) {
            freq[top.second] = top.first;
            lastK.push(top.second);
            if (lastK.size() > k) {
                lastK.pop();
            }
        }
    }
    
    if (result.size() != barcodes.size()) {
        return {};
    }
    
    return result;
}

int main() {
    vector<int> barcodes = {1,1,1,2,2,3};
    int k = 2;
    vector<int> result = rearrangeBarcodes(barcodes, k);
    for (int num : result) {
        cout << num << " ";
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of barcodes. The reason for this complexity is that we use a priority queue to store the barcodes and their frequencies, and we perform $n$ push and pop operations on the queue.
> - **Space Complexity:** $O(n)$, where $n$ is the number of barcodes. This is because we need to store the `barcodes` list, the frequency map, the priority queue, and the queue of last `k` barcodes.
> - **Optimality proof:** This solution is optimal because we use a priority queue to efficiently select the barcode with the highest frequency and append it to the result list, while ensuring that we do not append the same barcode again within a distance of `k`. We also use a queue to keep track of the last `k` barcodes, which allows us to efficiently remove the oldest barcode from the queue when it is full.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, queue, and frequency counting.
- Problem-solving patterns identified: Using a priority queue to efficiently select the barcode with the highest frequency and append it to the result list, while ensuring that we do not append the same barcode again within a distance of `k`.
- Optimization techniques learned: Using a queue to keep track of the last `k` barcodes and removing the oldest barcode from the queue when it is full.
- Similar problems to practice: Other problems that involve rearranging elements to meet certain conditions, such as rearranging a string to meet a certain condition.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the queue of last `k` barcodes is full before removing the oldest barcode, or not updating the frequency map correctly.
- Edge cases to watch for: Handling cases where `k` is 0 or greater, and where the number of occurrences of a barcode is greater than `k`.
- Performance pitfalls: Not using a priority queue to efficiently select the barcode with the highest frequency and append it to the result list, or not using a queue to keep track of the last `k` barcodes.
- Testing considerations: Testing the function with different inputs, including edge cases, and verifying that the output is correct.