import java.io.*;
import java.net.*;

class server
{
	public static void main(String args[]) throws IOException
	{
		int port = 1337;
		ServerSocket server_socket = new ServerSocket(port);
		Socket accept_req = server_socket.accept();

		BufferedReader from_client = new BufferedReader( new InputStreamReader( accept_req.getInputStream() ) );

		PrintWriter to_client = new PrintWriter(accept_req.getOutputStream(), true);

		String message = from_client.readLine();
		System.out.println("> "+message);
		
		server_socket.close();
		accept_req.close();
	}

}
