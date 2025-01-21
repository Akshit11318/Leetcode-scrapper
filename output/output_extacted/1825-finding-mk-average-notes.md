## Finding MK Average

**Problem Link:** https://leetcode.com/problems/finding-mk-average/description

**Problem Statement:**
- Input format: You are given a stream of integers `nums`, an integer `k`, and an integer `m`. 
- Constraints: `1 <= k <= 1000`, `1 <= m <= 1000`, `1 <= nums[i] <= 1000`, `1 <= i <= 1000`.
- Expected output format: Create an `MKAverage` object, then call `addElement` and `calculateMKAverage` methods to add elements and calculate the MKAverage respectively.
- Key requirements and edge cases to consider: Handle cases where the window size `k` is larger than the number of elements in the stream, and handle cases where `m` is larger than the number of elements in the window.
- Example test cases with explanations: 
  - `MKAverage mka = new MKAverage([1,3,10,5,2,4], 3, 1);` 
  - `mka.addElement(5);`
  - `mka.calculateMKAverage();`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the MKAverage, we need to maintain a window of `k` elements, sort them, and then find the `m`th smallest and largest elements.
- Step-by-step breakdown of the solution:
  1. Create a queue to maintain the window of `k` elements.
  2. When a new element is added, remove the oldest element from the window if it is full.
  3. Sort the elements in the window.
  4. Find the `m`th smallest and largest elements.
  5. Calculate the MKAverage by taking the average of the elements between the `m`th smallest and largest elements (inclusive).

```cpp
#include <queue>
#include <vector>
#include <algorithm>

class MKAverage {
public:
    MKAverage(std::vector<int>& nums, int k, int m) : k(k), m(m) {
        for (int num : nums) {
            addElement(num);
        }
    }

    void addElement(int num) {
        window.push(num);
        if (window.size() > k) {
            window.pop();
        }
    }

    int calculateMKAverage() {
        if (window.size() < k) {
            return -1;
        }
        std::vector<int> sortedWindow(window.begin(), window.end());
        std::sort(sortedWindow.begin(), sortedWindow.end());
        int sum = 0;
        for (int i = m; i < k - m; i++) {
            sum += sortedWindow[i];
        }
        return sum / (k - 2 * m);
    }

private:
    std::queue<int> window;
    int k;
    int m;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k \cdot log(k))$ where $n$ is the number of elements in the stream. This is because for each element, we are sorting the window of size $k$.
> - **Space Complexity:** $O(k)$ for storing the window of elements.
> - **Why these complexities occur:** The time complexity occurs because we are sorting the window for each new element, and the space complexity occurs because we need to store the window of elements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a multiset to maintain the window of elements, which allows for efficient insertion and removal of elements, as well as finding the `m`th smallest and largest elements.
- Detailed breakdown of the approach:
  1. Create a multiset to maintain the window of elements.
  2. When a new element is added, remove the oldest element from the window if it is full.
  3. Use the multiset to find the `m`th smallest and largest elements.
  4. Calculate the MKAverage by taking the average of the elements between the `m`th smallest and largest elements (inclusive).

```cpp
#include <multiset>
#include <queue>

class MKAverage {
public:
    MKAverage(std::vector<int>& nums, int k, int m) : k(k), m(m) {
        for (int num : nums) {
            addElement(num);
        }
    }

    void addElement(int num) {
        window.push(num);
        windowSet.insert(num);
        if (window.size() > k) {
            windowSet.erase(windowSet.find(window.front()));
            window.pop();
        }
    }

    int calculateMKAverage() {
        if (window.size() < k) {
            return -1;
        }
        auto it = windowSet.begin();
        std::advance(it, m - 1);
        int sum = 0;
        for (int i = 0; i < k - 2 * m; i++) {
            sum += *it;
            std::advance(it, 1);
        }
        return sum / (k - 2 * m);
    }

private:
    std::queue<int> window;
    std::multiset<int> windowSet;
    int k;
    int m;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(k))$ where $n$ is the number of elements in the stream. This is because for each element, we are inserting and removing elements from the multiset.
> - **Space Complexity:** $O(k)$ for storing the window of elements.
> - **Optimality proof:** This is the optimal solution because we are using a multiset to maintain the window of elements, which allows for efficient insertion and removal of elements, as well as finding the `m`th smallest and largest elements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a multiset to maintain a window of elements, finding the `m`th smallest and largest elements.
- Problem-solving patterns identified: Using data structures to maintain a window of elements, finding the average of elements between two indices.
- Optimization techniques learned: Using a multiset to reduce the time complexity of finding the `m`th smallest and largest elements.
- Similar problems to practice: Problems that involve maintaining a window of elements, finding the average of elements between two indices.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not handling cases where the window size `k` is larger than the number of elements in the stream.
- Edge cases to watch for: Cases where the window size `k` is larger than the number of elements in the stream, cases where `m` is larger than the number of elements in the window.
- Performance pitfalls: Using a data structure that has a high time complexity for insertion and removal of elements, not using a data structure that allows for efficient finding of the `m`th smallest and largest elements.
- Testing considerations: Test cases where the window size `k` is larger than the number of elements in the stream, test cases where `m` is larger than the number of elements in the window.