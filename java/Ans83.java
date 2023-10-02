package java;

public class Ans83 {
    public static void main(String[] args) {
        ListNode list = new ListNode();
    }
    public void removeduplicates(ListNode head){
        ListNode node = head;
        while (node.next!=null){
            if ( node.val==node.next.val){
                node.next = node.next.next;
                //whenever we are skipping a number the size also decreases
//                if doing with size then do size-- here as well
            } else {
                node = node.next;
            }
        }
        //as now we have reached the last node, so
        //if you have tail in the question, then reassign tail = node; and tail.next = null;
        node.next = null;
    }
}
