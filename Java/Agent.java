public class Agent {
    String firstName;
    String lastName;

    public Agent(String fName, String lName) {
        this.firstName = fName;
        this.lastName = lName;
    }

    @Override
    public String toString() {
        return "My name is " + this.lastName + ", " + this.firstName + " " + this.lastName;
    }
}
