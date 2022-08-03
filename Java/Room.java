import java.util.ArrayList;

public class Room {
    private final ArrayList<Person> persons = new ArrayList<>();

    public void add(Person person) {
        this.persons.add(person);
    }

    public boolean isEmpty() {
        return persons.isEmpty();
    }

    public ArrayList<Person> getPersons() {
        return persons;
    }

    public Person shortest() {
        if (isEmpty()) {
            return null;
        }

        Person shortestPerson = new Person("", Integer.MAX_VALUE);
//    }
        return shortestPerson;
    }
}








//    private String code;
//    private int seats;
//
//    public Room(String classCode, int numberOfSeats) {
//        this.code = classCode;
//        this.seats = numberOfSeats;