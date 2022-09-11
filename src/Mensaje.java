public class Mensaje {
    String type;
    String msg;
    String color;


    public Mensaje(String type, String msg, String color){
        this.type = type;
        this.msg = msg;
        this.color = color;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}
