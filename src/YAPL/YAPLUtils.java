package YAPL;

import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.TerminalNodeImpl;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class  YAPLUtils<T> {

    public static boolean isTerminalNode(TerminalNodeImpl node){
       return node instanceof TerminalNodeImpl;
    }
/*
    public static ArrayList<Boolean> evaluateTerminalChildren(List<ParseTree> nodes){
        ArrayList<Boolean> terminalChildren = new ArrayList<>();

        for(ParseTree node:nodes){
            terminalChildren.add(isTerminalNode(node));
        }
        return terminalChildren;
    }*/

    public static ArrayList<Integer> getNoTerminalIndexes(ArrayList<Boolean> nodes){
        ArrayList<Integer> noTerminals = new ArrayList<>();
        for (int i = 0; i < nodes.size()-1; i++) {
            if(!nodes.get(i)){
                noTerminals.add(i);
            }
        }
        return noTerminals;
    }

    public static Boolean someErrorType(ArrayList<String> types){
        return Stream.of(types).anyMatch(n -> n.equals("ERROR"));

    }
    public static int indx(ArrayList<String> arr, String element){
        try{
            return arr.indexOf(element);
        }catch(Error a){
            return -1;
        }
    }
    public static int indx(ArrayList<Integer> arr, int element){
        try{
            return arr.indexOf(element);
        }catch(Error a){
            return -1;
        }
    }
    public static int indx(ArrayList<Boolean> arr, boolean element){
        try{
            return arr.indexOf(element);
        }catch(Error a){
            return -1;
        }
    }
}
