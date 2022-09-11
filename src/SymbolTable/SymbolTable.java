package SymbolTable;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Stream;

public class SymbolTable {

    public static SymbolTable symbolTable;

    public static SymbolTable getSymbolTableInstance(){
        if(symbolTable == null) {
            symbolTable = new SymbolTable();
        }

        return symbolTable;
    }

    @Override
    protected SymbolTable clone() {
        try {
            throw new CloneNotSupportedException();
        } catch (CloneNotSupportedException e){
            e.printStackTrace();
        }
        return null;
    }

    private ArrayList<Table> tables;
    private ArrayList<Integer> scopes;

    private Errors errorMessage = new Errors();

    public int letsCounter;

    private HashMap<String, String> typeOfErrors = new HashMap<>() {{
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

    public Errors getErrorMessage() {
        return errorMessage;
    }

    public  SymbolTable() {
        tables = new ArrayList<>();
        tables.add(new Table("Global"));

        scopes = new ArrayList<>();
        scopes.add(0);

        letsCounter = 0;
        String[] types = {"int", "bool", "object", "string", "io"};

        for (String type : types){
            switch (type){
                case "int":
                    addType("Int", 43, new Tuple<>(0, 0),
                            "", "class", "", 0, 0,
                            "");
                    break;
                case "bool":
                    addType("Bool", 43, new Tuple<>(0, 0),
                            "value", "class", "", 0, 0,
                            "");
                    break;
                case "object":
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
                    break;
                case "string":
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

                    break;
                case "io":
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

                    break;
                default: break;
            }
        }

    }

    public void checkMainMethod(){
        int mainTableIndex = this.getTableIndex("Main");
    }
    public boolean checkMainExistence(){
        if(Stream.of(this.tables.get(0).getItems()).anyMatch(n -> n.stream().anyMatch(x->x.getLex().equals("Main")&& x.getInherits().equals("")))){
            return true;
        }
        return false;
    }

    public void pushToScope(String scope) {
        this.tables.add(new Table(scope));
        this.scopes.add(this.tables.size() - 1);
    }

    public boolean addType(String lex, int token, Tuple<Integer, Integer> line,
                        String paramMethod, String semKind, String type,
                        int param_no, int pos_mem, String inherits){

        return insert(new TableItem(lex, token, line, semKind, paramMethod,
                type, param_no, pos_mem, inherits));

    }

    public boolean insert(TableItem item) {
        for(TableItem table : this.tables.get(
                this.scopes.get(this.scopes.size() - 1)).items) {
            if(!item.lex.equals(table.lex) || !item.sem_kind.equals(table.sem_kind)) {
                this.tables.get(this.scopes.get(this.scopes.size() - 1)).items.add(item);
                return false;
            } else {
                errorMessage.addMessage(table.linea,
                        typeOfErrors.get(table.sem_kind) + ' '
                                + table.lex + " has already been declared", "error");
                return true;
            }
        }
        return true;
    }

    public TableItem get(String name) {
        for (int i = this.scopes.size() - 1; i >= 0; i--) {
            for(TableItem row : this.tables.get(this.scopes.get(i)).items){
                if(row.lex.equals(name)){
                    return row;
                }
            }
        }
        return null;
    }
    public int getTableIndex(String scope){
        for (int i = 0; i < tables.size()-1; i++) {
            if(tables.get(i).name==scope){
                return i;
            }

        }
        return 0;
    }

    public boolean existInTable(int index, String name){
        for(TableItem row: this.tables.get(index).getItems()){
            if (row.getLex().equals(name)){
                return true;
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
    public Boolean exists(String name) {
        for (int i = this.scopes.size() - 1; i >= 0; i--) {
            for(TableItem row : this.tables.get(this.scopes.get(i)).items){
                if(row.lex.equals(name)){
                    return true;
                }
            }
        }
        return false;
    }
}
