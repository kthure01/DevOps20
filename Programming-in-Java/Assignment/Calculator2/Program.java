import java.util.Scanner;

public class Program {
    // Used to colour text strings in the console window
    private static final String TEXT_RESET = "\u001B[0m";
    private static final String TEXT_RED = "\u001B[31m";

    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        boolean runProgram = true;

        System.out.println("This is a simple calculator.\n");

        // Lopp until user exit the program
        while (runProgram) {
            // Create a new instance of the Calculator class for each loop
            Calculator calc = new Calculator();

            // Ask for integers
            calc.getIntegers();

            // Ask for math operator
            calc.getOperator();

            // Show result of the calculation
            calc.getCalculationResult();

            // Ask user how to proceed
            switch (actionMenu()) {
                // Clear console window
                case "c":
                case "C":
                    clear();

                    break;

                // Exit program
                case "x":
                case "X":
                    System.out.println("\nExiting the program!!");
                    runProgram = false;

                    break;

                //
                default:
                    break;
            }
        }
        sc.close();

    }

    // Provided a menu to ask user how to procced
    private static String actionMenu() {
        String userInput = null;
        String regex = "[cCxX]";
        boolean falseInput = true;

        while (falseInput) {
            System.out.println("\nPress ENTER to continue, type X to exit the program or type C to clear the screen.");
            System.out.print(("Choose action [Press ENTER, C or X]: "));

            userInput = sc.nextLine();
            if (userInput.matches(regex) || userInput.isEmpty()) {
                falseInput = false;
            } else {
                System.out.println(TEXT_RED + "\n\nERROR: Invalid input!" + TEXT_RESET
                        + "\nA valid action is [Press ENTER, C or X]!");
            }
        }

        return userInput;
    }

    // Method to clear the consol window
    private static void clear() {
        System.out.print("\033\143");
    }
}
