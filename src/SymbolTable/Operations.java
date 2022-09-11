package SymbolTable;
import YAPL.YAPLParser;
import YAPL.YAPLUtils;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.TerminalNode;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Operations {

    public Tuple<ArrayList<String>, Tuple<Integer, Integer>> getCTX(ParserRuleContext ctx) {
        ArrayList<String> children = new ArrayList<>();
        List<ParseTree> ctxChildren = ctx.children;

        for (ParseTree ctxChild : ctxChildren) {
            children.add(ctxChild.getText());
        }
        TerminalNode a = (TerminalNode) ctxChildren.get(0);
        Tuple<Integer, Integer> line = new Tuple<>(a.getSymbol().getLine(),
                ((TerminalNode) ctxChildren.get(0)).getSymbol().getCharPositionInLine());

        return new Tuple<>(children, line);
    }

    public boolean insertSelf(Tuple<Integer, Integer> line) {
        return SymbolTable.getSymbolTableInstance()
                .addType("self",44,  line,"ref", "attr",
                        SymbolTable.getSymbolTableInstance().getTables()
                .get(SymbolTable.getSymbolTableInstance().getScopes()
                        .get(SymbolTable.getSymbolTableInstance().getScopes().size() - 1))
                                .getName(), 0,
                0, "");
    }

    public boolean insertClass(YAPLParser.ClassContext ctx) {
        Tuple<ArrayList<String>, Tuple<Integer, Integer>> childrenLine = getCTX(ctx);
        ArrayList<String> children = childrenLine.getX();
        Tuple<Integer, Integer> line = childrenLine.getY();

        int index = YAPLUtils.indx(children, "inherits");

        if(index == -1){
         index = YAPLUtils.indx(children, "INHERITS");
        }
        if(index != -1 && Arrays.asList(new String[]{"Int", "Bool", "String"}).contains(children.get(index + 1))) {
            Errors.getErrorsInstance().addError(line, "Class " + children.get(1) +
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

        List<ParseTree> child = ctx.children;
        TerminalNode a = (TerminalNode) child.get(1);
        int aa = a.getSymbol().getType();
        return SymbolTable.getSymbolTableInstance().addType(children.get(1), aa,
                line, "ref", "class", "", 0, 0, inherits);
    }

    public boolean insertFeature(YAPLParser.FeatureContext ctx) {
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
            type = SymbolTable.getSymbolTableInstance().getTables()
                    .get(SymbolTable.getSymbolTableInstance().getScopes()
                            .get(SymbolTable.getSymbolTableInstance().getScopes().size() - 1)).getName();
        }
        List<ParseTree> child = ctx.children;
        TerminalNode a = (TerminalNode) child.get(0);
        int aa = a.getSymbol().getType();
        return SymbolTable.getSymbolTableInstance().addType(children.get(0), aa,
                line, "ref", semKind, type, paramNumber, 0, "");
    }

    public boolean insertFormal(YAPLParser.FormalContext ctx) {
        Tuple<ArrayList<String>, Tuple<Integer, Integer>> childrenLine = getCTX(ctx);
        ArrayList<String> children = childrenLine.getX();
        Tuple<Integer, Integer> line = childrenLine.getY();
        List<ParseTree> child = ctx.children;
        TerminalNode a = (TerminalNode) child.get(0);
        int aa = a.getSymbol().getType();
        return SymbolTable.getSymbolTableInstance().addType(children.get(0), aa,
                line, "ref", "parameter", children.get(2), 0, 0, "");
    }

    // TODO Check scopes and remove getters
    public boolean insertExpr(YAPLParser.ExprContext ctx) {
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

        List<ParseTree> child = ctx.children;
        TerminalNode a = (TerminalNode) child.get(1);
        int aa = a.getSymbol().getType();
        boolean inserted =SymbolTable.getSymbolTableInstance()
                .addType("let" + SymbolTable.getSymbolTableInstance().letsCounter, aa,
                line, "", "expr", children.get(2), paramNum, 0, "");

        if(inserted){
            SymbolTable.getSymbolTableInstance()
                    .pushToScope("let" + SymbolTable.getSymbolTableInstance().letsCounter);
            SymbolTable.getSymbolTableInstance().letsCounter += 1;

            ArrayList<Integer> indexes = new ArrayList<>();

            for (int i = 0; i < children.size(); i++) {
                if(children.get(i).equals(":")){
                    indexes.add(i);
                }
            }

            for(int i : indexes){
                List<ParseTree> hijo = ctx.children;
                TerminalNode ah = (TerminalNode) hijo.get(i - 1);

                int aah = ah.getSymbol().getType();
                SymbolTable.getSymbolTableInstance().addType(children.get(i - 1),  aah,
                        line, "ref", "attr", children.get(i + 1), 0, 0, "");
            }

            SymbolTable.getSymbolTableInstance().scopes
                    .remove(SymbolTable.getSymbolTableInstance().getScopes().size() - 1);
        }

        return inserted;
    }

//    public boolean insertObj(YAPLParser.ExprContext ctx) {
//        Tuple<ArrayList<String>, Tuple<Integer, Integer>> ª = this.getCTX(ctx);
//        if(this.symbolTable.existInTable(0, ª.getX().get(1))){
//            TableItem tableItem = new TableItem("obj" + this.symbolTable.objectsCounter, ctx.children.get(1).symbo.type, )
//        }
//    }
}
