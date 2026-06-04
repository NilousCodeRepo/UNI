package View;

import javafx.stage.Stage;

import javafx.scene.Scene;
import javafx.scene.layout.StackPane;//usalo per la root, mette gli elementi uno sopra l'altro

public class Window
{
    private StackPane CreatePane(String nameOfPane)
    {
        StackPane pane = new StackPane();
        pane.getStyleClass().add(nameOfPane);//creating css class: root
        return pane;
    }
    
    private Scene CreateScene(StackPane pane, int width, int height)
    {
        Scene scene = new Scene(pane, width, height);
        return scene;
    }

    public void CreateWindow(Stage stage)
    {
        StackPane CyberPunk = CreatePane("root");

        int spacing_px = 5;
        VBox start_menu = new VBox(spacing_px);
        start_menu.getStyleClass().add("start_menu");

        Button start_button = new Button("START");
        start_button.getStyleClass().add("start_button");

        Button quit_button = new Button("QUIT");
        quit_button.getStyleClass().add("quit_button");

        //adding buttons to button stack
        start_menu.getChildren().addAll(start_button, quit_button);
        
        //drawing on the principal panel of the buttons
        CyberPunk.getChildren().add(start_menu);

        Scene s = CreateScene(CyberPunk, 400, 300);
        s.getStylesheets()
             .add(
                    getClass().getResource("../styles/start_menu.css").toExternalForm()
                );

        stage.setScene(s);
    }
    
}
