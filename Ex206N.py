# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

from typing import Optional

def reverseList(head):
    last_index = len(head) - 1
    i = 0
    teste  = 5

    for number in head:
        head[i] == head[last_index]
        print(head)
        i += 1
        teste -= 5
        last_index -= 1


    return head

head = [1,2,5]
print(reverseList(head))        