public class Booky {

    private String title;
    private int pages;
    private int year;

    public Booky(String bookTitle, int numberOfPages, int publicationYear) {
        this.title = bookTitle;
        this.pages = numberOfPages;
        this.year = publicationYear;
    }

    public String getBookTitle() {
        return title;
    }

    public int getPages() {
        return pages;
    }

    public int getYear() {
        return year;
    }

    @Override
    public String toString() {
        return this.title + ", " + this.pages + " pages, " + this.year;
    }
}
