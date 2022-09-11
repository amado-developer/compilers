package SymbolTable;

public class Error {
    private String type;
    private String errorMessage;

    public Error(String type, String errorMessage) {
        this.type = type;
        this.errorMessage = errorMessage;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getErrorMessage() {
        return errorMessage;
    }

    public void setErrorMessage(String errorMessage) {
        this.errorMessage = errorMessage;
    }
}
