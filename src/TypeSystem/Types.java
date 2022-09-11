package TypeSystem;
import org.antlr.v4.runtime.*;
import SymbolTable.*;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Stream;
import YAPL.YAPLParser;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.TerminalNode;
import org.antlr.v4.runtime.tree.TerminalNodeImpl;

public class Types {
    HashMap<Tuple<Integer, Integer>, String> rules;
    SymbolTable symbolTable;



    public Types() {
        rules = new HashMap<>();
        symbolTable = new SymbolTable();
    }


    public String getFather(String clase) {
        TableItem item = this.symbolTable.get(clase);
        if(!item.getInherits().equals("")){
            return item.getInherits();
        }else {
            return clase;
        }
    }


    public String castBool(String clase) {
        if(clase.equals("Int")){
            return "Bool";
        }else {
            return clase;
        }
    }

    public String castInt(String clase) {
        if(clase.equals("Bool")){
            return "Int";
        }else {
            return clase;
        }
    }


    public String getBaseCaseType(YAPLParser.ExprContext ctx){
        List<ParseTree> hijo = ctx.children;
        TerminalNode a = (TerminalNode) hijo.get(0);
        TerminalNode b = (TerminalNode) hijo.get(1);
        int aa = a.getSymbol().getType();
        int bb = b.getSymbol().getType();


        if(a.getSymbol().getType() == 12){
            if(this.symbolTable.exists(((TerminalNode)ctx.children.get(1)).getText())){
                return ((TerminalNode)ctx.children.get(1)).getText();
            }else {
                return "ERROR";
            }
        //  masdhjg  ((TerminalNode)ctx.children.get(x)).getText();
          //  ((TerminalNode)ctx.children.get(x).get)
        }else if(aa == 44){
            if(this.symbolTable.exists(((TerminalNode)ctx.children.get(0)).getText())){
                TableItem element = this.symbolTable.get(((TerminalNode)ctx.children.get(0)).getText());
                if(element.getSem_kind().equals("attr") || element.getSem_kind().equals("parameter")) {
                    if(ctx.getChildCount() == 1){
                        return element.getTyp();
                    }else if(bb == 25 || bb == 34) {
                        return element.getTyp();
                    }else {

                        Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
                        Errors.getErrorsInstance().addError(line, "Can't access to " + ((TerminalNode)ctx.children.get(1)).getText() + " of a variable");
                        return "ERROR";
                    }
                    //check
                }else if(element.getSem_kind().equals("Method")) {
                    if(ctx.getChildCount() > 1 && bb == 22 ) {
                        return element.getTyp();
                    }else {
                        Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
                        Errors.getErrorsInstance().addError(line, "Can't access to " + ((TerminalNode)ctx.children.get(1)).getText() + " of a method");
                        return "ERROR";
                    }
                }
            }else {
                Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
                Errors.getErrorsInstance().addError(line, ((TerminalNode)ctx.children.get(0)).getText() + " doesn't exist");
                return "ERROR";
            }
        }else if(aa == 41){
            return "Int";
        }else if(aa == 41){
            return "String";
        }else if(aa == 15 || aa == 16  ) {
            return "Bool";
        }

        return "";
    }


    public Tuple<String, String> getKeyTuple(YAPLParser.ExprContext ctx, ArrayList<Boolean> res) {
        String element1;
        String element2;
        List<ParseTree> hijo = ctx.children;
        TerminalNode a = (TerminalNode) hijo.get(0);
        TerminalNode b = (TerminalNode) hijo.get(1);
        int aa = a.getSymbol().getType();
        int bb = b.getSymbol().getType();

        if(!res.get(0)){
            element1 = "expr";
        }else {
            element1 = String.valueOf(aa); //castear donde se use.
        }

        if(!res.get(1)){
            element2 = "expr";
        }else {
            element2 = String.valueOf(aa);  //castear donde se use.
        }

        return new Tuple<>(element1, element2);
    }

    //validate feature
    public String validateExpr(YAPLParser.ExprContext ctx, ArrayList<String> types, ArrayList<Boolean> res){
        Tuple<String, String> tupla = getKeyTuple(ctx, res);

        // both token int type
        if(Integer.parseInt(tupla.x) == 14 && Integer.parseInt(tupla.y) == 45){
            return this.letExpression(ctx,types);
        }
        if(Integer.parseInt(tupla.x) == 45 && Integer.parseInt(tupla.y) == 35){
            return this.assign(ctx,types);
        }
        //expression type
        if(tupla.x.equals("expr") && Integer.parseInt(tupla.y) == 36){
            return this.exprArroba(ctx,types);
        }
        if(tupla.x.equals("expr") && Integer.parseInt(tupla.y) == 26){
            return this.exprPoint(ctx,types);
        }
        if(tupla.x.equals("expr") && Integer.parseInt(tupla.y) == 29){
            return this.aritmetic(ctx,types);
        }
        if(tupla.x.equals("expr") && Integer.parseInt(tupla.y) == 30){
            return this.aritmetic(ctx,types);
        }
        if(tupla.x.equals("expr") && Integer.parseInt(tupla.y) == 31){
            return this.aritmetic(ctx,types);
        }
        if(tupla.x.equals("expr") && Integer.parseInt(tupla.y) == 32){
            return this.aritmetic(ctx,types);
        }
        if(tupla.x.equals("expr") && Integer.parseInt(tupla.y) == 37){
            return this.compare(ctx,types);
        }
        if(tupla.x.equals("expr") && Integer.parseInt(tupla.y) == 38){
            return this.compare(ctx,types);
        }
        if(tupla.x.equals("expr") && Integer.parseInt(tupla.y) == 39){
            return this.compare(ctx,types);
        }
        //int token type
        if(Integer.parseInt(tupla.x) == 45 && Integer.parseInt(tupla.y) == 23){
            return this.idLRound(ctx,types);
        }
        if(Integer.parseInt(tupla.x) == 4 && tupla.y.equals("expr")){
            return this.ifExpression(ctx,types);
        }
        if(Integer.parseInt(tupla.x) == 11 && tupla.y.equals("expr")){
            return this.whileExpression(ctx,types);
        }
        if(Integer.parseInt(tupla.x) == 19 && tupla.y.equals("expr")){
            return this.block(ctx,types);
        }
        if(Integer.parseInt(tupla.x) == 7 && tupla.y.equals("expr")){
            return this.isVoid(ctx,types);
        }
        if(Integer.parseInt(tupla.x) == 33 && tupla.y.equals("expr")){
            return this.notInt(ctx,types);
        }
        if(Integer.parseInt(tupla.x) == 13 && tupla.y.equals("expr")){
            return this.notExpr(ctx,types);
        }
        if(Integer.parseInt(tupla.x) == 23 && tupla.y.equals("expr")){
            return this.lroundExpr(ctx,types);
        }

        return "a";
    }


   public String validateFormal(YAPLParser.FormalContext ctx) {
       List<ParseTree> hijo = ctx.children;
       TerminalNode a = (TerminalNode) hijo.get(0);
       TerminalNode b = (TerminalNode) hijo.get(1);
       int aa = a.getSymbol().getType();
       int bb = b.getSymbol().getType();

        if(this.symbolTable.exists(((TerminalNode)ctx.children.get(0)).getText()) && this.symbolTable.exists(ctx.children.get(2).getText())){
            return "CHECK_TYPE";
        }else {
            Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
            Errors.getErrorsInstance().addError(line, "Parametro " + ((TerminalNode)ctx.children.get(0)).getText() + " or type " +((TerminalNode)ctx.children.get(2)).getText()+ " undeclared");
            return "ERROR";
        }
   }


   public String isVoid(YAPLParser.ExprContext ctx, ArrayList<String> types){
        if(!types.get(0).equals("ERROR")){
            return "Bool";
        }else {
            //Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
            //Errors.getErrorsInstance().addError(line, ctx.children[1].getTextI() + " is not compatible with " + types.get(1));
            return "ERROR";
        }
   }


    public String lroundExpr(YAPLParser.ExprContext ctx, ArrayList<String> types){
        return types.get(1);
    }

    //compare
    public String compare(YAPLParser.ExprContext ctx, ArrayList<String> types) {
        if(types.get(0).equals("ERROR") || types.get(2).equals("ERROR")){
            return "ERROR";
        }
        Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());

        if (this.symbolTable.exists(types.get(0)) && this.symbolTable.exists(types.get(2))) {
            if(types.get(0).equals(types.get(2))){
                return "Bool";
            }else{
                String father0 = this.getFather(types.get(0));
                String father2 = this.getFather(types.get(2));
                if(father0.equals(father2) || types.get(0).equals(father2) || types.get(2).equals(father0)) {
                    return "Bool";
                }else {
                    Errors.getErrorsInstance().addError(line, types.get(0) + " no es compatible con " + types.get(2));
                    return "ERROR";
                }
            }
        }else {
            Errors.getErrorsInstance().addError(line, types.get(0) + " or " + types.get(2) + " doesn't exist");
            return "ERROR";
        }
    }


    public String notExpr(YAPLParser.ExprContext ctx, ArrayList<String> types) {
        String condition = Boolean.toString(types.get(1).equals("Bool"));
        if(this.castBool(condition).equals("Boolean")){
            return "Boolean";
        }else{
            Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
            Errors.getErrorsInstance().addError(line, types.get(1) + " is not compatible with  " + "Boolean");
            return "ERROR";
        }
    }

    public String aritmetic(YAPLParser.ExprContext ctx, ArrayList<String> types) {
        if(this.castInt(Boolean.toString(types.get(0).equals("Int"))).equals("Int") && this.castInt(String.valueOf(types.get(2).equals("Int"))).equals("Int")){
            return "Int";
        }else{
            Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
            Errors.getErrorsInstance().addError(line, types.get(0) + " or  " + types.get(2)+" are not Integers");
            return "ERROR";
        }
    }

    public String notInt(YAPLParser.ExprContext ctx, ArrayList<String> types) {
        if(castInt(types.get(1)).equals("Int")){
            return "Int";
        }else {
            Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
            Errors.getErrorsInstance().addError(line, types.get(1) + " is not compatible with Int");
            return "ERROR";
        }
    }

    public String assign(YAPLParser.ExprContext ctx, ArrayList<String> types) {
        if(types.get(0).equals("ERROR") || types.get(2).equals("ERROR")){
            return "ERROR";
        }

        Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
        if(this.symbolTable.exists(ctx.children.get(0).getText()) && this.symbolTable.exists(types.get(2))){
            TableItem idItem = this.symbolTable.get(ctx.children.get(0).getText());

            if(idItem.getTyp().equals(types.get(2))) {
                return types.get(2);
            }else {
                String father2 = this.getFather(types.get(2));

                if(idItem.getTyp().equals(father2)){
                    return types.get(2);
                }else {
                    Errors.getErrorsInstance().addError(line, idItem.getTyp() +  " is not compatible with " + types.get(2));
                    return "ERROR";
                }
            }
        }else {
            Errors.getErrorsInstance().addError(line, ctx.children.get(0).getText() + " or " + types.get(2) + " doesn't exist" );
            return "ERROR";
        }
    }

    public String block(YAPLParser.ExprContext ctx, ArrayList<String> types) {
        for (int i = 1; i < types.size() - 1 ; i+=2) {
            if(types.get(i).equals("ERROR")){
                Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
                Errors.getErrorsInstance().addError(line, "Error in Block");
                return "ERROR";
            }
        }
        return types.get(types.size() -  3);
    }

    public String whileExpression(YAPLParser.ExprContext ctx, ArrayList<String> types) {
        Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());

        if(!this.castBool(types.get(1)).equals("Bool")){
            Errors.getErrorsInstance().addError(line, types.get(1) + "not compatible with Bool");
            return "ERROR";
        }
        if(!this.castBool(types.get(3)).equals("ERROR")){
            return "Object";
        }else {
            Errors.getErrorsInstance().addError(line, "Error in Block");
            return "ERROR";
        }
    }

    public String ifExpression(YAPLParser.ExprContext ctx, ArrayList<String> types) {
        if(Stream.of(types).anyMatch(n -> n.equals("ERROR")) || !this.castBool(types.get(1)).equals("Bool")){
            return "ERROR";
        }
        return "noType";
    }

    public String letExpression (YAPLParser.ExprContext ctx, ArrayList<String> types) {
        List<ParseTree> hijo = ctx.children;
        TerminalNode a = (TerminalNode) hijo.get(0);
        TerminalNode b = (TerminalNode) hijo.get(1);
        int aa = a.getSymbol().getType();
        int bb = b.getSymbol().getType();
        if(Stream.of(types).anyMatch(n -> n.equals("ERROR"))){
            return "ERROR";
        }
        Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
        int i = 1;
        String currentType = "";

        while(!ctx.children.get(i).getText().toLowerCase().equals("in")){
            if(ctx.children.get(1) instanceof YAPLParser.ExprContext){
                if(!types.get(i).equals(currentType)){
                    Errors.getErrorsInstance().addError(line, types.get(i) + "not compatible with " + currentType);
                    return "ERROR";
                }

            }else if(bb == 44){
                if(this.symbolTable.exists(ctx.children.get(i).getText()) && this.symbolTable.exists(ctx.children.get(i + 2).getText())){
                    currentType = this.symbolTable.get(ctx.children.get(i).getText()).getTyp(); //duda
                }else {
                    Errors.getErrorsInstance().addError(line, ctx.children.get(i).getText() + " or " + ctx.children.get(i + 2).getText() + " doesn't exist");
                    return "ERROR";
                }
            }

           i += 1;
        }
        return types.get(types.size() - 1);
    }

    public String idLRound (YAPLParser.ExprContext ctx, ArrayList<String> types) {
        if (Stream.of(types).anyMatch(n -> n.equals("ERROR"))) {
            return "ERROR";
        }

        Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());

        if(this.symbolTable.exists(ctx.children.get(0).getText())){
            TableItem elem = this.symbolTable.get(ctx.children.get(0).getText());
            ArrayList<ParseTree> commas = new ArrayList<>();

            for(ParseTree x : ctx.children){
                if(x instanceof TerminalNodeImpl && ((TerminalNodeImpl) x).symbol.getType() == 24 ){
                    commas.add(x);
                }
            }

            int commasLength = commas.size();
            int params = 0;

            if(commasLength == 0){
                if(ctx.children instanceof TerminalNodeImpl){
                    params = 0;
                }else {
                    params = 1;
                }
            }else {
                params = commasLength + 1;
            }
            if(params != elem.getParam_no()){
                Errors.getErrorsInstance().addError(line, "The number of parameters don't match " +
                        "with the number of parameters of the method "+elem.getLex());
                return "ERROR";
            }
            int tableIndex = 2;

            Table table = this.symbolTable.getTables().get(this.symbolTable.getTableIndex(elem.getLex()));
            //

            for (int i = 0; i < elem.getParam_no()-1; i++) {
                if(table.getItems().get(i).getTyp() != types.get(tableIndex)) {
                    Errors.getErrorsInstance().addError(line, "Type of expression"+ types.get(tableIndex)+
                            "its not expected type for parameter"+table.getItems().get(i).getLex()+":"+table.getItems().get(i).getTyp());
                    return "ERROR";
                }else {
                    tableIndex +=2;
                }
            }
            return elem.getTyp();


        }
        else {
            Errors.getErrorsInstance().addError(line, "method "+ctx.children.get(0).getText()+" doesnt exist");
            return "ERROR";
        }
    }
    public String exprPoint(YAPLParser.ExprContext ctx,  ArrayList<String> types){
        if (Stream.of(types).anyMatch(n -> n.equals("ERROR")))
            return "ERROR";

        Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());

        if(this.symbolTable.exists(types.get(0))){
            int tableIndex = this.symbolTable.getTableIndex(types.get(0));
            boolean idExists = this.symbolTable.existInTable(tableIndex,ctx.children.get(2).getText());
            if(idExists){
                TableItem elem = this.symbolTable.getFromTable(tableIndex,ctx.children.get(2).getText());
                ArrayList<ParseTree> commas = new ArrayList<>();
                int paramCount = 0;

                for(ParseTree x : ctx.children) {
                    if (x instanceof TerminalNodeImpl && ((TerminalNodeImpl) x).symbol.getType() == 24) {
                        commas.add(x);
                    }
                }
                    int commaCount =  commas.size();
                    if(commaCount == 0){
                        if(ctx.children.get(4) instanceof TerminalNodeImpl){
                            paramCount = 0;
                        }else{
                            paramCount = 1;
                        }

                    }else{
                        paramCount = commaCount +1;
                    }
                    if(paramCount != elem.getParam_no()){
                        Errors.getErrorsInstance().addError(line, "the number of parameters doesnt match the number of parameters of method "+elem.getLex());
                        return "ERROR";
                    }
                    Table table = this.symbolTable.getTables().get(this.symbolTable.getTableIndex(elem.getLex()));
                    int indx = 4;

                for (int i = 0; i <elem.getParam_no()-1 ; i++) {
                    if(table.getItems().get(i).getTyp() != types.get(indx)){
                        Errors.getErrorsInstance().addError(line, "the type of expression:"+types.get(indx)+"is not the expected for the parameter "+table.getItems().get(i).getLex()+": "+table.getItems().get(i).getTyp());
                        return "ERROR";
                    }else{
                        indx +=2;
                    }
                }
                return elem.getTyp();
            }else {
                Errors.getErrorsInstance().addError(line, "the method "+ctx.children.get(2).getText()+" doesnt exist");
                return "ERROR";
            }
        }else{
            Errors.getErrorsInstance().addError(line, "Type of expression "+types.get(0)+" doesnt exist");
            return "ERROR";
        }


    }
public String exprArroba(YAPLParser.ExprContext ctx,  ArrayList<String> types){
    if (Stream.of(types).anyMatch(n -> n.equals("ERROR")))
        return "ERROR";

    Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());

    if(this.symbolTable.exists(types.get(0))&& this.symbolTable.exists(ctx.children.get(2).getText())){
        int tableIndex = this.symbolTable.getTableIndex(types.get(0));
        boolean idExists = this.symbolTable.existInTable(tableIndex,ctx.children.get(4).getText());
        if(idExists){
            TableItem elem = this.symbolTable.getFromTable(tableIndex,ctx.children.get(4).getText());
            ArrayList<ParseTree> commas = new ArrayList<>();
            int paramCount = 0;

            for(ParseTree x : ctx.children) {
                if (x instanceof TerminalNodeImpl && ((TerminalNodeImpl) x).symbol.getType() == 24) {
                    commas.add(x);
                }
            }
            int commaCount =  commas.size();
            if(commaCount == 0){
              if(ctx.children.get(6) instanceof TerminalNodeImpl){
                  paramCount = 0;
              }else {
                  paramCount = 1;
              }
            }else{
                paramCount =commaCount + 1;
            }
            if(paramCount != elem.getParam_no()){
                Errors.getErrorsInstance().addError(line, "the number of parameters doesnt match the number of parameters of method "+elem.getLex());
                return "ERROR";
            }
            Table table = this.symbolTable.getTables().get(this.symbolTable.getTableIndex(elem.getLex()));
            int indx = 6;
            for (int i = 0; i <elem.getParam_no()-1 ; i++) {
                if(table.getItems().get(i).getTyp() != types.get(indx)){
                    Errors.getErrorsInstance().addError(line, "the type of expression:"+types.get(indx)+"is not the expected for the parameter "+table.getItems().get(i).getLex()+": "+table.getItems().get(i).getTyp());
                    return "ERROR";
                }else{
                    indx +=2;
                }
            }
            return elem.getTyp();
        }else{
            Errors.getErrorsInstance().addError(line, "the method "+ctx.children.get(2).getText()+" doesnt exist");
            return "ERROR";
        }
    }else{
        Errors.getErrorsInstance().addError(line, "Type of expression "+types.get(0)+" doesnt exist");
        return "ERROR";
    }
}

}
