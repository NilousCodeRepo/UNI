import java.util.Scanner;
import java.net.*;
import java.io.*;

public class client
{
	public static void main(String[] args) throws IOException
	{
        int port = 1337;
        String host = "localhost";
        Socket client = new Socket(host, port);

        //setup message to send to server
        DataOutputStream to_server = new DataOutputStream( client.getOutputStream());

        //setup message to receive from server
        
        BufferedReader from_server = new BufferedReader(
                                        new InputStreamReader( client.getInputStream() ) 
                                        );

        //to read data from the keybard
        BufferedReader kb = new BufferedReader( new InputStreamReader(System.in) );
        
        while(true)
        {
            String s1, s2;

            while( !( (s1 = from_server.readLine() ).equals("exit") ) )
            {
                to_server.writeBytes(s1 + "\n");

                s2 = kb.readLine();
                System.out.println(s1);

            }
            client.close();
       
            //exti the loop
            System.exit(0);
        }

	}

}
