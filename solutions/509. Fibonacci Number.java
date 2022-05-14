class Solution {
    public int fib(int n) {
        
        
        //recursive
        // if (n==0) return 0;
        // if (n==1) return 1;
        // return fib(n-1)+fib(n-2);
        
        //iterative
        if (n==0) return 0;
        if (n==1) return 1;
        int pprev=0, prev=1, res=0;
        for (int i=2; i<=n; i++) {
            res=pprev+prev;
            pprev=prev;
            prev=res;
     
            //System.out.println(pprev+" "+prev);
        }
        return res;
     
        
        
    }
}
