package sample;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("reserva.fxml"));
        primaryStage.setTitle("CanPasamane");
        primaryStage.setScene(new Scene(root));
        DBAccess.openConnection();
        primaryStage.show();
        Controller.getPrimaryStage(primaryStage);
    }


    public static void main(String[] args) {
        launch(args);
    }
}
