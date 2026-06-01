import javafx.application.Application;

import javafx.stage.Stage;

import javafx.scene.Scene;

    import javafx.scene.paint.Color;
   
    import javafx.scene.control.Label;
    import javafx.scene.control.Button;
    
    import javafx.scene.layout.VBox;

public class ButtonCSS extends Application
{
    @override
    public void start(Stage stage)
    {
        VBox root = new VBox(10);
        root.getStyleClass().add("root");//creating css class: root

        Label label = new Label("Button with CSS styling");
        label.getStyleClass().add("label");

        Button button = new Button("Button");
        buton.getStyleClass().add("buton");

        root.getChildren().addAll(label, buton);

        Scene scene = new Scene("root", 400, 300);
        scene.getStyleSheet()
             .add(
                    getClass().getResource("ButtonCSS.css").toExternalForm()
                );

        stage.setTitle("ButtonCSS");
        stage.setScene(scene);
        stage.show();
    }


    public static void main(String[] args)
    {
        launch(args);
    }
}
