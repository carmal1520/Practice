public class Debt {
    double balance;
    double interestRate;

    public Debt(double initialBalance, double initialInterestRate) {
        this.balance = initialBalance;
        this.interestRate = initialInterestRate;
    }

    public void printBalance() {
        System.out.println("Balance: " + this.balance);
    }

    public void waitOneYear() {
        balance *= interestRate;
    }
}
