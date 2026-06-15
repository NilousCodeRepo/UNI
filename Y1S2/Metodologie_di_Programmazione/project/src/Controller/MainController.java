package Controller;

import View.MainView;
import Model.UNO;//TODO(nilou): change UNO the MainModel

import javafx.event.EventHandler;
import javafx.event.ActionEvent;

public class MainController
{
    public final MainView view;
    public final UNO model;

    public MainController(MainView view, UNO model)
    {
        this.view = view;
        this.model = model;

        // attach behavior via view API
        EventHandler<ActionEvent> handler = e -> model.incrementPressCount();
        view.setInitialButtonHandler(handler);

        // listen to model changes and ask view to spawn buttons (view handles concrete Button)
        model.pressCountProperty().addListener((obs, oldV, newV) -> {
            view.spawnButton("Spawned " + newV, handler);
        });
    }
}

