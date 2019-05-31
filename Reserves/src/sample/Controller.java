package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import java.sql.SQLException;


public class Controller {
    static Stage finestra;

    @FXML
    TextField client;
    @FXML
    Text Res;
    @FXML
    TextArea dataEntrada;

    static void getPrimaryStage(Stage stage) {
        finestra = stage;
    }


    @FXML
    private void setReserva(ActionEvent event) throws SQLException {
        String entrada;
        entrada = dataEntrada.getText();
        int client_reserva = Integer.parseInt(client.getText()) ;
        Res.setText(clients.insertReserva(entrada,client_reserva));

    }

}
