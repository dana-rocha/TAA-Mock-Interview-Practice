# Linked List Exercises

## [Replit] (https://replit.com/@adadev/linked-list-practice-section-b#README.md)

## [Solution] (https://replit.com/@adadev/linked-list-practice-section-a#linked_lists/palindrome_linked_list.py)

## Wave 1: Rotate List

Given the head of a linked list, rotate the list to the right by k places. 

Note that for readability the example input and output nodes are denoted as integers. Your actual function should receive and return `ListNode` objects. The full linked lists the given and returned nodes link to are denoted as Input List and Output List below.

### Rotate List Example 1:

![Two element rotation](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)

**Input:** head = `1`, k = `2`

**Input List:** `[1,2,3,4,5]`

**Output:** `4`

**Output List:** `[4,5,1,2,3]`

### Example 2:

![Four element rotation](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)

**Input:** head = `0`, k = `4`

**Input List:** `[0,1,2]`

**Output** `2`

**Output List:** `[2,0,1]`



## Wave 2: Has Cycle

Given the `head` of a singly linked list, return true if the list has a cycle. A cycle exists if any node in the linked list has already been visited.

Note that for readability, the example input nodes are denoted as integers. Your actual function will be given a `ListNode` object as an argument. The full linked lists the given node `head` links to is denoted as Input List in the examples below.




### Has Cycle Example 1:

![Cycle example](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Input:** head = `3`

**Input List:** `[3,2,0,4]`

**Output:** `True`

### Has Cycle Example 2:

![Cycle example whole list is a cycle](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Input:** head = `1`

**Input List:** `[1,2]`

**Output:** `True`


### Has Cycle Example 3:

![No Cycle example](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

**Input:** head = `1`

**Input List:** `[1]`

**Output:** `False`

*This problem was taken from [Leetcode: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/).*

