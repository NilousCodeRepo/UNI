import java.util.Scanner;
class hello
{
	public static void main(String[] args)
	{
		System.out.print("Ciao Java\n");
		System.out.print(args[0]);	
		Scanner in = new Scanner(System.in);
		System.out.print("Inserisci un numero: ");
		int i = in.nextInt();
		for (;; --i)
		{
			System.out.print("Guh\n");
			if(i <= 0)
				return;
		}
	}
}
