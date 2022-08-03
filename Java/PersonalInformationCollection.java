import java.util.ArrayList;
import java.util.Scanner;

public class PersonalInformationCollection {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<PersonalInformation> info = new ArrayList<>();

        while (true) {
            System.out.print("First name: ");
            String fName = scanner.nextLine();
            if (fName.isEmpty()) {
                break;
            }

            System.out.print("Last name: ");
            String lName = scanner.nextLine();

            System.out.print("Identification number: ");
            String idNumber = scanner.nextLine();

            info.add(new PersonalInformation(fName, lName, idNumber));
        }

        System.out.println();
        for (PersonalInformation personalInformation : info) {
            System.out.println(personalInformation.getFirstName() + " " + personalInformation.getLastName());
        }
    }
}
