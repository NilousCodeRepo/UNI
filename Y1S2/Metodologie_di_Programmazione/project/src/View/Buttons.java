package View;

import javafx.scene.control.Button;
import javafx.event.EventHandler;
import javafx.event.ActionEvent;

class Buttons 
{
    public Button createButton(String text, EventHandler<ActionEvent> handler) 
    {
        Button btn = new Button(text);
        if (handler != null) btn.setOnAction(handler);//i store the handler as the action to execute i.e. lambda inside the handler

        return btn;
    }
}
