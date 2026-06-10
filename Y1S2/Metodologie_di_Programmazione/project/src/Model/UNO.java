//TODO(nilou): Make a button that creates a button using the MVC communication protocol
package Model;

//the stage it's best to initialize in the Model, they are not GUI yet, and javaFX requires it to be in the "start" thread
import javafx.stage.Stage;
import javafx.stage.StageStyle;


//import View.Window;
//import View.VButtons;
import View.MainView;

import Controller.Controller;

public class UNO extends javafx.application.Application
{
    @Override
    public void start(javafx.stage.Stage stage)
    {
        stage.initStyle(StageStyle.UNDECORATED);
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

