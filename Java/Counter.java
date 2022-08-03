public class Counter {
    private int counter;

    public Counter(int startValue) {
        this.counter = startValue;
    }

    public Counter() {
        this.counter = 0;
    }

    public int value() {
        return this.counter;
    }

    public void increase() {
        counter++;
    }

    public void increase(int increaseBy) {
        if (increaseBy < 0) {

        }
        counter += increaseBy;
    }

    public void decrease() {
        counter--;
    }

    public void decrease(int decreaseBy) {
        counter-= decreaseBy;
    }
}
