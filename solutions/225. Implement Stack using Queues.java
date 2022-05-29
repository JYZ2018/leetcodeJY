class MyStack {
    Queue<Integer> qs1;
    Queue<Integer> qs2;
   
​
    public MyStack() {
         qs1 = new LinkedList<Integer>();
         qs2 = new LinkedList<Integer>();
        
    }
    
    public void push(int x) {
        if (qs2.isEmpty()) qs2.offer(x);
        while (!qs1.isEmpty()) {
            qs2.add(qs1.poll());
        }
        while (!qs2.isEmpty()) {
            qs1.add(qs2.poll());
        }
        
    }
    
    public int pop() {
        return qs1.poll();
    }
    
    public int top() {
        return qs1.peek();
    }
    
    public boolean empty() {
        return qs1.isEmpty();
    }
}
​
/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
