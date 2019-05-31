package sample;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDate;

public class clients {
    public static String insertReserva(String entrada,int client_id) throws SQLException
    {
        try {
            DBAccess.setData("INSERT INTO reserva_reserva VALUES ("+(findlastReserva()+1)+",'{"+entrada+"}','True','True','"+client_id+"')");
        } catch (SQLException e) {
            e.printStackTrace();
            DBAccess.closeConnection();
            return "err2";
        }
        DBAccess.closeConnection();
        return "done";
    }
    public static int findlastReserva() throws SQLException {
        int ultimaReserva = 0;
        ResultSet resultatReserva = DBAccess.getData("select * from reserva_reserva order by id asc");
        while (resultatReserva.next()) {
            ultimaReserva = resultatReserva.getInt(1);
        }
        DBAccess.closeConnection();
        return ultimaReserva;
    }
}
