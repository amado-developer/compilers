package SymbolTable;

import YAPL.YAPLUtils;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Stream;

public class SymbolTable {

    public static SymbolTable symbolTable;

    public int getMemoryCounter() {
        return memoryCounter;
    }

    public void setMemoryCounter(int memoryCounter) {
        this.memoryCounter = memoryCounter;
    }

    private int memoryCounter;

    public static SymbolTable getSymbolTableInstance(){
        if(symbolTable == null) {
            symbolTable = new SymbolTable();
        }

        return symbolTable;
    }

    @Override
    protected SymbolTable clone() throws CloneNotSupportedException {
        SymbolTable clone = (SymbolTable) super.clone();
        try {
            throw new CloneNotSupportedException();
        } catch (CloneNotSupportedException e){
            e.printStackTrace();
        }
        return null;
    }

    private ArrayList<Table> tables;
    public ArrayList<Integer> scopes;

    public int letsCounter;

    private final HashMap<String, String> typeOfErrors = new HashMap<>() {{
        put("ATTR", "Variable");
        put("METHOD", "Method");
        put("PARAMETER", "Parameter");
        put("CLASS", "Class");
    }};

    public ArrayList<Table> getTables() {
        return tables;
    }

    public ArrayList<Integer> getScopes() {
        return scopes;
    }


    public  SymbolTable() {
        tables = new ArrayList<>();
        tables.add(new Table("Global"));

        scopes = new ArrayList<>();
        scopes.add(0);

        letsCounter = 0;
        String[] types = {"int", "bool", "object", "string", "io"};

        for (String type : types){
            switch (type) {
                case "int" -> addType("Int", 43, new Tuple<>(0, 0),
                        "", "class", "", 0, 0,
                        "");
                case "bool" -> addType("Bool", 43, new Tuple<>(0, 0),
                        "value", "class", "", 0, 0,
                        "");
                case "object" -> {
                    addType("Object", 43, new Tuple<>(0, 0),
                            "value", "class", "", 0, 0,
                            "");
                    pushToScope("Object");
                    addType("abort", 44, new Tuple<>(0, 0),
                            "value", "method", "Object", 0, 0,
                            "");
                    addType("type_name", 44, new Tuple<>(0, 0),
                            "value", "method", "String", 0, 0,
                            "");
                    addType("copy", 44, new Tuple<>(0, 0),
                            "value", "method", "Object", 0, 0,
                            "");
                    this.scopes.remove(this.scopes.size() - 1);
                }
                case "string" -> {
                    addType("String", 43, new Tuple<>(0, 0),
                            "value", "class", "", 0, 0,
                            "");
                    pushToScope("String");
                    addType("length", 44, new Tuple<>(0, 0),
                            "value", "method", "Int", 0, 0,
                            "");
                    pushToScope("length");
                    this.scopes.remove(this.scopes.size() - 1);
                    addType("concat", 44, new Tuple<>(0, 0),
                            "value", "method", "String", 1, 0,
                            "");
                    pushToScope("concat");
                    addType("s", 44, new Tuple<>(0, 0),
                            "value", "parameter", "String", 0, 0,
                            "");
                    this.scopes.remove(this.scopes.size() - 1);
                    addType("substr", 44, new Tuple<>(0, 0),
                            "value", "method", "String", 2, 0,
                            "");
                    this.pushToScope("substr");
                    addType("i", 44, new Tuple<>(0, 0),
                            "value", "parameter", "Int", 0, 0,
                            "");
                    addType("l", 44, new Tuple<>(0, 0),
                            "value", "parameter", "Int", 0, 0,
                            "");
                    this.scopes.remove(this.scopes.size() - 1);
                    this.scopes.remove(this.scopes.size() - 1);
                }
                case "io" -> {
                    addType("IO", 43, new Tuple<>(0, 0),
                            "value", "class", "", 0, 0,
                            "");
                    pushToScope("IO");
                    addType("out_string", 44, new Tuple<>(0, 0),
                            "value", "method", "IO", 1, 0,
                            "");
                    pushToScope("out_string");
                    addType("x", 44, new Tuple<>(0, 0),
                            "value", "parameter", "String", 0, 0,
                            "");
                    this.scopes.remove(this.scopes.size() - 1);
                    addType("out_int", 44, new Tuple<>(0, 0),
                            "value", "method", "IO", 1, 0,
                            "");
                    pushToScope("out_int");
                    addType("x", 44, new Tuple<>(0, 0),
                            "value", "parameter", "Int", 0, 0,
                            "");
                    this.scopes.remove(this.scopes.size() - 1);
                    addType("in_string", 44, new Tuple<>(0, 0),
                            "value", "method", "String", 0, 0,
                            "");
                    pushToScope("in_string");
                    this.scopes.remove(this.scopes.size() - 1);
                    addType("in_int", 44, new Tuple<>(0, 0),
                            "value", "method", "Int", 0, 0,
                            "");
                    pushToScope("in_int");
                    this.scopes.remove(this.scopes.size() - 1);
                    this.scopes.remove(this.scopes.size() - 1);
                }
                default -> {
                }
            }
        }

    }



    public void checkMain(){
        if(this.checkMainExistence()){
            ArrayList<String> lexers = new ArrayList<>();

            for (TableItem item:this.tables.get(0).getItems()) {
                lexers.add(item.getLex());
            }
            int mainIndex = YAPLUtils.indx(lexers,"Main");
            Tuple<Integer,Integer> mainLine = this.tables.get(0).getItems().get(mainIndex).getLinea();
            this.checkMainMethod(mainLine);
        }else{
            Errors.getErrorsInstance().addError(new Tuple<Integer, Integer>(0,0),
                    " Main class doesn't exist or it's being inherited from another class");
        }
    }
    public void checkMainMethod(Tuple<Integer,Integer> line){
        int mainTableIndex = this.getTableIndex("Main");
        ArrayList<String> lexers = new ArrayList<>();
        for (TableItem item:this.tables.get(0).getItems()) {
            lexers.add(item.getLex());
        }
        int mainIndex = YAPLUtils.indx(lexers,"Main");
        if(mainIndex < 0){
            Errors.getErrorsInstance().addError(line,"method has not be declared");
        }else{
            TableItem mainM = this.tables.get(mainTableIndex).getItems().get(mainIndex);
            if(mainM.getParam_no()>0){
                Errors.getErrorsInstance().addError(line,"Main method must not have parameters");
            }
        }
    }
    public boolean checkMainExistence(){
        return Stream.of(this.tables.get(0).getItems())
                .anyMatch(n -> n.stream().anyMatch(x -> x.getLex().equals("Main")
                        && x.getInherits().equals("")));
    }

    public boolean addType(String lex, int token, Tuple<Integer, Integer> line,
                        String paramMethod, String semKind, String type,
                        int param_no, int pos_mem, String inherits){

        return insert(new TableItem(lex, token, line, semKind,0, paramMethod,
                type, param_no, pos_mem, inherits));
    }

    public void pushToScope(String scope) {
        this.tables.add(new Table(scope));
        this.scopes.add(this.tables.size() - 1);
    }

    //TODO remove this later
    public void popScope(){
        this.scopes.remove(this.scopes.size() - 1);
    }

    public void enterScope(String scope){
        this.scopes.add(this.getTableIndex(scope));
    }

    public void exitScope(){
        this.scopes.remove(this.scopes.size()-1);
    }

    public int getTableIndex(String scope){
        for (int i = 0; i < tables.size()-1; i++) {
            if(tables.get(i).getName().equals(scope)){
                return i;
            }
        }
        return 0;
    }

    public boolean insert(TableItem item) {
        int cs = currentScope();
        for(TableItem table : this.tables.get(currentScope()).items) {
            if(!item.lex.equals(table.lex) || !item.sem_kind.equals(table.sem_kind)) {
                this.tables.get(this.scopes.get(this.scopes.size() - 1)).items.add(item);
                return false;
            } else {
                Errors.getErrorsInstance().addMessage(table.linea,
                        typeOfErrors.get(table.sem_kind) + " "
                                + table.lex + " has already been declared", "error");
                return true;
            }
        }

        if(this.tables.get(currentScope()).items.size() == 0){
            this.tables.get(currentScope()).items.add(item);
        }
        return true;
    }

    public TableItem get(String name) {
        for (int i = this.scopes.size() - 1; i >= 0; i--) {
            for(TableItem row : this.tables.get(this.scopes.get(i)).getItems()){
                if(row.lex.equals(name)){
                    return row;
                }
            }
        }
        return null;
    }
    public Boolean exists(String name) {
        for (int i = this.scopes.size() - 1; i >= 0; i--) {
            for(TableItem row : this.tables.get(this.scopes.get(i)).getItems()){
                if(row.lex.equals(name)){
                    return true;
                }
            }
        }
        return false;
    }



    public TableItem getFromTable(int index, String name){
        for(TableItem row: this.tables.get(index).getItems()){
            if (row.getLex().equals(name)){
                return row;
            }
        }
        return null;
    }

    public boolean existInTable(int index, String name){
        for(TableItem row: this.tables.get(index).getItems()){
            if (row.getLex().equals(name)){
                return true;
            }
        }
        return false;
    }

    public Integer currentScope(){
        return this.scopes.get(this.scopes.size() - 1);
    }


    public void updateMemPosition(int index){
        for(TableItem tableItem : this.tables.get(index).getItems()){
            index = this.getTableIndex(tableItem.getLex());

            if(index != -1){
                this.updateMemPosition(index);
            }

            if(tableItem.getSem_kind().equals("attr")
                    || tableItem.getSem_kind().equals("parameter")
                    || tableItem.getSem_kind().equals("obj")){
                tableItem.pos_mem = this.allocateMemPos(tableItem.getByteSize());

            }
        }
    }

    public int allocateMemPos(int byteSize) {
        this.memoryCounter += byteSize;
        return this.memoryCounter - byteSize;
    }


    public boolean addByteSize(int i, String name, int sum) {
        for(TableItem row: this.tables.get(i).getItems()){
            if(row.getLex().equals(name)){
                row.byteSize += sum;
                return true;
            }
        }
        return false;
    }
}
