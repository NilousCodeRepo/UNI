package View;

import javafx.scene.control.Button;
import javafx.event.EventHandler;
import javafx.event.ActionEvent;

class Buttons 
{
    public Button createButton(String text, EventHandler<ActionEvent> handler) 
    {
        Button btn = new Button(text);
        if (handler != null) btn.setOnAction(handler);

        return btn;
    }
}
