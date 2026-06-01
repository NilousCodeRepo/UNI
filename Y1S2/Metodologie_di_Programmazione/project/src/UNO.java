import javafx.application.Application;

import javafx.stage.Stage;

import javafx.scene.Scene;
import javafx.scene.layout.StackPane;//usalo per la root, mette gli elementi uno sopra l'altro
import javafx.scene.layout.VBox; // usalo per roba tipo liste di bottoni uno sotto/accanto l'altro 
import javafx.scene.control.Label;
import javafx.scene.control.Button;

public class UNO extends Application
{
    @Override
    public void start(Stage stage)
    {
        StackPane root = new StackPane();
        root.getStyleClass().add("root");//creating css class: root
        
        Scene scene = new Scene(root, 400, 300);
        
        int spacing_px = 5;
        VBox start_menu = new VBox(spacing_px);
        start_menu.getStyleClass().add("start_menu");

        Button start_button = new Button("START");
        start_button.getStyleClass().add("start_button");

        Button quit_button = new Button("QUIT");
        quit_button.getStyleClass().add("quit_button");

        //adding buttons to button stack
        start_menu.getChildren().addAll(start_button, quit_button);
        
        //drawing on the principale panel the buttons
        root.getChildren().add(start_menu);
    
        scene.getStylesheets()
             .add(
                    getClass().getResource("styles/start_menu.css").toExternalForm()
                );
        
        stage.setTitle("UNO the GAME");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args)
    {
        launch(args);
    }
}

