package Controller;

import View.MainView;
import Model.UNO;//TODO(nilou): change UNO the MainModel

import javafx.event.EventHandler;
import javafx.event.ActionEvent;

public class MainController
{
    public final MainView view;
    public final UNO model;

    public MainController(MainView arg_view, UNO arg_model)
    {
        this.view = arg_view;//quindi this si riferisce all'oggetto
        this.model = arg_model;

        // attach behavior via view API
        EventHandler<ActionEvent> handler = e -> model.incrementPressCount();
        view.setInitialButtonHandler(handler);

        // listen to model changes and ask view to spawn buttons (view handles concrete Button)
        model.pressCountProperty().addListener((obs, oldV, newV) -> {
            view.spawnButton("Spawned " + newV, handler);
        });
    }
}

