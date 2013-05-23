package sdt;

import org.junit.internal.TextListener;
import org.junit.runner.JUnitCore;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith( Suite.class )
@Suite.SuiteClasses( { AdderTest.class } )

public class TestSuite {

	public static void main( String[] args ) {
		JUnitCore junit = new JUnitCore();
	    junit.addListener( new TextListener( System.out ) );
	    junit.run( AdderTest.class );
	}

}
