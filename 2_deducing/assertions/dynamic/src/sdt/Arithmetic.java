package sdt;

import sdt.Multiplier;
import sdt.Adder;

public class Arithmetic {

	public static void main( String[] args ) {

		Adder a = new Adder();
		Multiplier m = new Multiplier();

		a.add( 1, 2 );
		m.mul( 3, 4 );
		a.add( 5, 6 );
		m.mul( 7, 8 );
		a.add( 9, 0 );

		System.out.println( a.sofar() + " " + m.sofar() );

	}

}
