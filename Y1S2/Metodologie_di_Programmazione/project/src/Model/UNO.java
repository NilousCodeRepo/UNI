//THIS IS JUST THE APP LAUNCHER

//TODO(nilou): Make a button that creates a button using the MVC communication protocol
package Model;

import javafx.beans.property.IntegerProperty;
import javafx.beans.property.SimpleIntegerProperty;

import View.MainView;
import Controller.MainController;

public class UNO extends javafx.application.Application
{
    private final IntegerProperty pressCount = new SimpleIntegerProperty(0);

    public void incrementPressCount() {
        pressCount.set(pressCount.get() + 1);
    }

    public IntegerProperty pressCountProperty() {
        return pressCount;
    }

    @Override
    public void start(javafx.stage.Stage stage)
    {
        UNO model = new UNO();
        MainView view = new MainView();

        new Controller.MainController(view, model);

        //the stage it's best to initialize in the Model, they are not GUI yet, and javaFX requires it to be in the "start" thread
        stage.setScene( view.getScene( view.getRoot(), 400,300 ) );
        stage.setTitle("UNO the GAME");
        stage.show();
    }

    public static void main(String[] args)
    {
        //here we  place some "out of the purpose of the application controls". This is just an example
        String OS = System.getProperty("os.name");
        String OSVersion = System.getProperty("os.version");
        String OSArch = System.getProperty("os.arch");
        String javaVersion= System.getProperty("java.version");
        String javaFXVersion = System.getProperty("javafx.version");

        System.out.println("Operating System is: " + OS + "\n" +
                            "Operating System Version is: " + OSVersion + "\n" +
                            "Operating System Arch is: " + OSArch + "\n" +
                            "Java Version is: " + javaVersion + "\n" +
                            "JavaFX Version is: " + javaFXVersion + "");

        launch(args);
    }
}

