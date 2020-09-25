public class ForLoop {

   static final long NSEC = 1000000000;
   String str1;
   String str2;


   public static void main(String[] args) {

      String[] stringArray = {"Ett", "Två", "Tre", "Fyra"};
      for (int i = 0; i < stringArray.length; i++) {
         System.out.println("Index " + i + " = " + stringArray[i]);


      }

      for (String str : stringArray) {
         System.out.println("Str = " + str);
      }

      int j = 0;
      while (j < stringArray.length){
         System.out.println("Index " + j + " = " + stringArray[j]);
         j++;
      }

   }
}
