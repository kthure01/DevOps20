public class DvdPlayer implements IMediaPlayer {
   @Override
   public String play() {
      return "Dvd play";
   }

   @Override
   public String fastRewind() {
      return "Dvd rewind";
   }

   @Override
   public String fastForward() {
      return "Dvd forward";
   }
}
