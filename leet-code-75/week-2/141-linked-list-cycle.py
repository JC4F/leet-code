'''
Solution 1: O(n)

public boolean hasCycle(ListNode head) {
    if(head==null) return false;
    ListNode walker = head;
    ListNode runner = head;
    while(runner.next!=null && runner.next.next!=null) {
        walker = walker.next;
        runner = runner.next.next;
        if(walker==runner) return true;
    }
    return false;
}
Use two pointers, walker and runner.
walker moves step by step. runner moves two steps at time.
if the Linked List has a cycle walker and runner will meet at some point.
'''