public class Vehicle {

    private String make;
    private String model;
    private int wheels;

    public String getMake() {
        return this.make;
    }

    public void setMake(String make) {
        this.make = make;
    }

    public String getModel() {
        return this.model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public int getWheels() {
        return this.wheels;
    }

    public void setWheels(int wheels) {
        this.wheels = wheels;
    }

    public Vehicle() {
    }

    public Vehicle(String sMake, String sModel, int iWheels) {
        setMake(sMake);
        setModel(sModel);
        setWheels(iWheels);
    }

    @Override
    public String toString() {
        String outputString;

        outputString = "Make: " + getMake();
        outputString += "\nModel: " + getModel();
        outputString += "\nWheels: " + getWheels();

        return outputString;
    }

    public static boolean isLeapYear(int year) {
        boolean isLeapYear = false;

        // Varje år som är jämnt delbart med 4 är ett skottår: till exempel 1984, 1996
        // och 2004 är skottår.
        if (year % 4 == 0) {
            // År som är jämnt delbart med 100 (till exempel 1900) är ett skottår endast om
            // det också är jämnt delbart med 400.
            if (year % 100 == 0) {
                if (year % 400 == 0)
                    isLeapYear = true;
            } else
                isLeapYear = true;
        } else
            isLeapYear = false;

        return isLeapYear;
    }
}
