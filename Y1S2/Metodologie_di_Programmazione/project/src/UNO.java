import javafx.application.Application;

import javafx.stage.Stage;

import javafx.scene.Scene;
import javafx.scene.layout.StackPane;

//most minimal javafx app
public class UNO extends Application
{
    @Override 
    public void start(Stage stage)
    {
        StackPane root = new StackPane();
        Scene scene = new Scene(root);

        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args)
    {
        launch(args);
    }
}
