class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> lmap = new HashMap<>();
        int[] count = new int[26];
        for (String str: strs) {
            Arrays.fill(count,0);
            for (char c: str.toCharArray()) {
                count[c-'a']++;
            }
            
            StringBuilder sb = new StringBuilder("");
            for (int i=0; i<26; i++) {
                sb.append('#');
                sb.append(count[i]);
            }
            
            String key = sb.toString();
            if (!lmap.containsKey(key)) lmap.put(key, new ArrayList<String>());
            lmap.get(key).add(str);
            
            
        }
        return new ArrayList(lmap.values());
        
        
        
        
        
//         Map<String,List<String>> lmap = new HashMap<>();
        
//         for (String str: strs) {
//             char[] sa = str.toCharArray();
//             Arrays.sort(sa);
//             String key = String.valueOf(sa);
//             if (!lmap.containsKey(key)) {
//                 lmap.put(key, new ArrayList<String>());
//             } 
//             lmap.get(key).add(str);  
//         }
        
//         //System.out.println(lmap);
        
//         return new ArrayList(lmap.values());
    }
}
