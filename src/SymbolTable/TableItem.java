package SymbolTable;

public class TableItem {
    String lex;
    int token;
    Tuple<Integer, Integer> linea;
    String sem_kind;

    int byteSize;
    String param_method;
    String type;
    int param_no;
    int pos_mem;
    String inherits;

    public TableItem(String lex, int token, Tuple<Integer, Integer> linea,
                     String sem_kind,int byteSize, String param_method, String type,
                     int param_no, int pos_mem, String inherits) {
        this.lex = lex;
        this.token = token;
        this.linea = linea;
        this.sem_kind = sem_kind;
        this.byteSize = byteSize;
        this.param_method = param_method;
        this.type = type;
        this.param_no = param_no;
        this.pos_mem = pos_mem;
        this.inherits = inherits;
    }


    public String getLex() {
        return lex;
    }

    public void setLex(String lex) {
        this.lex = lex;
    }

    public int getToken() {
        return token;
    }

    public void setToken(int token) {
        this.token = token;
    }

    public Tuple<Integer, Integer> getLinea() {
        return linea;
    }

    public void setLinea(Tuple<Integer, Integer> linea) {
        this.linea = linea;
    }

    public String getSem_kind() {
        return sem_kind;
    }

    public void setSem_kind(String sem_kind) {
        this.sem_kind = sem_kind;
    }

    public int getByteSize(){return byteSize;}

    public void setByteSize(){this.byteSize = byteSize;}

    public String getParam_method() {
        return param_method;
    }

    public void setParam_method(String param_method) {
        this.param_method = param_method;
    }

    public String getTyp() {
        return type;
    }

    public void setTyp(String typ) {
        this.type = typ;
    }

    public int getParam_no() {
        return param_no;
    }

    public void setParam_no(int param_no) {
        this.param_no = param_no;
    }

    public int getPos_mem() {
        return pos_mem;
    }

    public void setPos_mem(int pos_mem) {
        this.pos_mem = pos_mem;
    }

    public String getInherits() {
        return inherits;
    }

    public void setInherits(String inherits) {
        this.inherits = inherits;
    }
}
