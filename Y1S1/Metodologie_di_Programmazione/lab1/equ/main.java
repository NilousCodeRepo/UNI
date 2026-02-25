package equ;
import java.util.Scanner;

public class main
{
	public static void main(String args[])
	{
		System.out.println("Inserire 3 variabli: ");
		Scanner input = new Scanner(System.in);
		double v[] = new double[3];
		for(int i = 0; i < v.length; ++i)
		{
			double a = input.nextDouble();
			v[i] = a;
		}
		System.out.println( (v[0]*v[1]) + (v[0]/v[2])*v[1] );
	}
		
}
