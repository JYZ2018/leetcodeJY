            return isEnd;
        }
        
        public Map<Character, TrieNode> getChildren() {
            return children;
        }
    }
        
​
    public Trie() {
        root = new TrieNode("");
    }
    
    public void insert(String word) {
        if (word==null) return;
        
        TrieNode node = root;
        for (int i=0; i<word.length(); i++) {
            Character ch = word.charAt(i);
            if (!node.getChildren().containsKey(ch)) {
                node.getChildren().put(ch, new TrieNode(ch.toString()));
            }
            
            node= node.getChildren().get(ch);
        }       
        node.isEnd = true;
    }
    
    public boolean search(String word) {
        if (word==null) return false;
        TrieNode node = root;
        for (int i=0; i<word.length(); i++) {
            Character ch = word.charAt(i);
            if (!node.getChildren().containsKey(ch)) return false;
            node=node.getChildren().get(ch);
        }
        return node.getIsEnd();   
    }
    
    public boolean startsWith(String prefix) {
        if (prefix==null) return false;
        TrieNode node = root;
        for (int i=0; i<prefix.length(); i++) {
            Character ch = prefix.charAt(i);
            if (!node.getChildren().containsKey(ch)) return false;
            node=node.getChildren().get(ch);
        }
        return true;  
    }    
}
​
/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
