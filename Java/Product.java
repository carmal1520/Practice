public class Product {
    private String name;
    private String location;
    private int weight;

    public Product(String name) {
        this.name = name;
    }

    public Product(String name, String location) {
        this.name = name;
        this.location = location;
    }

    public Product(String name, int weight) {
        this.name = name;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "Product{" +
                "name='" + name + '\'' +
                ", location='" + location + '\'' +
                ", weight=" + weight +
                '}';
    }
}
