import java.util.Scanner;

public class Program {
    // Used to colour text strings in the console window
    private static final String TEXT_RESET = "\u001B[0m";
    private static final String TEXT_RED = "\u001B[31m";

    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        boolean runProgram = true;

        System.out.println("This is a simple calculator.\n");
        while (runProgram) {
            Testar calc = new Testar();

            calc.getIntegers();
            calc.getOperator();
            calc.getCalculationResult();

            switch (actionMenu()) {
                case "c":
                case "C":
                    clear();

                    break;

                case "x":
                case "X":
                    System.out.println("\nExiting the program!!");
                    runProgram = false;

                default:
                    break;
            }
        }
        sc.close();

    }

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

    // Method to clear the consol window
    private static void clear() {
        System.out.print("\033\143");
    }
}
