package SymbolTable;

import java.util.ArrayList;

public class Errors {

    private static Errors errorsInstance;

    public static Errors getSymbolTableInstance(){
        if(errorsInstance == null) {
            errorsInstance = new Errors();
        }

        return errorsInstance;
    }

    @Override
    protected Errors clone() {
        try {
            throw new CloneNotSupportedException();
        } catch (CloneNotSupportedException e){
            e.printStackTrace();
        }
        return null;
    }

    private ArrayList<Error> errors = new ArrayList<>();
    private boolean isError = false;

    public ArrayList<Error> getErrors() {
        return errors;
    }

    public static Errors getErrorsInstance() {
        return errorsInstance;
    }

    public void setError(boolean error) {
        isError = error;
    }

    public void setErrors(ArrayList<Error> errors) {
        this.errors = errors;
    }

    public void addError(Tuple<Integer, Integer> line, String errorMessage) {
        this.isError = true;
        this.errors.add(new Error("error", "Line " + line.getX()
                + " : " + line.getY()  + "has encountered error: " + errorMessage));
    }

    public void addMessage(Tuple<Integer, Integer> line, String errorMessage, String type){
        if(type.equals("error")){
            this.isError = true;
        }

        if(type.equals("success")){
            this.errors.add(new Error(type, errorMessage));

        }else {
            this.errors.add(new Error(type, "Line " + line.getX()
                    + " : " + line.getY()  + "has encountered :" + type + ""+ errorMessage));
        }
    }

    public void deleteErrors() {
        this.errors.clear();
    }
}
