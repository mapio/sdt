public class Loop {

	public static void main( String[] args ) {
		try {
			while ( true ) {
				System.out.println( "." );
				Thread.sleep(5 * 1000);
			}
		} catch ( InterruptedException e ) {
			e.printStackTrace();
		}
	}
}
