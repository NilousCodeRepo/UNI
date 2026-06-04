package Model;

import View.Window;

public class UNO extends javafx.application.Application
{
    @Override
    public void start(javafx.stage.Stage stage)
    {
        Window w = new Window();
        w.CreateWindow(stage);

        stage.setTitle("UNO the GAME");
        stage.show();
    }

    public static void main(String[] args)
    {
        //TODO(nilou): check things like OS, java version, javafx version
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

