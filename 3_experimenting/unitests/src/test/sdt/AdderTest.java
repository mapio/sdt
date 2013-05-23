package sdt;

import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;


public class AdderTest {

	Adder sut;

	@Before
	public void setUp() throws Exception {
		sut = new Adder();
	}

	@Test
	public void testAdd() {
		sut.add( 1 );
		sut.add( 2 );
		assertEquals( 3, sut.value() );
	}

	@Test
	public void testValue() {
		assertEquals( 0, sut.value() );
	}

}
