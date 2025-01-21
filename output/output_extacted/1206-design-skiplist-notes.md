## Design Skiplist
**Problem Link:** [https://leetcode.com/problems/design-skiplist/description](https://leetcode.com/problems/design-skiplist/description)

**Problem Statement:**
- Input format and constraints: The problem asks to design a skiplist, which is a probabilistic data structure that facilitates fast search within an ordered sequence of elements. The input will include various operations like `search`, `add`, and `erase`.
- Expected output format: The output will be boolean values for `search` and `erase` operations, and `void` for the `add` operation.
- Key requirements and edge cases to consider: Handling duplicate elements, maintaining the ordered sequence, and ensuring the skiplist remains balanced.
- Example test cases with explanations: 
  - Adding elements and then searching for them.
  - Erasing elements and verifying their removal.
  - Handling duplicate elements during addition and search.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Implement a basic linked list and perform operations linearly.
- Step-by-step breakdown of the solution:
  1. Create a linked list with a `head` node.
  2. For `add` operation, traverse the list to find the correct position and insert the new node.
  3. For `search` operation, traverse the list to find the target element.
  4. For `erase` operation, find the element and remove it by updating pointers.
- Why this approach comes to mind first: It's the simplest data structure that comes to mind for ordered sequences.

```cpp
class Skiplist {
public:
    struct Node {
        int val;
        Node* next;
        Node(int v) : val(v), next(nullptr) {}
    };

    Skiplist() : head(new Node(0)) {}

    bool search(int target) {
        Node* curr = head;
        while (curr) {
            if (curr->val == target) return true;
            curr = curr->next;
        }
        return false;
    }

    void add(int num) {
        Node* newNode = new Node(num);
        if (!head->next || num < head->next->val) {
            newNode->next = head->next;
            head->next = newNode;
        } else {
            Node* curr = head->next;
            while (curr->next && curr->next->val < num) {
                curr = curr->next;
            }
            newNode->next = curr->next;
            curr->next = newNode;
        }
    }

    bool erase(int num) {
        Node* curr = head;
        while (curr->next) {
            if (curr->next->val == num) {
                curr->next = curr->next->next;
                return true;
            }
            curr = curr->next;
        }
        return false;
    }

private:
    Node* head;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for all operations, where $n$ is the number of elements in the skiplist, because in the worst case, we might have to traverse the entire list.
> - **Space Complexity:** $O(n)$ for storing the elements.
> - **Why these complexities occur:** The brute force approach involves linear traversal for all operations, leading to $O(n)$ time complexity. The space complexity is linear because we store each element in a node.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Utilize a skiplist with multiple levels to reduce the time complexity of search, add, and erase operations.
- Detailed breakdown of the approach:
  1. Implement a skiplist with a specified maximum level and a randomization factor to decide the level of each new node.
  2. For `add` operation, generate a random level for the new node and insert it into the skiplist while maintaining the order.
  3. For `search` operation, start from the highest level and move down the levels until the target is found or it's determined the target is not in the list.
  4. For `erase` operation, find the node to be erased by searching and then remove it by updating the pointers of the previous nodes at all levels.
- Proof of optimality: The skiplist's average time complexity for search, add, and erase operations is $O(\log n)$, making it more efficient than the brute force approach for large datasets.

```cpp
#include <random>
class Skiplist {
public:
    struct Node {
        int val;
        vector<Node*> next;
        Node(int v, int level) : val(v), next(level, nullptr) {}
    };

    Skiplist() : head(new Node(0, 16)), level(1), rnd(random_device{}()) {}

    bool search(int target) {
        Node* curr = head;
        for (int i = level - 1; i >= 0; --i) {
            while (curr->next[i] && curr->next[i]->val < target) {
                curr = curr->next[i];
            }
        }
        return curr->next[0] && curr->next[0]->val == target;
    }

    void add(int num) {
        int newLevel = randomLevel();
        if (newLevel > level) {
            level = newLevel;
        }
        Node* newNode = new Node(num, newLevel);
        vector<Node*> update(level);
        Node* curr = head;
        for (int i = level - 1; i >= 0; --i) {
            while (curr->next[i] && curr->next[i]->val < num) {
                curr = curr->next[i];
            }
            if (i < newLevel) {
                update[i] = curr;
            }
        }
        for (int i = 0; i < newLevel; ++i) {
            newNode->next[i] = update[i]->next[i];
            update[i]->next[i] = newNode;
        }
    }

    bool erase(int num) {
        vector<Node*> update(level);
        Node* curr = head;
        for (int i = level - 1; i >= 0; --i) {
            while (curr->next[i] && curr->next[i]->val < num) {
                curr = curr->next[i];
            }
            update[i] = curr;
        }
        if (curr->next[0] && curr->next[0]->val == num) {
            for (int i = 0; i < level; ++i) {
                if (update[i]->next[i] && update[i]->next[i]->val == num) {
                    update[i]->next[i] = update[i]->next[i]->next[i];
                } else {
                    break;
                }
            }
            while (level > 1 && !head->next[level - 1]) {
                --level;
            }
            return true;
        }
        return false;
    }

private:
    Node* head;
    int level;
    mt19937 rnd;

    int randomLevel() {
        int level = 1;
        while ((rnd() % 2) && level < 16) {
            ++level;
        }
        return level;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$ for all operations on average, where $n$ is the number of elements in the skiplist.
> - **Space Complexity:** $O(n)$ for storing the elements, where $n$ is the number of elements.
> - **Optimality proof:** The skiplist's design allows for efficient search, insertion, and deletion with an average time complexity of $O(\log n)$, which is optimal for a data structure that maintains sorted order and allows for these operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of probabilistic data structures like skiplists for achieving efficient search, insertion, and deletion in ordered sequences.
- Problem-solving patterns identified: Utilizing multiple levels to reduce time complexity.
- Optimization techniques learned: Randomization for determining node levels.
- Similar problems to practice: Implementing other probabilistic data structures or optimizing existing ones.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating pointers during insertion or deletion, not handling edge cases properly.
- Edge cases to watch for: Empty lists, lists with a single element, duplicate elements.
- Performance pitfalls: Not utilizing the skiplist's levels efficiently, leading to $O(n)$ time complexity.
- Testing considerations: Thoroughly test all operations (`search`, `add`, `erase`) with various inputs, including edge cases.