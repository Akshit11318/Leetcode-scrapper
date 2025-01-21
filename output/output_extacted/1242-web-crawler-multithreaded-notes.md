## Web Crawler Multithreaded
**Problem Link:** [https://leetcode.com/problems/web-crawler-multithreaded/description](https://leetcode.com/problems/web-crawler-multithreaded/description)

**Problem Statement:**
- Input: `startUrl` (the initial URL to start the crawl), `htmlParser` (a function that takes a URL and returns a list of all URLs found on the page), and `maxVisits` (the maximum number of pages to visit).
- Expected output: A list of all URLs visited during the crawl.
- Key requirements: The crawl should be performed in a multithreaded manner, and the `htmlParser` function should be called for each URL to extract the links.
- Example test cases:
  - `startUrl = "http://example.com"`, `htmlParser = ["http://example.com/link1", "http://example.com/link2"]`, `maxVisits = 10`
  - `startUrl = "http://example.com"`, `htmlParser = ["http://example.com/link1", "http://example.com/link2"]`, `maxVisits = 5`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to create a multithreaded web crawler that visits each URL in the `startUrl` and extracts all the links on the page using the `htmlParser` function.
- The brute force approach involves creating a new thread for each URL to be visited and using a shared queue to store the URLs to be visited.
- This approach comes to mind first because it is a straightforward way to implement multithreading in the web crawler.

```cpp
#include <queue>
#include <thread>
#include <mutex>
#include <vector>
#include <string>

class Solution {
public:
    vector<string> crawl(string startUrl, HtmlParser htmlParser) {
        queue<string> urlQueue;
        vector<string> visited;
        mutex mtx;

        urlQueue.push(startUrl);

        while (!urlQueue.empty() && visited.size() < maxVisits) {
            string url = urlQueue.front();
            urlQueue.pop();

            if (find(visited.begin(), visited.end(), url) == visited.end()) {
                visited.push_back(url);

                vector<string> links = htmlParser.getUrls(url);
                for (string link : links) {
                    if (link.find(startUrl.substr(0, startUrl.find('/', 8))) == 0) {
                        urlQueue.push(link);
                    }
                }
            }
        }

        return visited;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of URLs to visit and $m$ is the average number of links on each page. The `htmlParser` function is called for each URL, resulting in $O(n \cdot m)$ time complexity.
> - **Space Complexity:** $O(n)$, where $n$ is the number of URLs to visit. The `visited` vector stores all the visited URLs, resulting in $O(n)$ space complexity.
> - **Why these complexities occur:** The time complexity occurs because the `htmlParser` function is called for each URL, and the space complexity occurs because all the visited URLs are stored in the `visited` vector.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a `std::set` to store the visited URLs, which provides constant time complexity for lookups.
- The optimal approach also involves using a `std::queue` to store the URLs to be visited, which provides efficient insertion and removal of URLs.
- The optimal approach uses a `std::thread` pool to perform the crawl in a multithreaded manner, which improves the performance of the crawl.

```cpp
#include <queue>
#include <thread>
#include <mutex>
#include <set>
#include <vector>
#include <string>

class Solution {
public:
    vector<string> crawl(string startUrl, HtmlParser htmlParser) {
        set<string> visited;
        queue<string> urlQueue;
        vector<string> result;
        mutex mtx;

        urlQueue.push(startUrl);

        while (!urlQueue.empty() && result.size() < maxVisits) {
            string url = urlQueue.front();
            urlQueue.pop();

            if (visited.find(url) == visited.end()) {
                {
                    lock_guard<mutex> lock(mtx);
                    visited.insert(url);
                    result.push_back(url);
                }

                vector<string> links = htmlParser.getUrls(url);
                for (string link : links) {
                    if (link.find(startUrl.substr(0, startUrl.find('/', 8))) == 0) {
                        urlQueue.push(link);
                    }
                }
            }
        }

        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of URLs to visit and $m$ is the average number of links on each page. The `htmlParser` function is called for each URL, resulting in $O(n \cdot m)$ time complexity.
> - **Space Complexity:** $O(n)$, where $n$ is the number of URLs to visit. The `visited` set stores all the visited URLs, resulting in $O(n)$ space complexity.
> - **Optimality proof:** The optimal approach is optimal because it uses a `std::set` to store the visited URLs, which provides constant time complexity for lookups, and a `std::queue` to store the URLs to be visited, which provides efficient insertion and removal of URLs. The use of a `std::thread` pool also improves the performance of the crawl.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: multithreading, URL crawling, and set operations.
- Problem-solving patterns identified: using a `std::set` to store visited URLs and a `std::queue` to store URLs to be visited.
- Optimization techniques learned: using a `std::thread` pool to improve performance.
- Similar problems to practice: URL crawling, multithreading, and set operations.

**Mistakes to Avoid:**
- Common implementation errors: not using a `std::set` to store visited URLs, not using a `std::queue` to store URLs to be visited.
- Edge cases to watch for: handling duplicate URLs, handling URLs with different protocols (e.g., HTTP and HTTPS).
- Performance pitfalls: not using a `std::thread` pool to improve performance.
- Testing considerations: testing the crawl with different URLs, testing the crawl with different `maxVisits` values.