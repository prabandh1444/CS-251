package Q1;

import java.util.Map.Entry;
import java.util.*; 
import java.util.regex.*;

public class Graph {

    // Assume maximum path length to be less than INF
    private static Integer INF = 1000*1000*1000 ;
    private Map<String, Node> nodeMap = new HashMap<>() ;
    
    public void addNode(String name) {
        /*
         * TODO: Implement this method
         */
        Node new_node = new Node(name);
        nodeMap.put(name,new_node);
        return;
    }

    public void addDirectedEdge(String nameA, String nameB, Integer distance) {
        /*
         * TODO: Implement this method
         * Check if nodes with nameA and nameB exist.
         */
        assert (nodeMap.containsKey(nameA)&&nodeMap.containsKey(nameB)) : "Given Cities arent Present";
        nodeMap.get(nameA).addNeighbour(nodeMap.get(nameB),distance);
        return;
    }

    public Map<String, Integer> dijkstraAlgorithm(String source) {
        /*
         * TODO: Implement this method
         * Return a map of name of all the nodes
         * with the minimum distance from source node
         */
        Integer size = nodeMap.size();
        Node Source = nodeMap.get(source);
        Node min_node_path = Source;
        Map<String,Integer> min = new HashMap<>();
        for (Map.Entry<String, Node> e : nodeMap.entrySet()){
            if(!source.equals(e.getKey())) min.put(e.getKey(),INF);
            else min.put(source,0);
        }
        Integer numberofIterations=0;
        while(numberofIterations<size){
            Entry<Node, Integer> min_so_far = null;
        for (Entry<Node,Integer> entry : min_node_path.adjacentNodes.entrySet()) {
            Integer k;
            k = Math.min(min.get(min_node_path.getName())+entry.getValue(),min.get(entry.getKey().getName()));
            min.put(entry.getKey().getName(),k);
            }
        for (Entry<Node,Integer> entry : min_node_path.adjacentNodes.entrySet()) {
            if (min_so_far == null || min.get(min_so_far.getKey().getName()) > min.get(entry.getKey().getName())) {
                min_so_far = entry;
            } 
        }   
            min_node_path=min_so_far.getKey(); 
            numberofIterations++;         
        }   
        return min;
    } 
}