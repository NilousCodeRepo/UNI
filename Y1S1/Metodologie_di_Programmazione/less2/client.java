import java.util.Scanner;
import java.net.*;
import java.io.*;

public class client
{
	public static void main(String[] args) throws IOException
	{
		System.out.println("======================= Lezione 2 =======================");
		
		//CONFIG CLIENT
		int port = 1337;
		String ip = new String("localhost");

		Socket socket = new Socket(ip, port);
		
		PrintWriter to_server = new PrintWriter(socket.getOutputStream(), true);

		BufferedReader from_server = new BufferedReader( new InputStreamReader(socket.getInputStream()) );

		String message = from_server.readLine();
		System.out.println("> "+message);

		socket.close();
	}

}
