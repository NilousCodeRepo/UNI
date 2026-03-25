import java.io.*;
import java.net.*;

class server
{
	public static void main(String args[]) throws IOException
	{
		int port = 1337;
		ServerSocket server = new ServerSocket(port);
        Socket client = server.accept();//it's blocking, it waits, no while required
        System.out.println("SUCCESSO: connessione al server dal client");

        //setp messages to the client
        PrintStream to_client = new PrintStream(client.getOutputStream());

        //setup messages from client
        BufferedReader from_client = new BufferedReader(
                                        new InputStreamReader( client.getInputStream() ) 
                                        );
        //to read data from the keybard
        BufferedReader kb = new BufferedReader( new InputStreamReader(System.in) );

        String client_message = from_client.readLine();
        
        while(true)
        {
            String s1, s2;

            while( !( (s1 = from_client.readLine() ).equals("exit") ) )
            {
                System.out.println(s1);
                s2 = kb.readLine();

                to_client.println(s2);
            }
            client.close();
            server.close();
       
            //exti the loop
            System.exit(0);
        }
        
	}
}
