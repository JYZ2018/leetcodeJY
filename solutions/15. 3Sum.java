        
       
        Arrays.sort(nums);
        
        List<List<Integer>> result= new ArrayList<>();
        if (nums.length<3) {return result;}
        Arrays.sort(nums);
        for (int i=0; i<nums.length-2;i++) {
            if (i==0 || (i>0 && nums[i]!=nums[i-1])) {
                int l=i+1, r=nums.length-1 ;
                
                while (l<r) {
                
                if (nums[i]+nums[l]+nums[r]==0) {
                    result.add(Arrays.asList(nums[i],nums[l],nums[r]));
                    while (l<r && nums[l]==nums[l+1] ) {l++;}
                    while (l<r && nums[r]==nums[r-1]) {r--;}
                    l++; r--;
                }
                    
                else if (nums[i]+nums[l]+nums[r]<0) {
                    //while (l<r && nums[l]==nums[l+1] ) {l++;};
                    l++;}
                else { 
                    //while (l<r && nums[r]==nums[r-1]) {r--;};
                      r--;}
                }      
            }
        }
        
        return result;
        
        
        
        /* List<List<Integer>> result= new ArrayList<>();
        Arrays.sort(nums);
        for (int i=0;  i<nums.length; i++) {
           if ((i>0 && nums[i]!=nums[i-1])  || i==0) {
           int l=i+1;
           int r=nums.length-1;
           while (l<r) {
               //System.out.println("nums[i]+nums[1]+nums[r] is: "+(nums[i]+nums[l]+nums[r] ));
               //System.out.println("nums[i] is: "+nums[i]+" nums[l] is: "+nums[l]+" nums[r] is: "+nums[r] );
               if (nums[i]+nums[l]+nums[r]==0) {
                  // System.out.println("l is: "+l+" r is : "+r);
                   ArrayList<Integer> temp = new ArrayList<Integer>();
                   if ((nums[l]!=nums[l-1]) ||  l==i+1) {
                       //temp.add(nums[i]);
                       //temp.add(nums[l]);
                       //temp.add(nums[r]);
                       result.add(Arrays.asList(nums[i],nums[l],nums[r]));
