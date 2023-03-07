/*arquivo Pessoa.java*/ 

public class Pessoa{
	
/* atributos */
	public String idPessoa;
	public String nomePessoa;
	public String enderecoPessoa;
	
/* métodos*/
	public void ImprimirPessoa(){
		System.out.println("Id: "+ this.idPessoa);
		System.out.println("Nome: "+ this.nomePessoa);
	System.out.println("Endereço: "+this.enderecoPessoa);
	}
}