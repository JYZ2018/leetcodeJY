import java.util.ArrayList;
import java.io.*;
import java.util.*;
import java.util.Collections;
​
class Solution {
    public boolean isSubsequence(String s, String t) {
        ArrayList<Integer> [] positions = new ArrayList [26];
        /* for (char c: s.toCharArray()) */
        for (int i=0; i<t.length();i++) {
            int index = t.charAt(i) -'a';
            if (positions[index] == null) {
                positions[index]=new ArrayList<Integer>();
            }
           positions[index].add(i);
        }
      
        
        int start=0;
        for  (int j=0; j<s.length(); j++) {
            
            int lett=s.charAt(j)-'a';
            if (positions[lett]==null) {return false;}
            int insertion = Collections.binarySearch(positions[lett],start);
            if (insertion <0 ) {
                insertion = -(insertion+1);
                            }
            if (insertion==positions[lett].size()) {return false;}
            start=positions[lett].get(insertion)+1;
        }
       return true; 
    }
}
