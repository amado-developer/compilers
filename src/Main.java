import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import org.antlr.v4.runtime.*;
import YAPL.YAPLLexer;
import YAPL.YAPLParser;
import YAPL.YAPLSintacticErrorListener;

import org.antlr.v4.runtime.misc.Pair;

public class Main {

    public static void main(String[] args) {
        String code = "";
        try{
            File myCode = new File("./pruebas/silly.yapl");
            Scanner scaner = new Scanner(myCode);
            while(scaner.hasNextLine()){
                //String line = scaner.nextLine();
               // System.out.println(line);
                code = code + scaner.nextLine() + "\n";
            }
            scaner.close();
            System.out.println(code);
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
       /// Mensaje texto = new Mensaje()


    }
}