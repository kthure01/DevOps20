import java.util.Scanner;

public class Program {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        CarsInStock cars = new CarsInStock(200);
        CarsInStock cars2 = new CarsInStock(500);

        System.out.println("1 Enter how many sold car(s): ");
        cars.carsSold(Integer.parseInt(sc.nextLine()));

        System.out.println("1 Cars in stock: " + cars.getCarsInStock());

        System.out.println("1 Enter how many bought car(s): ");
        cars.carsBought(Integer.parseInt(sc.nextLine()));

        System.out.println("1 Cars in stock: " + cars.getCarsInStock());

        //

        System.out.println("\n\n2 Enter how many sold car(s): ");
        cars2.carsSold(Integer.parseInt(sc.nextLine()));

        System.out.println("2 Cars in stock: " + cars2.getCarsInStock());

        System.out.println("2 Enter how many bought car(s): ");
        cars2.carsBought(Integer.parseInt(sc.nextLine()));

        System.out.println("2 Cars in stock: " + cars2.getCarsInStock());

        System.out.println("\n" + cars + "\n");
        System.out.println(cars2);

        sc.close();
    }
}
