package com.kthure;
/*
För betyget Godkänt:

    Skapa ett ’Repository’ på Github
    Skapa ett nytt java projekt som innehåller minst:
        En .gitignore fil som innehåller konfigurationsfilerna för den IDE du använder
        En ReadMe fil med några korta valfria ord
        Minst en class som innehåller ett ’Try Catch’-block

_____________________________________________________________________________________

För betyget Väl Godkänt:

    Skapa en ny bransch
    I din nya bransch skapar du en ny valfri feature (ex Class, metod osv)
    Pusha din branch och dess modifieringar till Github
    Merga din branch till master på Github
*/

import javax.sound.midi.Soundbank;
import java.util.IllegalFormatException;
import java.util.Scanner;

public class Main {
   static Scanner sc = new Scanner(System.in);

   public static void main(String[] args) {
      String regex = "[0-9]";
      int input;

      while (true) {
         try {
            System.out.println();
            System.out.print("Enter a character " + regex + ": ");
            input = Integer.parseInt(sc.nextLine());

            System.out.println("You entered a correct character: " + input);

            System.out.print("Type exit to exit the program!: ");
            if (sc.nextLine().equals("exit")) {
               System.out.println("Exiting the program!");
               break;
            }
         } catch (Exception e) {
            System.err.println("Input error: " + e.getMessage());
         }
      }


   }
}
