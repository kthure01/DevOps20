/*
Chapter 2 Sample Program: Displaying a Window
File: Ch2Sample1.java
*/

import javax.swing.*;

class Ch2Sample1 {
   public static void main(String[] args) {
      JFrame myWindow;
      myWindow = new JFrame();
      myWindow.setSize(300, 200);
      myWindow.setTitle("My First Java Program");
      myWindow.setVisible(true);
      myWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   }
}
