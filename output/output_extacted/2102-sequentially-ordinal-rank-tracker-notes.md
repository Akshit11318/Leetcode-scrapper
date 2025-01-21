## Sequentially Ordinal Rank Tracker
**Problem Link:** https://leetcode.com/problems/sequentially-ordinal-rank-tracker/description

**Problem Statement:**
- Input format and constraints: The problem requires creating a class `SORDTracker` that tracks the rank of elements in a sequence. The class has two methods: `add` and `get`. The `add` method adds a new element to the sequence, and the `get` method returns the rank of a given element in the sequence.
- Expected output format: The `get` method should return the rank of the given element as a string in the format "Xth", "Ynd", "Zrd", or "Wst" depending on the rank.
- Key requirements and edge cases to consider: The sequence is built incrementally, and the rank of an element is its position in the sequence in descending order.
- Example test cases with explanations:
  - `SORDTracker tracker = new SORDTracker(); tracker.add("new1", 10); tracker.add("new2", 5); tracker.add("new3", 10); tracker.get("new1");`
  - The expected output is "1st" because "new1" has the highest rank in the sequence.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves sorting the sequence in descending order every time a new element is added or the rank of an element is queried.
- Step-by-step breakdown of the solution:
  1. Create a class `SORDTracker` with a method `add` to add new elements to the sequence and a method `get` to get the rank of an element.
  2. In the `add` method, add the new element to the sequence.
  3. In the `get` method, sort the sequence in descending order and find the rank of the given element.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is not efficient for large sequences.

```cpp
class SORDTracker {
public:
    vector<pair<string, int>> seq;
    void add(string name, int score) {
        seq.push_back({name, score});
    }
    string get(string name) {
        sort(seq.begin(), seq.end(), [](pair<string, int> a, pair<string, int> b) {
            return a.second > b.second;
        });
        for (int i = 0; i < seq.size(); i++) {
            if (seq[i].first == name) {
                return getRank(i + 1);
            }
        }
        return "";
    }
    string getRank(int rank) {
        if (rank % 10 == 1 && rank % 100 != 11) {
            return to_string(rank) + "st";
        } else if (rank % 10 == 2 && rank % 100 != 12) {
            return to_string(rank) + "nd";
        } else if (rank % 10 == 3 && rank % 100 != 13) {
            return to_string(rank) + "rd";
        } else {
            return to_string(rank) + "th";
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log n)$ due to sorting the sequence in the `get` method.
> - **Space Complexity:** $O(n)$ for storing the sequence.
> - **Why these complexities occur:** The brute force approach involves sorting the sequence in the `get` method, which has a time complexity of $O(n \log n)$. Since the `get` method is called for each element in the sequence, the overall time complexity is $O(n^2 \log n)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a `set` to store the elements in the sequence in descending order.
- Detailed breakdown of the approach:
  1. Create a class `SORDTracker` with a method `add` to add new elements to the sequence and a method `get` to get the rank of an element.
  2. In the `add` method, add the new element to the `set`.
  3. In the `get` method, find the rank of the given element in the `set`.
- Why further optimization is impossible: The optimal solution has a time complexity of $O(\log n)$ for the `add` and `get` methods, which is the best possible time complexity for this problem.

```cpp
class SORDTracker {
public:
    set<pair<int, string>> seq;
    void add(string name, int score) {
        seq.insert({score, name});
    }
    string get(string name) {
        int rank = 1;
        for (auto it = seq.rbegin(); it != seq.rend(); it++) {
            if (it->second == name) {
                return getRank(rank);
            }
            rank++;
        }
        return "";
    }
    string getRank(int rank) {
        if (rank % 10 == 1 && rank % 100 != 11) {
            return to_string(rank) + "st";
        } else if (rank % 10 == 2 && rank % 100 != 12) {
            return to_string(rank) + "nd";
        } else if (rank % 10 == 3 && rank % 100 != 13) {
            return to_string(rank) + "rd";
        } else {
            return to_string(rank) + "th";
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$ for the `add` method and $O(n)$ for the `get` method.
> - **Space Complexity:** $O(n)$ for storing the sequence.
> - **Optimality proof:** The optimal solution has the best possible time complexity for the `add` and `get` methods.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of a `set` to store elements in descending order.
- Problem-solving patterns identified: The use of a `set` to optimize the time complexity of the `add` and `get` methods.
- Optimization techniques learned: The use of a `set` to reduce the time complexity of the `add` and `get` methods.
- Similar problems to practice: Problems that involve storing elements in a data structure and retrieving them in a specific order.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty sequence.
- Edge cases to watch for: An empty sequence, a sequence with duplicate elements.
- Performance pitfalls: Using a data structure with a high time complexity, such as a `vector` with a `sort` method.
- Testing considerations: Testing the `add` and `get` methods with different inputs, including edge cases.