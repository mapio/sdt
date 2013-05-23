package sdt;

public class Adder {

	private int tot = -2;

	public void add( int x ) {
		tot += x + 1;
	}

	public int value() {
		return tot;
	}

}
