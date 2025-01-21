## Browser History
**Problem Link:** https://leetcode.com/problems/design-browser-history/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a browser history system with methods to visit a URL, back, and forward. The input will be a sequence of these operations.
- Expected output format: The output should be the URL after each operation.
- Key requirements and edge cases to consider: Handling edge cases such as visiting a URL when the history is empty, going back when the history is empty, and going forward when the history is empty.
- Example test cases with explanations:
  - Visiting a URL and then going back.
  - Visiting a URL, going back, and then going forward.
  - Visiting multiple URLs and then going back and forward.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To implement the browser history system, we can use a data structure to store the URLs and keep track of the current position.
- Step-by-step breakdown of the solution:
  1. Create a data structure to store the URLs.
  2. Implement the visit method to add a new URL to the data structure.
  3. Implement the back method to move to the previous URL in the data structure.
  4. Implement the forward method to move to the next URL in the data structure.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient.

```cpp
class BrowserHistory {
private:
    vector<string> history;
    int currentIndex;

public:
    BrowserHistory(string homepage) {
        history.push_back(homepage);
        currentIndex = 0;
    }

    void visit(string url) {
        history.erase(history.begin() + currentIndex + 1, history.end());
        history.push_back(url);
        currentIndex++;
    }

    string back(int steps) {
        currentIndex = max(0, currentIndex - steps);
        return history[currentIndex];
    }

    string forward(int steps) {
        currentIndex = min((int)history.size() - 1, currentIndex + steps);
        return history[currentIndex];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for the visit method, where $n$ is the number of URLs in the history. $O(1)$ for the back and forward methods.
> - **Space Complexity:** $O(n)$, where $n$ is the number of URLs in the history.
> - **Why these complexities occur:** The visit method has a time complexity of $O(n)$ because it may need to erase all URLs after the current index. The back and forward methods have a time complexity of $O(1)$ because they only need to update the current index. The space complexity is $O(n)$ because we need to store all URLs in the history.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a vector to store the URLs and keep track of the current position using an index.
- Detailed breakdown of the approach:
  1. Create a vector to store the URLs.
  2. Implement the visit method to add a new URL to the vector and update the current index.
  3. Implement the back method to move to the previous URL in the vector.
  4. Implement the forward method to move to the next URL in the vector.
- Proof of optimality: This approach is optimal because it uses a vector to store the URLs, which has an average time complexity of $O(1)$ for insertion and deletion operations. The back and forward methods also have a time complexity of $O(1)$ because they only need to update the current index.
- Why further optimization is impossible: This approach is already optimal because it uses a vector to store the URLs and updates the current index in constant time.

```cpp
class BrowserHistory {
private:
    vector<string> history;
    int currentIndex;

public:
    BrowserHistory(string homepage) {
        history.push_back(homepage);
        currentIndex = 0;
    }

    void visit(string url) {
        history.resize(currentIndex + 1);
        history.push_back(url);
        currentIndex++;
    }

    string back(int steps) {
        currentIndex = max(0, currentIndex - steps);
        return history[currentIndex];
    }

    string forward(int steps) {
        currentIndex = min((int)history.size() - 1, currentIndex + steps);
        return history[currentIndex];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for the visit method, $O(1)$ for the back and forward methods.
> - **Space Complexity:** $O(n)$, where $n$ is the number of URLs in the history.
> - **Optimality proof:** The visit method has a time complexity of $O(1)$ because it uses the `push_back` method to add a new URL to the vector, which has an average time complexity of $O(1)$. The back and forward methods have a time complexity of $O(1)$ because they only need to update the current index.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a vector to store URLs and keeping track of the current position using an index.
- Problem-solving patterns identified: Using a data structure to store URLs and updating the current index to implement the back and forward methods.
- Optimization techniques learned: Using a vector to store URLs and updating the current index in constant time.
- Similar problems to practice: Implementing a stack or queue using a vector.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases such as visiting a URL when the history is empty, going back when the history is empty, and going forward when the history is empty.
- Edge cases to watch for: Visiting a URL when the history is empty, going back when the history is empty, and going forward when the history is empty.
- Performance pitfalls: Using a data structure with a high time complexity for insertion and deletion operations.
- Testing considerations: Testing the implementation with different sequences of operations to ensure that it works correctly.