import java.text.BreakIterator;
import java.util.Scanner;

public class Calculator {
    // Used to colour text strings in the console window
    public static final String TEXT_RESET = "\u001B[0m";
    public static final String TEXT_RED = "\u001B[31m";

    // Create a scanner to allow user inputs
    static Scanner sc = new Scanner(System.in);

    // Variables to hold user input
    static int firstNumber;
    static int secondNumber;

    static boolean runProgram = true;

    public static void main(final String[] args) {

        // The program will run in a loop until the user choose to exit
        while (runProgram) {
            System.out.println(("\nThis program will operate on 2 integers.\n"));

            // Ask for 2 integers
            firstNumber = getAnInteger(1);
            secondNumber = getAnInteger(2);

            // Ask for the operator
            switch (getOperator()) {
                case "+":
                    System.out.println("\nThe result of the expression " + firstNumber + "+" + secondNumber + " is "
                            + addition(firstNumber, secondNumber));
                    break;

                case "-":
                    System.out.println("\nThe result of the expression " + firstNumber + "-" + secondNumber + " is "
                            + subtraction(firstNumber, secondNumber));
                    break;

                case "*":
                    System.out.println("\nThe result of the expression " + firstNumber + "*" + secondNumber + " is "
                            + multiplication(firstNumber, secondNumber) + ".");
                    break;

                case "/":
                    if (secondNumber == 0) {
                        System.out.println(TEXT_RED + "Division by zero is not allowd" + TEXT_RESET);
                        System.out.print("Press ENTER to continue: ");
                        sc.nextLine();

                        break;
                    }

                    System.out.println("\nThe result of the expression " + firstNumber + "/" + secondNumber + " is "
                            + division(firstNumber, secondNumber));
                    break;

                default:
                    break;
            }

            // Ask the user if he/she want to continue or exit the program
            switch (actionMenu()) {
                case "c":
                case "C":
                    clear();

                    break;

                case "x":
                case "X":
                    System.out.println("\nExiting the program!!");
                    runProgram = false;
                    break;

                default:
                    break;

            }
        }

    }

    // Method to get the operator.
    private static String getOperator() {
        String userInput = null;
        String regex = "[\\+\\-\\*\\/]";
        boolean falseInput = true;

        do {
            System.out.print(("Choose which math operator you want to use: [+-*/]: "));

            userInput = sc.nextLine();
            if (userInput.matches(regex)) {
                falseInput = false;
            } else {
                System.out.println(
                        TEXT_RED + "\n\nERROR: Invalid input!" + TEXT_RESET + "\nEnter a valid math operator!");
                System.out.print("\nPress ENTER to continue: ");
                sc.nextLine();

                falseInput = true;
            }
        } while (falseInput);

        return userInput;
    }

    // Method to ask the user how to continue the program
    private static String actionMenu() {
        String userInput = null;
        String regex = "[cCxX]";
        boolean falseInput = true;

        do {
            System.out.println("\nPress ENTER to continue, type X to exit the program or type C to clear the screen.");
            System.out.print(("Choose action: [ENTER, C or X]: "));

            userInput = sc.nextLine();
            if (userInput.matches(regex) || userInput.isEmpty()) {
                falseInput = false;
            } else {
                System.out.println(TEXT_RED + "\n\nERROR: Invalid input!" + TEXT_RESET + "\nEnter a valid action!");
                System.out.print("\nPress ENTER to continue: ");
                sc.nextLine();

                falseInput = true;
            }
        } while (falseInput);

        return userInput;
    }

    // Method to ask the user for a valid integer
    private static int getAnInteger(int intCount) {
        int userInput = 0;
        boolean falseInput = true;

        do {
            try {
                System.out.print("Enter an integer (no: " + intCount + "): ");
                userInput = Integer.parseInt(sc.nextLine());
                falseInput = false;
            } catch (NumberFormatException e) {
                System.out.println(TEXT_RED + "\n\nERROR: Invalid input!" + TEXT_RESET
                        + "\nEnter a valid integer between " + Integer.MIN_VALUE + " and " + Integer.MAX_VALUE);
                System.out.print("\nPress ENTER to continue: ");
                sc.nextLine();

                falseInput = true;
            }

        } while (falseInput);

        return userInput;
    }

    // Method to clear the consol window
    private static void clear() {
        System.out.print("\033\143");
    }

    // Methods for calculations depending on the users choice
    private static long addition(int first, int second) {
        return ((long) first) + second;
    }

    private static long subtraction(int first, int second) {
        return ((long) first) - second;
    }

    private static long multiplication(int first, int second) {
        return ((long) first) * second;
    }

    private static double division(int first, int second) {
        return ((float) first) / second;
    }

}