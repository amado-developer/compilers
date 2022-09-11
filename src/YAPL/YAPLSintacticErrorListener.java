package YAPL;
import org.antlr.v4.runtime.*;
public class YAPLSintacticErrorListener extends BaseErrorListener {
    public static final YAPLSintacticErrorListener INSTANCE = new YAPLSintacticErrorListener();

    @Override
    public void syntaxError(Recognizer<?, ?> recognizer, Object offendingSymbol, int line, int charPositionInLine, String msg, RecognitionException e){
        System.out.println("Error en linea: " + line + ":" + charPositionInLine + " " + msg);
    }

}
