/*
Chapter 3 Sample Program: Find the Day of Week of a Given Date
File: Ch3FindDayOfWeek.java
*/

import java.util.*;
import java.text.*;

class Ch3FindDayOfWeek {
   public static void main(String[] args) {
      int year, month, day;
      GregorianCalendar cal;
      SimpleDateFormat sdf;
      Scanner scanner = new Scanner(System.in);
      scanner.useDelimiter(System.getProperty("line.separator"));
      System.out.print("Year (yyyy): ");
      year = scanner.nextInt();
      System.out.print("Month (1-12): ");
      month = scanner.nextInt();
      System.out.print("Day (1-31): ");
      day = scanner.nextInt();
      cal = new GregorianCalendar(year, month - 1, day);
      sdf = new SimpleDateFormat("EEEE");
      System.out.println("");
      System.out.println("Day of Week: " + sdf.format(cal.getTime()));
   }
}
