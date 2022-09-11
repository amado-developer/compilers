package YAPL;// Generated from C:/Users/massa/Documents/Universidad/quinto a�o/Segundo semestre/Compiladores/P1/untitled/YAPL\YAPL.g4 by ANTLR 4.10.1
import SymbolTable.TableItem;
import org.antlr.v4.runtime.tree.AbstractParseTreeVisitor;
import SymbolTable.*;

import java.security.MessageDigest;

/**
 * This class provides an empty implementation of {@link YAPLVisitor},
 * which can be extended to create a visitor which only needs to handle a subset
 * of the available methods.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public class YAPLBaseVisitor<T> extends AbstractParseTreeVisitor<T> implements YAPLVisitor<T> {
	SymbolTable symbol_table = new SymbolTable();
	Operations tableOperations = new Operations();

	public int getClassTotalSize(String name){
		for(TableItem symbol:symbol_table.getTables().get(0).getItems()){
			if(symbol.getLex().equals(name)){
				return symbol.getByteSize();
			}
		}
		return 0;
	}
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation returns the result of calling
	 * {@link #visitChildren} on {@code ctx}.</p>
	 */
	@Override public T visitProgram(YAPLParser.ProgramContext ctx) {

		this.visitChildren(ctx);
		this.symbol_table()
		return visitChildren(ctx);
	}


	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation returns the result of calling
	 * {@link #visitChildren} on {@code ctx}.</p>
	 */

	@Override public T visitClass(YAPLParser.ClassContext ctx) { return visitChildren(ctx); }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation returns the result of calling
	 * {@link #visitChildren} on {@code ctx}.</p>
	 */
	@Override public T visitFeature(YAPLParser.FeatureContext ctx) { return visitChildren(ctx); }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation returns the result of calling
	 * {@link #visitChildren} on {@code ctx}.</p>
	 */
	@Override public T visitFormal(YAPLParser.FormalContext ctx) { return visitChildren(ctx); }
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation returns the result of calling
	 * {@link #visitChildren} on {@code ctx}.</p>
	 */
	@Override public T visitExpr(YAPLParser.ExprContext ctx) { return visitChildren(ctx); }
}