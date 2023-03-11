Recursion Lecture: https://adaacademy.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=6c9b0e2a-6031-40a9-863b-af690172d08f&start=0


Link to Google Slides: https://docs.google.com/presentation/d/1DrEy1sy7qt2vDp6gKSyuXOvni7NouxfHj6hFAKwYI4I/edit#slide=id.g186221dd0c6_0_153


Array-to-BST Code Block (used at timestamp 24:00)
If you have the screen space available to do so, you can follow along to the whiteboard walkthrough at timestamp 24:00 using the code block below.

```
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


def arr_to_bst(arr):
    if not arr:
        return None

    mid = (len(arr)) // 2

    root = TreeNode(arr[mid])
    root.left = arr_to_bst(arr[:mid])
    root.right = arr_to_bst(arr[mid + 1:])
    return root
```


Python Tutor Link: https://pythontutor.com/visualize.html#mode=display

One can use Python Tutor to visualize what happens in the memory addresses of the Python program for recursive functions.

