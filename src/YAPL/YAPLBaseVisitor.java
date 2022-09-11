package YAPL;// Generated from C:/Users/massa/Documents/Universidad/quinto a�o/Segundo semestre/Compiladores/P1/untitled/YAPL\YAPL.g4 by ANTLR 4.10.1
import SymbolTable.TableItem;
import org.antlr.v4.runtime.tree.AbstractParseTreeVisitor;
import SymbolTable.*;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.TerminalNode;

import java.security.MessageDigest;
import java.util.ArrayList;
import java.util.List;

/**
 * This class provides an empty implementation of {@link YAPLVisitor},
 * which can be extended to create a visitor which only needs to handle a subset
 * of the available methods.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public class YAPLBaseVisitor<T> extends AbstractParseTreeVisitor<T> implements YAPLVisitor<T> {
	Operations tableOperations = new Operations();

	public int getClassTotalSize(String name){
		for(TableItem symbol:  SymbolTable.getSymbolTableInstance().getTables().get(0).getItems()){
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
		SymbolTable.getSymbolTableInstance().checkMain();
//		SymbolTable.getSymbolTableInstance().updateMemPosition(0);
//		System.out.println("Symbol Table: ");
//		for(Table table :  SymbolTable.getSymbolTableInstance().getTables()){
//			for(TableItem tableItem: table.getItems()){
//				System.out.println(tableItem.getLex());
//			}
//		}

//		return visitChildren(ctx); P2
		return (T) "checkType"; // P1
	}


	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation returns the result of calling
	 * {@link #visitChildren} on {@code ctx}.</p>
	 */

	@Override public T visitClass(YAPLParser.ClassContext ctx) {
		if(Errors.getErrorsInstance().isError){
			return (T) "ERROR";
		}

		boolean inserted = this.tableOperations.insertClass(ctx);

		if(inserted){
			SymbolTable.getSymbolTableInstance().pushToScope(ctx.children.get(1).getText());
			Tuple<Integer, Integer> line = new Tuple<>(ctx.start.getLine(), ctx.start.getCharPositionInLine());
			this.tableOperations.insertSelf(line);
			this.visitChildren(ctx);

			Table currentTable =   SymbolTable.getSymbolTableInstance().getTables().get(  SymbolTable.getSymbolTableInstance().getScopes()
					.get(  SymbolTable.getSymbolTableInstance().getScopes().size() -1));

			ArrayList<Integer> byteSizes = new ArrayList<>();

			for(TableItem tableItem : currentTable.getItems()){
				if(tableItem.getTyp().equals(currentTable.getName())){
					byteSizes.add(tableItem.getByteSize());
				}else{
					byteSizes.add(0);
				}
			}

			  SymbolTable.getSymbolTableInstance().addByteSize(0, currentTable.getName(), byteSizes.stream().mapToInt(a -> a).sum());
			int byteSize = this.getClassTotalSize(currentTable.getName());

			for(TableItem tableItem :   SymbolTable.getSymbolTableInstance().getTables()
					.get(  SymbolTable.getSymbolTableInstance().getScopes().get(  SymbolTable.getSymbolTableInstance().getScopes().size() - 1)).getItems()){
				if(tableItem.getTyp().equals(currentTable.getName())){
					tableItem.setByteSize(byteSize);
				}
			}

			  SymbolTable.getSymbolTableInstance().scopes.remove(  SymbolTable.getSymbolTableInstance().scopes.size() - 1);
		}
		return visitChildren(ctx);
	}
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation returns the result of calling
	 * {@link #visitChildren} on {@code ctx}.</p>
	 */
	@Override public T visitFeature(YAPLParser.FeatureContext ctx) {
		if(Errors.getErrorsInstance().isError){
			return (T) "ERROR";
		}

		boolean inserted = this.tableOperations.insertFeature(ctx);

		if(inserted){
			if(!ctx.children.get(1).getText().equals(":")){
				  SymbolTable.getSymbolTableInstance().pushToScope(ctx.children.get(0).getText());
			}

			this.visitChildren(ctx);

			if(!ctx.children.get(1).getText().equals(":")) {
				  SymbolTable.getSymbolTableInstance().scopes.remove(  SymbolTable.getSymbolTableInstance().scopes.size() - 1);
			}
		}
		return visitChildren(ctx);
	}
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation returns the result of calling
	 * {@link #visitChildren} on {@code ctx}.</p>
	 */
	//TODO VERIFICAR NOTS
	@Override public T visitFormal(YAPLParser.FormalContext ctx) {
		if(Errors.getErrorsInstance().isError){
			return (T) "ERROR";
		}

		this.tableOperations.insertFormal(ctx);
		return visitChildren(ctx);
	}
	/**
	 * {@inheritDoc}
	 *
	 * <p>The default implementation returns the result of calling
	 * {@link #visitChildren} on {@code ctx}.</p>
	 */
	@Override public T visitExpr(YAPLParser.ExprContext ctx) {
		if(Errors.getErrorsInstance().isError){
			return (T) "ERROR";
		}

		if(ctx.children.size() == 0){
			return null;
		}

		List<TerminalNode> a = ctx.TYPE();
		int type = 0;

		if(a.size() > 0){
			type = a.get(0).getSymbol().getType();
		}else {
			visitChildren(ctx);
		}

		if(ctx.children.get(0).getText().toLowerCase().equals("let")){
			if(this.tableOperations.insertExpr(ctx)){
				visitChildren(ctx);
			}
		}/*else if(YAPLUtils.isTerminalNode(ctx.children.get(0)) && type == 12){
//			this.tableOperations.insertObj(ctx);
		}else {
			visitChildren(ctx);
		}*/
		return visitChildren(ctx);
	}
}