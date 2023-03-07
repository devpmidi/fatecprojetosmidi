import java.util.Scanner;

public class TesteCalendario{
	public static void main(String[] args){
		Scanner entrada = new Scanner (System.in);
		Calendario p1 = new Calendario();
		
		System.out.println("---------------------");
		
		System.out.print("Digite o Id: ");
		p1.idPessoa = entrada.next();
		
		entrada.nextLine();
		System.out.print("\nDigite o seu nome: ");
		p1.nomePessoa = entrada.nextLine();
		
		System.out.print("\nDigite o seu endereço: ");
		p1.enderecoPessoa = entrada.nextLine();
		
		System.out.print("\nDigite o ano de nascimento: ");
		p1.nascimentoPessoa = entrada.nextInt();
		
		System.out.println("---------------------");
		
		p1.Informacao();

	}
}