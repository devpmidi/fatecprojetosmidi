/*arquivo Calendario.java*/ 

import java.util.Calendar;

public class Calendario{
	
/* atributos */
	public String idPessoa, nomePessoa, enderecoPessoa;
	public int nascimentoPessoa;
	
/* m�todos*/
	public void Informacao(){
	System.out.println("Id: "+ this.idPessoa);
	System.out.println("Nome: "+ this.nomePessoa);
	System.out.println("Endere�o: "+this.enderecoPessoa);
	System.out.println("Sua idade neste ano: " +this.calcularIdade(this.nascimentoPessoa));
	}
	
	public int calcularIdade(int nascimentoPessoa){
		Calendar calendario = Calendar.getInstance();
		int anoAtual = Calendar.YEAR;
		return calendario.get(anoAtual) - nascimentoPessoa;
	}
}