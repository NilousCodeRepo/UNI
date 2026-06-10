import javafx.fxml.FXML;

import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

public class Controller
{
    @FXML private TextField nameField;
    @FXML private Label messageLabel;
    @FXML private Button submitButton;

    @FXML
    private void initialize()
    {
        submitButton.setOnAction( lambda -> {
                                                String name = nameField.getText().trim();

                                                if(name.isEmpty())
                                                {
                                                    messageLabel.setText("Enter your [name]");
                                                    messageLabel.getStyleClass().setAll("message", "error");
                                                }
                                                else
                                                {
                                                    messageLabel.setText("Hello "+name);
                                                    messageLabel.getStyleClass().setAll("message", "success");
                                                }
                                            } 
                                ); 

    }

    @FXML
    private void onClear() {
        nameField.clear();
        messageLabel.setText("");
        messageLabel.getStyleClass().setAll("message");
    }

}

