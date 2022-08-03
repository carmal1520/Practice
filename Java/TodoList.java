import java.util.ArrayList;

public class TodoList {
    private final ArrayList<String> list;

    public TodoList() {
        this.list = new ArrayList<>();
    }

    public void add(String task) {
        list.add(task);
    }

    public void print() {
        for (String task : list) {
            System.out.println(list.indexOf(task) + 1 + ":" + " " + task);
        }
    }

    public void remove(int number) {
        list.remove(number - 1);0
    }
}
