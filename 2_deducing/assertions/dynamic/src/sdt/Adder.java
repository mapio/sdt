package sdt;

public class Adder {
	private int sofar = 0;

	public int add( int x, int y ) {
		int result = x + y;
		sofar += result;
		return result;
	}

	public int sofar() {
		return sofar;
	}
}
