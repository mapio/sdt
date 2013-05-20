import java.util.Random;
import java.lang.Long;

public class WhatIsSlow {
	
	static interface RNG {
		public double next();
	}
	
	static class FastRNG implements RNG {
		static long x = 1;
		public double next() {
			x ^= x << 13;
			x ^= x >>> 7;
			x ^= (x << 17);
			return x / (double)Long.MAX_VALUE;
		}
	}

	static class SlowRNG implements RNG {
		static final Random r = new Random();
		public double next() {
			return r.nextDouble();
		}
	}
	
	static RNG rng = null;
	
	static double gaussian() {
		double s, u, v;
		do {
			u = rng.next();
	        v = rng.next();
	        double vv = ( 2 * v - 1 );
	        vv *= vv;
	        double uu = ( 2 * u - 1 );
	        uu *= uu;
	        s = uu + vv;
	      } while( s >= 1 );
	      return  u * Math.sqrt( -2 * Math.log( s ) / s ) ;
	}
	
	public static void main( String[] args ) {
		rng = args[ 0 ].startsWith( "s" ) ? new SlowRNG() : new FastRNG();
		long n = Long.parseLong( args[ 1 ] );
		while ( --n != 0 ) gaussian();
	}

}
