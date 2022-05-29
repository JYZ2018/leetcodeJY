class MyQueue {
    private Stack<Integer> qs1;
    private Stack<Integer> qs2;
​
    public MyQueue() {
        qs1 = new Stack<Integer>();
        qs2 = new Stack<Integer>();
        
    }
    
    public void push(int x) {
       
        while (!qs1.empty()) {
            qs2.push(qs1.pop());
        }
        qs1.push(x);
        while(!qs2.empty()) {
            qs1.push(qs2.pop());
        }
        
    }
    
    public int pop() {
        return qs1.pop();
        
    }
    
    public int peek() {
        return qs1.peek();
        
    }
    
    public boolean empty() {
        return qs1.empty();
        
    }
}
​
/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
