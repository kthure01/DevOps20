import java.util.Scanner;

public class Calculator {
    // Used to colour text strings in the console window
    private static final String TEXT_RESET = "\u001B[0m";
    private static final String TEXT_RED = "\u001B[31m";
    private static final String TEXT_YELLOW = "\u001B[33m";

    private Scanner sc = new Scanner(System.in);

    private int[] _numbers; // Array of integers to calculate
    private String _operator; // Choosen operator
    private double _sum;

    private int _askForIntegerNumber = 1; // Used to show the user which integer we ask for
    private int _numberOfIntegers = 2; // Size of the integer array used to hold the users input
    private String _regexOperators = "[\\+\\-\\*\\/]"; // Regex of valid operators

    // With the default constructor the user can input 2 integers
    public Calculator() {
        _numbers = new int[_numberOfIntegers];
    }

    // Constructor to let the user select how many integers to calculate. Not yet
    // used in the main program
    public Calculator(int numberOfIntegers) {
        _numberOfIntegers = numberOfIntegers;
        _numbers = new int[_numberOfIntegers];
    }

    // Method to get integers from the user
    public void getIntegers() {
        boolean falseInput = true;

        System.out.println("You have to input " + _numberOfIntegers + " integers!");

        // Loop until we have got the correct number of integers from the user
        while (falseInput) {
            try {
                System.out.print("Enter integer number " + _askForIntegerNumber + " : ");
                _numbers[_askForIntegerNumber - 1] = Integer.parseInt(sc.nextLine());

                // If we got all integers, end the loop
                if (_askForIntegerNumber == _numberOfIntegers) {
                    falseInput = false;
                } else {
                    _askForIntegerNumber = (falseInput) ? ++_askForIntegerNumber : _askForIntegerNumber;
                }
            } catch (NumberFormatException e) {
                System.out.println(TEXT_RED + "\n\nERROR: Invalid input!" + TEXT_RESET
                        + "\nValid input is an integer between " + Integer.MIN_VALUE + " and " + Integer.MAX_VALUE);
            }
        }
    }

    // Method to get the math operator
    public void getOperator() {
        String userInput;

        boolean falseInput = true;

        // Loop until we got a correct math operator
        while (falseInput) {
            System.out.print(("Choose which math operator you want to use: [+-*/]: "));
            userInput = sc.nextLine();

            if (userInput.matches(_regexOperators)) {
                _operator = userInput;
                falseInput = false;
            } else {
                System.out.println(
                        TEXT_RED + "\n\nERROR: Invalid input!" + TEXT_RESET + "\nA valid math operator is [+-*/]!");
            }
        }
    }

    // Method to print out the result of the math calculation
    public void getCalculationResult() {
        String result = "The result of calculating the numbers (";

        // Add all integers to the output string
        for (int i = 0; i < _numbers.length; i++) {
            result += _numbers[i];
            if ((i + 1) != _numbers.length)
                result += _operator;
        }

        switch (_operator) {
            case "+":
                addition();
                break;

            case "-":
                subtraction();
                break;

            case "*":
                multiplication();
                break;

            case "/":
                boolean divideByNull = false;

                for (int i = 1; i < _numbers.length; i++) {
                    if (_numbers[i] == 0) {
                        divideByNull = true;
                    }
                }

                if (divideByNull) {
                    System.out.println(TEXT_RED + "Division by zero is not allowd" + TEXT_RESET);

                    return;
                }

                division();
                break;

            default:
                break;
        }

        System.out.println(TEXT_YELLOW + result + ") is: " + _sum + TEXT_RESET);
    }

    // Math methods
    private void addition() {
        for (int i = 0; i < _numbers.length; i++) {
            _sum += (long) _numbers[i];
        }
    }

    private void subtraction() {
        for (int i = 0; i < _numbers.length; i++) {
            if (i == 0) {
                _sum = _numbers[i];
            } else {
                _sum -= (long) _numbers[i];
            }
        }
    }

    private void multiplication() {
        for (int i = 0; i < _numbers.length; i++) {
            if (i == 0) {
                _sum = _numbers[i];
            } else {
                _sum *= (long) _numbers[i];
            }
        }
    }

    private void division() {
        for (int i = 0; i < _numbers.length; i++) {
            if (i == 0) {
                _sum = _numbers[i];
            } else {
                _sum /= (long) _numbers[i];
            }
        }
    }

}
