package sdt;

import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

public class TestMult {

	private Mult m;

	@Before
	public void setUp() throws Exception {
		m = new Mult();
	}

	@Test
	public void testMultOK() {
		m.mult( 1, 2 );
		assertEquals( 2, m.result() );
	}

	@Test
	public void testMultFail() {
		m.mult( 3, 2 );
		assertEquals( 6, m.result() );
	}

}
