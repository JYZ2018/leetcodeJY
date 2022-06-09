class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String,List<String>> lmap = new HashMap<>();
        
        for (String str: strs) {
            char[] sa = str.toCharArray();
            Arrays.sort(sa);
            String key = String.valueOf(sa);
            if (!lmap.containsKey(key)) {
                lmap.put(key, new ArrayList<String>());
            } 
            lmap.get(key).add(str);  
        }
        
        //System.out.println(lmap);
        
        return new ArrayList(lmap.values());
    }
}
