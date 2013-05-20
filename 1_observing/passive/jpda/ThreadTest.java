import java.util.concurrent.atomic.AtomicLong;

public class ThreadTest {

	static interface Counter {
		public void increment();
		public long value(); 
	}
	
	static class NonSyncronizedCounter implements Counter {
		private long counter = 0;
		public void increment() { counter++; }
		public long value() { return counter; } 
	}
	
	static class SyncronizedCounter implements Counter {
		private long counter = 0;
		public synchronized void increment() { counter++; }
		public synchronized long value() { return counter; } 
	}

	static class ModernCounter implements Counter {
		private AtomicLong counter = new AtomicLong( 0 );
	    public void increment() { counter.incrementAndGet(); }
	    public long value() { return counter.get(); }
	}

	static class Worker implements Runnable {
		Counter counter;
		public Worker( Counter counter ) { this.counter = counter; }
		public void run() {	while ( true ) counter.increment();	}
	}

	public static void main( String[] args ) {
		
		Counter shared = null;
		
		int numThreads = Integer.valueOf( args[ 1 ] );
		
		switch ( Integer.valueOf( args[ 0 ] ) ) {
			case 0: shared = new NonSyncronizedCounter(); numThreads = 1; break;
			case 1: shared = new SyncronizedCounter(); break;
			case 2: shared = new ModernCounter(); break;
		}
		
		for ( int i = 0; i < numThreads; i++ ) {
			(new Thread( new Worker( shared ) ) ).start();
			System.out.print( i + "\r" );
		}
		
		System.out.println( "Running..." );
		long previousValue, previousTime;
		previousTime = System.currentTimeMillis();
		previousValue = 0;
		while ( true ) {
			long currentValue = shared.value();
			long currentTime = System.currentTimeMillis();
			System.out.println( ( currentValue - previousValue ) / (float)( currentTime - previousTime ) );
			previousValue = currentValue;
			previousTime = currentTime;
			try {
				Thread.sleep( 1000 );
			} catch ( InterruptedException e ) {
				return;
			}
		}
		
	}

}
