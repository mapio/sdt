package sdt;

public class Adder {

	private int tot = 0;

	public void add( int x ) {
		tot += x;
	}

	public int value() {
		return tot;
	}

}
