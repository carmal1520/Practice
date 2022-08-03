import java.util.Objects;

public class Person {

    private String name;
    private int height;

    public Person(String name, int height) {
        this.name = name;
        this.height = height;
    }

    public String getName() {
        return name;
    }

    public int getHeight() {
        return height;
    }

    @Override
    public String toString() {
        return this.name + " (" + this.height + " cm)";
    }

    // Created with the insert code functionality of NetBeans
    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Person other = (Person) obj;
        if (this.height != other.height) {
            return false;
        }
        if (!Objects.equals(this.name, other.name)) {
            return false;
        }
        return true;
    }

}


















//public class Person {
//
//    private String name;
//    private int age;
//    private int height;
//    private int weight;
//
//    public Person(String name, int age, int height, int weight) {
//        this.name = name;
//        this.age = age;
//        this.height = height;
//        this.weight = weight;
//    }
//
//    public void printPerson() {
//        System.out.println("My name is " + this.name + " and I am " + this.age + " years old");
//    }
//
//    public void growOlder() {
//        this.age++;
//    }
//
//    public boolean isOfLegalAge() {
//        if (this.age > 17) {
//            return true;
//        }
//
//        return false;
//    }
//
//    public void setHeight(int height) {
//        this.height = height;
//    }
//
//    public int getHeight() {
//        return this.height;
//    }
//
//    public int getWeight() {
//        return this.weight;
//    }
//
//    public void setWeight(int weight) {
//        this.weight = weight;
//    }
//
//    public double bmi() {
//        double heightInMeters = this.height / 100.0;
//
//        return this.weight / (heightInMeters * heightInMeters);
//    }
//
//    public String getName() {
//        return this.name;
//    }
//
//
//    @Override
//    public String toString() {
//        return "My name is " + this.name + " and I am " + this.age + " years old. My BMI is " + this.bmi();
//    }
//}