package sdt;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import sdt.Mult;

public class TestMult {

	private Mult m;

	@Before
	public void setUp() throws Exception {
		m = new Mult();
	}

	@Test
	public void testMult() {
		int v;
		m.mult( 1, 2 );
		v = m.result();
		assertEquals( v, 2 );
	}

	@Test
	public void testMultX() {
		int v;
		m.mult( 3, 2 );
		v = m.result();
		assertEquals( v, 6 );
	}

}
