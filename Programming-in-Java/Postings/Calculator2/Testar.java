import java.util.Scanner;

public class Testar {
    // Used to colour text strings in the console window
    private static final String TEXT_RESET = "\u001B[0m";
    private static final String TEXT_RED = "\u001B[31m";
    private Scanner sc = new Scanner(System.in);

    private int[] _numbers; // Array of integers to calculate
    private String _operator; // Choosen operator
    private double _sum;

    private int _askForIntegerNumber = 1;
    private int _numberOfIntegers = 2;
    private String _regexOperators = "[\\+\\-\\*\\/]"; // Regex of valid operators

    // With the default constructor the user can input 2 integers
    public Testar() {
        _numbers = new int[_numberOfIntegers];
    }

    // The user select the number of integers to calculate
    public Testar(int numberOfIntegers) {
        _numberOfIntegers = numberOfIntegers;
        _numbers = new int[_numberOfIntegers];
    }

    public void getIntegers() {
        boolean falseInput = true;

        System.out.println("You have to input " + _numberOfIntegers + " integers!");

        while (falseInput) {
            try {
                System.out.print("Enter integer number " + _askForIntegerNumber + " : ");
                _numbers[_askForIntegerNumber - 1] = Integer.parseInt(sc.nextLine());

                if (_askForIntegerNumber == _numberOfIntegers) {
                    falseInput = false;
                } else {
                    _askForIntegerNumber = (falseInput) ? ++_askForIntegerNumber : _askForIntegerNumber;
                }
            } catch (NumberFormatException e) {
                System.out.println(TEXT_RED + "\n\nERROR: Invalid input!" + TEXT_RESET
                        + "\nEnter a valid integer between " + Integer.MIN_VALUE + " and " + Integer.MAX_VALUE);
                System.out.print("\nPress ENTER to continue: ");
                sc.nextLine();
            }
        }
    }

    // Method to get the operator.
    public void getOperator() {
        String userInput;

        boolean falseInput = true;

        while (falseInput) {
            System.out.print(("Choose which math operator you want to use: [+-*/]: "));

            userInput = sc.nextLine();
            if (userInput.matches(_regexOperators)) {
                _operator = userInput;
                falseInput = false;
            } else {
                System.out.println(
                        TEXT_RED + "\n\nERROR: Invalid input!" + TEXT_RESET + "\nEnter a valid math operator!");
                System.out.print("\nPress ENTER to continue: ");
                sc.nextLine();

                falseInput = true;
            }
        }
    }

    public void getCalculationResult() {
        String result = "The result of calculating numbers (";
        for (int i = 0; i < _numbers.length; i++) {
            result += _numbers[i] + " ";
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
                    System.out.print("Press ENTER to continue: ");
                    sc.nextLine();

                    return;
                }

                division();
                break;

            default:
                break;
        }

        System.out.println(result + ") is: " + _sum);
    }

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
