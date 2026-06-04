import javafx.scene.layout.VBox; // usalo per roba tipo liste di bottoni uno sotto/accanto l'altro 
import javafx.scene.control.Button;

class VButtons
{
    protected VBox RootVBox(int spacing_px, String css_name)
    {
        VBox vbox = new VBox(spacing_px);
        vbox.getStyleClass().add(css_name);
    }

    protected Button DeclareVButton(String css_name)
    {
        Button start_button = new Button("START");
        start_button.getStyleClass().add("start_button");

        Button quit_button = new Button("QUIT");
        quit_button.getStyleClass().add("quit_button");


        return Button;
    }
    
    //TODO(nilou): see how to dinamically add children here
    private CreateVButton()
    {
        
        start_menu.getChildren().addAll(start_button, quit_button);

    }
}
