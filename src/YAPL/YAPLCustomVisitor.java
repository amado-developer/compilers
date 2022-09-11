package YAPL;
import org.antlr.v4.runtime.*;
import TypeSystem.Types;
import SymbolTable.*;
import org.antlr.v4.runtime.tree.AbstractParseTreeVisitor;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.TerminalNode;
import org.antlr.v4.runtime.tree.TerminalNodeImpl;

import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class YAPLCustomVisitor<T> extends AbstractParseTreeVisitor<T> implements YAPLVisitor<T>{

    int analizedLets;
    Types typesSys;
    public YAPLCustomVisitor() {
        typesSys = new Types();
        analizedLets = 0;
    }

   public String getType(YAPLParser.ExprContext child){
        return typesSys.getBaseCaseType(child);

    }

    public  ArrayList<Boolean> evaluateTerminalChildren(List<T> nodes){
        ArrayList<Boolean> terminalChildren = new ArrayList<>();

        for(T node:nodes){
            terminalChildren.add((node instanceof TerminalNodeImpl));
        }
        return terminalChildren;
    }
    public ArrayList<String> visitChildren(YAPLParser.ProgramContext ctx, ArrayList<Boolean> res){
        ArrayList<String> resTypes = new ArrayList<>();
        for (int i = 0; i < ctx.children.size()-1; i++) {
            if(!res.get(i)){
                resTypes.add((String)ctx.accept(this));
            }else{
                resTypes.add("");
            }
        }
        return resTypes;
        
    }
    public ArrayList<String> visitChildren(YAPLParser.FeatureContext ctx, ArrayList<Boolean> res){
        ArrayList<String> resTypes = new ArrayList<>();
        for (int i = 0; i < ctx.children.size()-1; i++) {
            if(!res.get(i)){
                resTypes.add((String)ctx.accept(this));
            }else{
                resTypes.add("");
            }
        }
        return resTypes;

    }
    public ArrayList<String> visitChildren(YAPLParser.ExprContext ctx, ArrayList<Boolean> res){
        ArrayList<String> resTypes = new ArrayList<>();
        for (int i = 0; i < ctx.children.size()-1; i++) {
            if(!res.get(i)){
                resTypes.add((String)ctx.accept(this));
            }else{
                resTypes.add("");
            }
        }
        return resTypes;

    }
    public ArrayList<String> visitChildren(YAPLParser.ClassContext ctx, ArrayList<Boolean> res){
        ArrayList<String> resTypes = new ArrayList<>();
        for (int i = 0; i < ctx.children.size()-1; i++) {
            if(!res.get(i)){
                resTypes.add((String)ctx.accept(this));
            }else{
                resTypes.add("");
            }
        }
        return resTypes;

    }
    @Override
    public T visitProgram(YAPLParser.ProgramContext ctx) {
       // ArrayList<Boolean> res = YAPLUtils.evaluateTerminalChildren(ctx.children);
         ArrayList<Boolean> res = evaluateTerminalChildren((List<T>) ctx.children);
        System.out.println("dont ever say its over if im breathing 1");
        ArrayList<String> typs = this.visitChildren(ctx,res);
        for (String a:typs
             ) {
            System.out.println(a);
        }
        if(YAPLUtils.someErrorType(typs)){
            System.out.println("dont ever say its over if im breathing");
            Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
            Errors.getErrorsInstance()
                    .addError(line,
                            "Can't start the program due errors:" +
                                    " " + ctx.getText());
            return (T)"ERROR";
        }
        return (T)"checkType";
    }

    @Override
    public T visitClass(YAPLParser.ClassContext ctx) {
        if(Errors.getErrorsInstance().isError){
            return (T) "ERROR";
        }

        //ArrayList<Boolean> res = YAPLUtils.evaluateTerminalChildren(ctx.children);
        ArrayList<Boolean> res = evaluateTerminalChildren((List<T>) ctx.children);
        boolean classExists =   SymbolTable.getSymbolTableInstance().exists(ctx.children.get(1).getText());
        if(classExists){
              SymbolTable.getSymbolTableInstance().enterScope(ctx.children.get(1).getText());
            ArrayList<String> typs = this.visitChildren(ctx,res);

            if(YAPLUtils.someErrorType(typs)){
                Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
                Errors.getErrorsInstance()
                        .addError(line,
                                "Can't start the program due errors:" +
                                        " " + ctx.getText());
                return (T)"ERROR";
            }
              SymbolTable.getSymbolTableInstance().exitScope();

            return (T)"checkType";
        }else{
            Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
            Errors.getErrorsInstance()
                    .addError(line,
                            "Class " + ctx.children.get(1).getText() +
                                    " doesn't exist");
            return (T)"ERROR";
        }


    }

    @Override
    public T visitFeature(YAPLParser.FeatureContext ctx) {
        if(Errors.getErrorsInstance().isError){
            return (T) "ERROR";
        }

        //ArrayList<Boolean> res = YAPLUtils.evaluateTerminalChildren(ctx.children);
        ArrayList<Boolean> res = evaluateTerminalChildren((List<T>) ctx.children);
        boolean featureExists =   SymbolTable.getSymbolTableInstance().exists(ctx.children.get(0).getText());
        ArrayList<String> typs;
        if(featureExists){
            TableItem feature =   SymbolTable.getSymbolTableInstance().get(ctx.children.get(0).getText());

            if(feature.getSem_kind().equals("method")){
                  SymbolTable.getSymbolTableInstance().enterScope(ctx.children.get(0).getText());
            }
            typs = this.visitChildren(ctx,res);

            if(YAPLUtils.someErrorType(typs)){
                Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
                Errors.getErrorsInstance()
                        .addError(line,
                                "Can't start the program due errors:" +
                                        " " + ctx.getText());
                return (T)"ERROR";
            }
            String validation = typesSys.validateFeature(ctx, typs);

            if(feature.getSem_kind().equals("method")){
                  SymbolTable.getSymbolTableInstance().exitScope();
            }
            return (T)validation;
        }else{
            Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
            Errors.getErrorsInstance()
                    .addError(line,
                            "Attribute " + ctx.children.get(0).getText()+ " doeesn't exist");
            return (T)"ERROR";
        }


    }

    @Override
    public T visitFormal(YAPLParser.FormalContext ctx) {
        if(Errors.getErrorsInstance().isError){
            return (T) "ERROR";
        }

        return (T)typesSys.validateFormal(ctx);
    }

    @Override
    public T visitExpr(YAPLParser.ExprContext ctx) {
        if(Errors.getErrorsInstance().isError){
            return (T) "ERROR";
        }

        //ArrayList<Boolean> res = YAPLUtils.evaluateTerminalChildren(ctx.children);
        ArrayList<Boolean> res = evaluateTerminalChildren((List<T>) ctx.children);
        ArrayList<String> typs;

        if(!Arrays.asList(res).contains(false)){
            return (T)this.getType(ctx);
        }else{
            if(ctx.children.get(0).getText().toLowerCase().equals("let")){
                boolean letExists =   SymbolTable.getSymbolTableInstance().exists("let"+this.analizedLets);
                if(letExists) {
                      SymbolTable.getSymbolTableInstance().enterScope("let" + this.analizedLets);
                }else{
                    Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
                    Errors.getErrorsInstance().addError(line,"Let doesn't exist");
                    return (T)"ERROR";
                }
            }
            typs = this.visitChildren(ctx, res);

            if(YAPLUtils.someErrorType(typs)){
                Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
                Errors.getErrorsInstance()
                        .addError(line,
                                "Can't start the program due errors: " +
                                        " " + ctx.getText());
                return (T)"ERROR";
            }

            if(ctx.children.get(0).getText().equalsIgnoreCase("let")){
                  SymbolTable.getSymbolTableInstance().exitScope();
                this.analizedLets +=1;
            }
           // return (T) this.visitChildren(ctx, res);
            return  (T)typesSys.validateExpr(ctx, typs, res);
        }


    }
}

