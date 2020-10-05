/*
Chapter 6 Sample Program: Time the performance of gcd methods
File: Ch6TimeGcd.java
*/

import java.util.*;

class Ch6TimeGcd {
   private final Scanner scanner;

   public Ch6TimeGcd() {
      scanner = new Scanner(System.in);
   }

   public static void main(String[] args) {
      Ch6TimeGcd tester = new Ch6TimeGcd();
      tester.start();
      System.exit(0);
   }

   public void start() {
      long bruteForceTime, euclidTime;
      int m, n;
      while (isContinue()) {
         m = getPositiveInteger();
         n = getPositiveInteger();

         //Time the brute force method
         bruteForceTime = timeMethod(m, n, ComputationType.BRUTE_FORCE);

         //Time the Euclidean method
         euclidTime = timeMethod(m, n, ComputationType.EUCLID);
         System.out.println("M: " + m);
         System.out.println("N: " + n);
         System.out.println("Brute Force Time: " + bruteForceTime);
         System.out.println("Euclidean Time:                 " + euclidTime + "\n");
      }
   }

   private long timeMethod(int m, int n, ComputationType type) {
      Date startTime, endTime;
      startTime = new Date();
      if (type == ComputationType.BRUTE_FORCE) {
         gcd_bruteforce(m, n);
      } else {
         gcd(m, n);
      }
      endTime = new Date();
      return (endTime.getTime() - startTime.getTime());
   }

   private int getPositiveInteger() {
      int input;
      while (true) {
         System.out.print("Enter positive integer (0 is okay):");
         input = scanner.nextInt();
         if (input >= 0) break;
         System.out.println("Input must be 0 or more");
      }
      return input;
   }

   private boolean isContinue() {
      String input;
      boolean response = false;
      System.out.print("Run test? ");
      input = scanner.next();
      if (input.equals("Y") || input.equals("y")) {
         response = true;
      }
      return response;
   }

   private int gcd_bruteforce(int m, int n) {
      return 0;
   }

   private int gcd(int m, int n) {
      return 0;
   }

   private enum ComputationType {BRUTE_FORCE, EUCLID}
}