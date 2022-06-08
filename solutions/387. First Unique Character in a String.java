class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> sMap = new HashMap<>();
        char[] sArray = s.toCharArray();
        for (char sChar: sArray) {
            sMap.put(sChar,sMap.getOrDefault(sChar,0)+1);
        }
        
        for(int i=0; i<sArray.length; i++)  {
            if (sMap.get(sArray[i])==1) return i;
        }
        return -1;
        
    }
}
