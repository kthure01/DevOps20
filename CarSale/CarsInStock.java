public class CarsInStock {
    private int _amountOfCarsInStock;
    private static int _carSold = 0;
    private static int _carBought = 0;

    public CarsInStock(int amountOfCarsInStock) {
        _amountOfCarsInStock = amountOfCarsInStock;
    }

    public void carsSold(int noOfCarsSold) {
        _amountOfCarsInStock -= noOfCarsSold;
        _carSold += noOfCarsSold;
    }

    public void carsBought(int noOfCarsBought) {
        _amountOfCarsInStock += noOfCarsBought;
        _carBought += noOfCarsBought;
    }

    public int getCarsInStock() {
        return _amountOfCarsInStock;
    }

    public String toString() {
        String result = "Total cars sold: " + _carSold + "\nTotal cars bought: " + _carBought;

        return result;
    }
}