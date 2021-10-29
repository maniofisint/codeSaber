import java.util.Scanner;
import java.util.concurrent.CountDownLatch;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        DoublyLinkedList list1 = new DoublyLinkedList();
        for (int i=0;i<n;i++) {
            list1.add(sc.nextInt());
        }
        DoublyLinkedList.print(list1.header);
    }
}

class DoublyLinkedList{
    private static class Node{
        private int element;
        private Node prev,next;
        public Node(int e, Node p,Node n) {
            element = e;
            next = n;
            prev = p;
        }
        public int getElement() { return element;}
        public Node getNext() {return next;}
        public Node getPrev() {return prev;}
        public void setNext(Node n) {next = n;}
        public void setPrev(Node p) {prev = p;}
    }
    public Node header;
    private Node trailer;
    private int size = 0;
    public DoublyLinkedList() {
        header = new Node(0,null,null);
        trailer = new Node(0,header,null);
        header.setNext(trailer);
    }
    public int size(){return size;}
    public boolean isEmpty(){return size==0;}
    public Node first() {
        if (isEmpty()) return null;
        return header.getNext();
    }
    public Node last() {
        if (isEmpty()) return null;
        return trailer.getPrev();
    }
    public void addFirst(int e) {
        addBetween(e,header,header.getNext());
    }
    public void addLast(int e) {
        addBetween(e,trailer.getPrev(),trailer);
    }
    public void add(int e) {
        if (isEmpty()) addFirst(e);
        addLast(e);
    }
    public int removeFirst() {
        if (isEmpty()) return 0;
        return remove(header.getNext());
    }
    public int removeLast() {
        if (isEmpty()) return 0;
        return remove(trailer.getPrev());
    }
    private void addBetween(int e,Node predecessor,Node successor) {
        Node newest = new Node(e,predecessor,successor);
        predecessor.setNext(newest);
        successor.setPrev(newest);
        size++;
    }
    private int remove(Node node) {
        Node predecessor = node.getPrev();
        Node successor = node.getNext();
        predecessor.setNext(successor);
        successor.setPrev(predecessor);
        size--;
        return node.getElement();
    }
    public static void addTwoList(int n, int m, DoublyLinkedList l1, DoublyLinkedList l2) {
        if (n == m) {
            int carry = 0;
            for (int i=0;i<=n;i++) {
                int num = l1.trailer.element + l2.trailer.element + carry;
                l1.trailer.element = num%10;
                carry = (int) (l1.trailer.element + l2.trailer.element + (carry))/10;
                System.out.println(num+" "+carry+" "+l1.trailer.element);
                l1.trailer = l1.trailer.prev;
                l2.trailer = l2.trailer.prev;
            }
            l1.trailer = l1.trailer.prev;
            l2.trailer = l2.trailer.prev;
        }
       // print(result.getNext().getNext());
    }
    private static void addPrecedingZeros(Node start1, Node start2) {
        Node next1 = start1.next;
        Node next2 = start2.next;
        while (next1 != null && next2 != null) {
            next1 = next1.next;
            next2 = next2.next;
        }
        if (next1 == null && next2 != null) {
            while (next2 != null) {
                Node node = new Node(0,null,null);
                node.next = start1.next;
                start1.next = node;
                next2 = next2.next;
            }
        } else if (next2 == null && next1 != null) {
            while (next1 != null) {
                Node node = new Node(0,null,null);
                node.next = start2.next;
                start2.next = node;
                next1 = next1.next;
            }
        }
    }
    private static int sumTwoNodes(Node first, Node second, Node result) {
        if (first == null) {
            return 0;
        }
        int number = first.getElement() + second.getElement() + sumTwoNodes(first.next, second.next, result);
        Node node = new Node(number % 10,null,null);
        node.next = result.next;
        result.next = node;
        return number / 10;
    }
    public static void print(Node head) {
        Node node = head;
        while (node.getNext()!=null) {
            node = node.getNext();
            System.out.print(node.getElement()+" ");
            
        }
    }
}

