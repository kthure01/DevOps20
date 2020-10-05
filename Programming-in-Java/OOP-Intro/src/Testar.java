public class Testar implements ITest1 {


   public static void main(String[] args) {
      Testar testar = new Testar();
      ITest1 test1 = new Testar();

      test1.metod1();
      testar.metod2();
   }

   public void metod4() {
      System.out.println(new Object() {
      }.getClass().getEnclosingMethod().getName());
   }

   @Override
   public void metod1() {
      System.out.println(new Object() {
      }.getClass().getEnclosingMethod().getName());
   }

   @Override
   public void metod2() {
      System.out.println(new Object() {
      }.getClass().getEnclosingMethod().getName());
   }

   @Override
   public void metod3() {
      System.out.println(new Object() {
      }.getClass().getEnclosingMethod().getName());
   }
}