import java.util.concurrent.atomic.AtomicInteger;

import org.softee.management.annotation.Description;
import org.softee.management.annotation.MBean;
import org.softee.management.annotation.ManagedAttribute;
import org.softee.management.annotation.ManagedOperation;
import org.softee.management.annotation.Parameter;
import org.softee.management.helper.MBeanRegistration;

@MBean( objectName = "it.unimi.di:type=SdtDemo" )
public class BeanedCounter {

    private final AtomicInteger counter = new AtomicInteger();

    public static void main( String[] args ) throws Exception {
        new BeanedCounter().run();
    }

    public Object run() throws Exception {
        new MBeanRegistration( this ).register();
        for ( ;; ) {
            incrementCounter( 1 );
            Thread.sleep( 5000 );
        }
    }

    @ManagedAttribute
    public int getCounter() {
        return counter.get();
    }

    @ManagedAttribute
    public void setCounter( int counter ) {
        this.counter.set(counter);
    }

    @ManagedOperation
    public int incrementCounter( @Parameter( "amount" ) int delta ) {
        return counter.addAndGet( delta );
    }

    @ManagedOperation
    public void reset() {
        counter.set( 0 );
    }
}
