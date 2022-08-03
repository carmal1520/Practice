public class Product1 {
    public String name;
    public double price;
    public int quantity;

    public Product1(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    public void printProduct() {
        System.out.print(name + ", " + price + " " + quantity + " pcs");
    }
}
