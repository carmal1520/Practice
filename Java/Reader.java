import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Reader {
    public static void main(String[] args) throws IOException {
        System.out.println("Which file should have its contents printed?");
        Scanner scanner = new Scanner(System.in);
        String fileName = scanner.nextLine();

        BufferedReader x = new BufferedReader(new FileReader(fileName));
        String str;
        while ((str = x.readLine()) != null) {
            System.out.println(str);
        }
    }
}
//
//    ArrayList<String> list = new ArrayList<>();
//    Scanner scanner = new Scanner(System.in);
//        System.out.println("Name of the file:");
//                String fileName = scanner.nextLine();
//                try {
//
//                BufferedReader br = new BufferedReader(new FileReader(fileName));
//                String str;
//                while ((str = br.readLine()) != null) {
//                list.add(str);
//                }
//
//                System.out.println("Search for:");
//                String name = scanner.nextLine();
//                if (list.contains(name)) {
//                System.out.println("Found!");
//                } else {
//                System.out.println("Not found.");
//                }
//                } catch (FileNotFoundException e) {
//                System.out.println("Reading " + fileName + " failed.");
//                }

//    ArrayList<Integer> numbers = new ArrayList<>();
//    Scanner scanner = new Scanner(System.in);
//    int number = 0;
//
//        System.out.print("File? ");
//                String fileName = scanner.nextLine();
//                System.out.print("Lower bound? ");
//                int lowerNumber = Integer.valueOf(scanner.nextLine());
//                System.out.println("Upper bound? ");
//                int upperNumber = Integer.valueOf(scanner.nextLine());
//
//                BufferedReader br = new BufferedReader(new FileReader(fileName));
//                String str;
//                while ((str = br.readLine()) !=null) {
//                numbers.add(Integer.valueOf(str));
//                }
//
//                for (int i = 0; i < numbers.size(); i++) {
//        int n = numbers.get(i);
//        if (n >= lowerNumber && n <= upperNumber) {
//        number++;
//        }
//        }
//        System.out.println(number);

//    Scanner scanner = new Scanner(System.in);
//        System.out.println("File:");
//                String file = scanner.nextLine();
//
//                BufferedReader br = new BufferedReader(new FileReader(file));
//
//                String str;
//                List<String[]> total = new ArrayList<>();
//        while ((str = br.readLine()) != null) {
//        String[] arr = str.split(",");
//        total.add(arr);
//        }