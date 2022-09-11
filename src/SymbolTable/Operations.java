package SymbolTable;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class Operations {
    SymbolTable symbolTable;


    public Operations(){
        symbolTable = new SymbolTable();
    }

    public Tuple<ArrayList<String>, Tuple<Integer, Integer>> getCTX(ParserRuleContext parserRuleContext) {
        ArrayList<String> children = new ArrayList<>();
        ArrayList<ParserRuleContext> ctxChildren = parserRuleContext.children;

        for (int i = 0; i < ctxChildren.size() ; i++) {
            children.add(ctxChildren[i].getText());
        }

        Tuple<Integer, Integer> line = new Tuple<>(ctxChildren[0].symbol.line, ctxChildren[0].symbol.column);

        return new Tuple<>(children, line);
    }

    public boolean insertSelf(Tuple<Integer, Integer> line) {
        return symbolTable.addType("self",44,  line,"ref", "attr", symbolTable.getTables()
                .get(symbolTable.getScopes().get(symbolTable.getScopes().size() - 1)).getName(), 0,
                0, "");
    }

    public boolean insertClass(YaplParser.ClassContext ctx) {
        Tuple<ArrayList<String>, Tuple<Integer, Integer>> childrenLine = getCTX(ctx);
        ArrayList<String> children = childrenLine.getX();
        Tuple<Integer, Integer> line = childrenLine.getY();
        int index = children.indexOf("inherits");
        if(index == -1){
         index = children.indexOf("INHERITS");
        }else {
            symbolTable.getErrorMessage().addError(line, "Class " + children.get(1) +
                    " can't inherit from " + children.get(index + 1));
            return false;
        }

        String inherits = "";

        if(index != -1){
            inherits = children.get(index + 1);
        }else {
            if(!children.get(1).equals("Main")){
                inherits = "Object";
            }
        }

        return this.symbolTable.addType(children.get(1), ctx.children[1].symbol.type,
                line, "ref", "class", "", "", "", inherits);
    }

    public boolean insertFeature(YaplParser.FeatureContext ctx) {
        Tuple<ArrayList<String>, Tuple<Integer, Integer>> childrenLine = getCTX(ctx);
        ArrayList<String> children = childrenLine.getX();
        Tuple<Integer, Integer> line = childrenLine.getY();
        int index = children.indexOf("inherits");
        String semKind = "";

        if(!children.get(1).equals(":")){
            semKind = "method";
        }else{
            semKind = "attr";
        }


        int paramNumber = 0;
        if(semKind.equals("method")) {
            ArrayList<String> filteredList = new ArrayList<>();
            //TODO meterle la verga a Andre y las funciones en archivo aparte
            for (int i = 2; i < children.indexOf(")"); i++) {
                if(!children.get(i).equals(",")) {
                    filteredList.add(children.get(i));
                }
            }
            paramNumber = filteredList.size();
        }

        String type = "";

        if(!children.get(index + 1).equals("SELF_TYPE")) {
            type = children.get(index + 1);
        }else {
            type = symbolTable.getTables().get(symbolTable.getScopes().get(symbolTable.getScopes().size() - 1)).getName();
        }
        return this.symbolTable.addType(children.get(0), ctx.children[0].symbol.type,
                line, "ref", semKind, type, paramNumber, 0, "");
    }

    public boolean insertFormal(YaplParser.FormalContext ctx) {
        Tuple<ArrayList<String>, Tuple<Integer, Integer>> childrenLine = getCTX(ctx);
        ArrayList<String> children = childrenLine.getX();
        Tuple<Integer, Integer> line = childrenLine.getY();

        return this.symbolTable.addType(children.get(0), ctx.children[0].symbol.type,
                line, "ref", "parameter", children.get(2), 0, 0, "");
    }

    public boolean insertExpr(YaplParser.ExprContext ctx) {
        Tuple<ArrayList<String>, Tuple<Integer, Integer>> childrenLine = getCTX(ctx);
        ArrayList<String> children = childrenLine.getX();
        Tuple<Integer, Integer> line = childrenLine.getY();

        int paramNum = 0;
        if(children.get(0).toLowerCase().equals("let")){
            ArrayList<String> filteredList = new ArrayList<>();
            for (int i = 2; i < children.size() - 1 ; i++) {
                if(children.get(i).equals(":")){
                    filteredList.add(children.get(i));
                }
            }
            paramNum = filteredList.size();
        }

        boolean inserted = this.symbolTable.addType("let" + symbolTable.letsCounter, ctx.children[1].symbol.type,
                line, "", "expr", children.get(2), paramNum, 0, "");

        if(inserted){
            symbolTable.pushToScope("let" + symbolTable.letsCounter);
            symbolTable.letsCounter += 1;

            ArrayList<Integer> indexes = new ArrayList<>();

            for (int i = 0; i < children.size(); i++) {
                if(children.get(i).equals(":")){
                    indexes.add(i);
                }
            }

            for(int i : indexes){
                this.symbolTable.addType(children.get(i - 1), ctx.children[i - 1].symbol.type,
                        line, "ref", "attr", children.get(i + 1), 0, 0, "");
            }

            this.symbolTable.getScopes().remove(this.symbolTable.getScopes().size() - 1);
        }

        return inserted;
    }
}
