import java.text.MessageFormat;
import java.util.ArrayList;

public class Suitcase {
    private int maximumWeight;

    private final ArrayList<Item> items = new ArrayList<>();

    public Suitcase(int maximumWeight) {
        this.maximumWeight = maximumWeight;
    }

    public void addItem(Item item) {
        final int currentTotalWeight = this.items.stream()
                .mapToInt(Item::getWeight)
                .sum();

        if (item.getWeight() + currentTotalWeight <= maximumWeight) {
            this.items.add(item);
        }
    }

    @Override
    public String toString() {
        if (items.isEmpty()) {
            return "no items (0kg)";

        }
        int totalWeight = 0;
        String itemPluralMultipleNaming = "item";
        if (items.size() > 1) {
            itemPluralMultipleNaming = "items";
        }
        for (Item item : items) {
            totalWeight += item.getWeight();
        }
        return MessageFormat.format("{0} {1} ({2} kg)", items.size(), itemPluralMultipleNaming, totalWeight);
    }
}
