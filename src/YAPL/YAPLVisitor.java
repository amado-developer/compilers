package YAPL;// Generated from C:/Users/massa/Documents/Universidad/quinto a�o/Segundo semestre/Compiladores/P1/untitled/YAPL\YAPL.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link YAPLParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface YAPLVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link YAPLParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(YAPLParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link YAPLParser#class}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClass(YAPLParser.ClassContext ctx);
	/**
	 * Visit a parse tree produced by {@link YAPLParser#feature}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFeature(YAPLParser.FeatureContext ctx);
	/**
	 * Visit a parse tree produced by {@link YAPLParser#formal}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFormal(YAPLParser.FormalContext ctx);
	/**
	 * Visit a parse tree produced by {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr(YAPLParser.ExprContext ctx);
}