import jdk.swing.interop.SwingInterOpUtils;

public class Main {

   public static void main(String[] args) {
      VideoPlayer video = new VideoPlayer();
      DvdPlayer dvd = new DvdPlayer();

      System.out.println(video.play());
      System.out.println(dvd.play());
      
      System.out.println(dvd.fastRewind());
      System.out.println(video.fastForward());
   }

}
