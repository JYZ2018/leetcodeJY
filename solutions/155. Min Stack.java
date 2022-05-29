class MinStack {
    private LinkedList<Integer> stack;
    int res = Integer.MAX_VALUE;
​
    public MinStack() {
        stack=new LinkedList<Integer>();
        
    }
    
    public void push(int val) {
        if (res>=val) {
            stack.addFirst(res);
            res=val;
        }
        stack.addFirst(val);
        
    }
    
    public void pop() {
        if (stack.getFirst() == res) {
            stack.removeFirst();
            res=stack.getFirst();
        }
        
        stack.removeFirst();
        //System.out.println(stack);
        
    }
    
    public int top() {
    
      return stack.getFirst();
        
    }
    
    public int getMin() {
        
//         int i=0;
      
//         while (i<stack.size()) {
//             if (res>(stack.get(i))) {
//                 res=stack.get(i);
//             }
//             i++; 
//         }
        
//         return res;
        
        return res;
    }
}
​
/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
