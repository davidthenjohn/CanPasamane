package sample;
import java.sql.*;

public class DBAccess {
    static Connection connection = null;
    public static Connection openConnection()
    {
        try {
            final String password = "DavidJuan020717";
            final String user = "postgres";
            Class.forName("org.postgresql.Driver");
            connection = DriverManager.getConnection("jdbc:postgresql://localhost:5432/CanPasamane", user, password);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return connection;
    }
    public static void closeConnection() {
        try {
            connection.close();
        } catch (SQLException e) {

            e.printStackTrace();
        }
    }
    public static ResultSet getData(String sql) throws SQLException {
        connection = openConnection();
        Statement statement = connection.createStatement();
        return statement.executeQuery(sql);
    }
    public static int setData(String sql) throws SQLException {
        connection = openConnection();
        Statement statement = connection.createStatement();
        return statement.executeUpdate(sql);
    }
}
