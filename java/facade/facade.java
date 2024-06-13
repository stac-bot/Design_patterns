package java.facade;

enum Brightness{
    UNKNOWN, 
    BRIGHT,
    DIM
}
enum Service{
    UNKNOWN,
    HULU,
    NETFLIX,
    HBO
}

class SmartHomeSubSystem{
    private Brightness brightness;
    private int temperature;
    private boolean isSecurityArmed;
    private Service streamingService;

    //building a constructor class for the SmartHomeSubSystem
    public SmartHomeSubSystem(){
        this.brightness = Brightness.UNKNOWN;
        this.temperature = 19;
        this.isSecurityArmed = false;
        this.streamingService =  Service.UNKNOWN;

    }
    public void setBrightness(Brightness brightness){
        this.brightness = brightness;

    }

    public void setTemperature(int temperature){
        this.temperature = temperature;

    }

    public void setIsSecurityArmed(boolean isSecurityArmed){
        this.isSecurityArmed = isSecurityArmed;

    }
    public void setStreamingService(Service streamingService){
        this.streamingService = streamingService;
    
    }

    private void enableMoitionSensor(){
        //...
    }

    private void updateFirmware(){
        //...
    }

}
class SmartHomeFacade{
    private SmartHomeSubSystem  smartHome;
    public SmartHomeFacade(SmartHomeSubSystem smartHome){
        this.smartHome = smartHome;
    }

    public void setMovieMode(){
        smartHome.setBrightness(Brightness.DIM);
        smartHome.setTemperature(22);
        smartHome.setIsSecurityArmed(true);
        smartHome.setStreamingService(Service.NETFLIX);

    }

    public void setFocusMode(){
        smartHome.setBrightness(Brightness.BRIGHT);
        smartHome.setTemperature(22);
        smartHome.setIsSecurityArmed(true);
        smartHome.setStreamingService(Service.UNKNOWN);
    }
}



public class facade {
    public static void main(String[] args){
        SmartHomeFacade f = new SmartHomeFacade(new SmartHomeSubSystem());
        f.setMovieMode();
        f.setFocusMode();
    }
    
}
