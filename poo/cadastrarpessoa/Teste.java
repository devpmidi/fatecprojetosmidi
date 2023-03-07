import java.util.Scanner;

public class Teste{
	public static void main(String [] args) {
	
		Pessoa p1 = new Pessoa();
		Pessoa p2 = new Pessoa();
		Scanner entrada = new Scanner (System.in);


		System.out.println("---------------------");
		
		System.out.print("\nDigite o seu id: ");
		p1.idPessoa = entrada.next();
		
		entrada.nextLine();
		System.out.print("\nDigite o seu nome: ");
		p1.nomePessoa = entrada.nextLine();
		
		System.out.print("\nDigite o seu endereço: ");
		p1.enderecoPessoa = entrada.nextLine();
		
		System.out.println("---------------------");
		
		p1.ImprimirPessoa();
		
		System.out.println("---------------------");
		
		System.out.println("proxima pessoa");
		
		System.out.print("\nDigite o seu id: ");
		p2.idPessoa = entrada.next();
		
		entrada.nextLine();
		System.out.print("\nDigite o seu nome: ");
		p2.nomePessoa = entrada.nextLine();
		
		System.out.print("\nDigite o seu endereço: ");
		p2.enderecoPessoa = entrada.nextLine();
		
		System.out.println("---------------------");
		
		p2.ImprimirPessoa();
		System.out.println("---------------------");

		

		
		
	}
}