import javafx.application.Application;

import javafx.stage.Stage;

import javafx.scene.Scene;

    import javafx.scene.paint.Color;
   
    import javafx.scene.control.Label;
    import javafx.scene.control.Button;
    import javafx.scene.control.TextField;
    
    import javafx.scene.layout.VBox;
    import javafx.scene.layout.GridPane;
    import javafx.scene.layout.StackPane;
    
    

import javafx.geometry.Insets;

//most minimal javafx app with no exceptions or errors
public class CALC extends Application
{
    private String currentInput = "";
    private String operation = "";

    private double firstNumber = 0;
    
    private double calculate(double a, double b, String op)
    {
        switch(op)
        {
            case "+": return a + b;
            case "-": return a - b;
            case "*": return a * b;
            case "/": return a / b;
            default: return b;
        }

    }

    private void handleButton(String text, Label display)
    {
        switch(text)
        {
            case "C":
                {   
                    currentInput = "";
                    firstNumber = 0;
                    operation = "";
                    display.setText("0");
                }
                break;

            case "=":
                {       
                    if(!operation.isEmpty())
                    {
                        double secondNumber = Double.parseDouble(currentInput);
                        double result = calculate(firstNumber, secondNumber, operation);
                        display.setText(String.valueOf(result));
                        currentInput = String.valueOf(result);
                        operation = "";
                    }
                }
            break;

            case "+":
            case "-":
            case "*":
            case "/":
                {
                    if(!currentInput.isEmpty())
                    {
                        firstNumber = Double.parseDouble(currentInput);
                        operation = text;
                        currentInput = "";
                    }
                }
            break;
            
            default:
                {
                    currentInput += text;
                    display.setText(currentInput);
                }

        }
    }

    @Override 
    public void start(Stage stage)
    {
       // StackPane root = new StackPane();
        VBox root = new VBox(10);
        root.setStyle("-fx-background-color: #f0f0f0; -fx-padding: 20;");
        
        Label display = new Label("0");
        display.setStyle("-fx-font-size: 20; -fx-padding:10; -fx-background-color: #fff;");
            
        GridPane grid = new GridPane();
        grid.setHgap(5);
        grid.setVgap(5);
        grid.setPadding(new Insets(10));

//        Button button = new Button("HELLO");
//        TextField text = new TextField();
//        text.setPromptText("Scrivi: ");

//        button.setOnAction(e -> { 
//                                    String name = text.getText();
//                                    System.out.println("Scritto: " + name);
//                                }
//                          );

        String[][] buttons = {
                                {"7", "8", "9", "/"},
                                {"4", "5", "6", "*"},
                                {"1", "2", "3", "-"},
                                {"0", "C", "=", "+"},
                             };
        
        for(int row = 0; row < buttons.length; row++)
        {
            for(int col = 0; col < buttons[row].length; col++)
            {
                final String label = buttons[row][col];//this serves as true final

                Button btn = new Button(label);
                btn.setPrefSize(50,50);
                btn.setOnAction(e -> handleButton(label, display));
                grid.add(btn, col, row);

            }

        }

        root.getChildren().addAll(display, grid);

        Scene scene = new Scene(root, 250, 300);

        stage.setTitle("UNO the GAME");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args)
    {
        launch(args);
    }
}
