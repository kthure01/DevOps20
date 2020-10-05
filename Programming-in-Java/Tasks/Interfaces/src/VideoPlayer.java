public class VideoPlayer implements IMediaPlayer {
   @Override
   public String play() {
      return "Video play";
   }

   @Override
   public String fastRewind() {
      return "Video rewind";
   }

   @Override
   public String fastForward() {
      return "Video forward";
   }
}
