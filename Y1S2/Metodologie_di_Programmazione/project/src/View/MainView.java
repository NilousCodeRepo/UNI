package View;

import javafx.scene.Scene;
import javafx.scene.layout.StackPane;//usalo per la root, mette gli elementi uno sopra l'altro
import javafx.scene.layout.VBox; // usalo per roba tipo liste di bottoni uno sotto/accanto l'altro 
import javafx.event.EventHandler;
import javafx.event.ActionEvent;

public class MainView
{
    //first i create the window in the Model.UNO file
    private final StackPane root; //here lies the base in which i shall draw my world(used for z-ordering)
    private Scene scene; //how and where to position things
    private final Buttons buttonsFactory;

    public MainView()
    {
        root = new StackPane();
        
        //TODO(nilou): il bottono ovviamente non va qua
        buttonsFactory = new Buttons();
        //button.createButton();
        
        //TODO(nilou): ovviamente questo ha bisogno del suo metodo interno
        root.getChildren().add(buttonsFactory.createButton("O BOTTON", null));
    }

    public void setInitialButtonHandler(EventHandler<ActionEvent> handler) {

        root.getChildren().
                removeIf(n -> n.getUserData() != null && n.getUserData().equals("initial")
            );

        Button btn = buttonsFactory.createButton("O BOTTON", handler);
        btn.setUserData("initial");
        root.getChildren().add(btn);
    }

    // Allow controller to ask the view to add a new button with a handler
    public void spawnButton(String label, EventHandler<ActionEvent> handler) {
        var btn = buttonsFactory.createButton(label, handler);
        root.getChildren().add(btn);
    }

    public Scene getScene(StackPane root, int width, int height)
    {
        scene = new Scene(root, width, height);
        return scene;
    }

    public StackPane getRoot()
    {
        return root;
    }
}
