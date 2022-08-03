public class Pet {
    private String name;
    private String dogType;

    public Pet(String name, String dogType) {
        this.name = name;
        this.dogType = dogType;
    }

    @Override
    public String toString() {
        return this.name + (this.dogType);
    }
}
