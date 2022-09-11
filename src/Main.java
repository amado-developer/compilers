import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import SymbolTable.Error;
import SymbolTable.Errors;
import YAPL.*;
import org.antlr.v4.runtime.*;

import org.antlr.v4.runtime.misc.Pair;

public class Main {

    public static void main(String[] args) {
        String code = "";
        try{
            File myCode = new File("./pruebas/silly.yapl");
            Scanner scaner = new Scanner(myCode);
            while(scaner.hasNextLine()){
                code = code + scaner.nextLine() + "\n";
            }
            scaner.close();
//            System.out.println(code);
        }catch (FileNotFoundException e){
            System.out.println("ERROR");
            e.printStackTrace();
        }
        ANTLRInputStream input = new ANTLRInputStream(code);
        YAPLLexer lexer = new YAPLLexer(input);
        CommonTokenStream tokens  = new CommonTokenStream(lexer);
        YAPLParser parser = new YAPLParser(tokens);
        parser.removeErrorListeners();
        parser.addErrorListener(YAPLSintacticErrorListener.INSTANCE);
        YAPLParser.ProgramContext tree = parser.program();

        if(!Errors.getErrorsInstance().isError){
            Errors.getErrorsInstance().addCompleted("All good man!");
            YAPLBaseVisitor a = new YAPLBaseVisitor();
            YAPLCustomVisitor IronMaiden = new YAPLCustomVisitor<>();
            String answer = (String) a.visit(tree);

            if(answer.equals("checkType")){
                Errors.getErrorsInstance().addCompleted("Type insertion worked!");
            }
            if(!Errors.getErrorsInstance().isError){
                String answer2 = (String) IronMaiden.visit(tree);
                if(answer2.equals("checkType")){
                    Errors.getErrorsInstance().addCompleted("SIUUUU!");
                }
            }
        }
        for(Error message : Errors.getErrorsInstance().getErrors()){
            System.out.println(message.getErrorMessage());
        }
    }
}