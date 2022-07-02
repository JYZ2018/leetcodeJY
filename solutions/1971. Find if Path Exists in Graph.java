    
    public boolean dfs(Set<Integer>[] graph, int source, int destination, Set<Integer> visited) {
        if (source== destination) return true;
        visited.add(source);
        for (Integer neighbor: graph[source]) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor);
                if (dfs(graph, neighbor, destination, visited)) return true;
            }
        }
        
        return false;
    }
    
    public boolean bfs(Set<Integer>[] graph, int source, int destination, Set<Integer> visited) {
        Deque<Integer> queue = new LinkedList<>();
        queue.offer(source);
        visited.add(source);
        
        while (!queue.isEmpty()) {
            int temp = queue.poll();
            if (temp==destination) return true;
            for (Integer neighbor: graph[temp]) {
                //System.out.println("neighbor "+neighbor);
                if (!visited.contains(neighbor)) {
                    queue.offer(neighbor);
                    visited.add(neighbor);
                }  
            }
        }
        return false;
    }
        
}
