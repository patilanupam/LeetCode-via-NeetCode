import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) +1
        
        return heapq.nlargest(k, count.keys(), key = count.get)




"""
HEAP CONCEPT in 2 min GPT SHORT

🧠 What is a Heap (simple)

👉 A heap is just a special structure where:

You can quickly get the smallest or largest element

🎯 Two types
1. Min Heap (default in Python)

👉 Smallest element is always on top

Top → smallest
2. Max Heap

👉 Largest element is on top

Top → largest

(Python doesn’t directly support max heap — we fake it)

🧠 Think of it like a priority queue

Imagine:

You always want the top priority item
You don’t care about full sorting

👉 That’s a heap

📦 Example (Min Heap)
import heapq

nums = [5, 3, 8, 1]

heapq.heapify(nums)

Now internally it becomes:

[1, 3, 8, 5]

👉 Smallest (1) is at top

🔥 Operations
1. Push (add element)
heapq.heappush(nums, 2)

👉 Heap adjusts automatically

2. Pop (remove smallest)
heapq.heappop(nums)

👉 Always removes smallest

🧠 Why heap is powerful

👉 You don’t sort everything
👉 You just keep track of “important elements”

⚡ Real use case (Top K Frequent)

Instead of sorting whole array:

👉 Keep only k elements in heap

📦 Example
import heapq

nums = [1,1,1,2,2,3]
k = 2

We want top 2 frequent elements

👉 Use heap to track top k

🧠 Time complexity
Operation	Time
push	O(log n)
pop	O(log n)
peek	O(1)
⚡ Key intuition

Heap is NOT fully sorted

👉 Only guarantees:

“Top element is correct”

🔥 Simple analogy

Think of a leaderboard:

You don’t sort all players
You just maintain top 10

👉 That’s heap

🚫 Common misunderstanding

People think:

“Heap = sorted array”

❌ Wrong
👉 It’s partially ordered

🎯 One-line understanding

👉 Heap = fast access to min/max without full sorting

🔚 Bottom line
Use heap when:
You need top k elements
You don’t need full sorting

If you want next:
👉 I can show how heap actually rearranges elements step-by-step (this makes it stick permanently)
"""




