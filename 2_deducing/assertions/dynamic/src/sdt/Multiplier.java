package sdt;

public class Multiplier {
	private int sofar = 0;

	public int mul( int x, int y ) {
		int result = x * y;
		sofar += result;
		return result;
	}

	public int sofar() {
		return sofar;
	}
}
