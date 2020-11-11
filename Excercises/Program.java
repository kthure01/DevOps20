import java.util.Arrays;
import java.util.Scanner;

/**
 * Program
 */
public class Program {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {

        exercise8();

    }

    public static void exercise1() {
        int[] numbers = new int[3];

        System.out.println("Input number 1: ");
        numbers[0] = Integer.parseInt(sc.nextLine());

        System.out.println("Input number 2: ");
        numbers[1] = Integer.parseInt(sc.nextLine());

        System.out.println("Input number 3: ");
        numbers[2] = Integer.parseInt(sc.nextLine());

        Arrays.sort(numbers);

        System.out.println("Smallest number is: " + numbers[0]);
    }

    public static void exercise2() {
        int[] numbers = new int[3];

        System.out.println("Input number 1: ");
        numbers[0] = Integer.parseInt(sc.nextLine());

        System.out.println("Input number 2: ");
        numbers[1] = Integer.parseInt(sc.nextLine());

        System.out.println("Input number 3: ");
        numbers[2] = Integer.parseInt(sc.nextLine());

        System.out.println("Average number is: " + ((double) numbers[0] + numbers[1] + numbers[2]) / 3);
    }

    public static void exercise3() {
        String numberString;

        System.out.println("Input number: ");
        numberString = sc.nextLine();

        if (numberString.length() % 2 == 0) {

        }
    }

    public static void exercise8() {
        int investmentAmount;
        double interest;
        int noOfYears;

        System.out.println("Input investment amount: ");
        investmentAmount = Integer.parseInt(sc.nextLine());

        System.out.println("Input interest: ");
        interest = Integer.parseInt(sc.nextLine());

        System.out.println("Input number of years: ");
        noOfYears = Integer.parseInt(sc.nextLine());

        for (int i = 1; i <= noOfYears; i++) {
            investmentAmount += investmentAmount * (interest * 0.01);
            System.out.println("Year " + i + ": " + investmentAmount);
        }

        
    }
}