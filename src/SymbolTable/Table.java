package SymbolTable;

import java.util.ArrayList;

public class Table {

    String name;
    ArrayList<TableItem> items;
    public Table(String name) {
        name = "";
        items = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ArrayList<TableItem> getItems() {
        return items;
    }

    public void setItems(ArrayList<TableItem> items) {
        this.items = items;
    }
}