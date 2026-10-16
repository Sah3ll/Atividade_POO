# Atividade_POO
# Questão 07

​a. Função da classe Animal e Abstração: A classe Animal serve como um molde geral para juntar tudo o que é comum aos animais (como nome e idade). Ela é a abstração da história porque guarda só o que interessa para o programa, sem detalhar coisas que não importam.  
​
b. Uso de _idade / Encapsulamento: Usamos _idade para proteger a informação e evitar que a alterem de qualquer maneira (tipo meter idades negativas). Assim, qualquer mudança passa obrigatoriamente pelos métodos criados para isso.  
​
c. Vantagem da Herança: Evita trabalho repetido. Em vez de estarmos a criar tudo de novo para cada bicho, o Cachorro, o Gato e o Pássaro já ganham os atributos e métodos todos da classe Animal de borla.  
​
d. Sons diferentes em emitir_som() / Polimorfismo: É o chamado polimorfismo: o método tem o mesmo nome para todos, mas cada bicho sabe exatamente o som que deve fazer ("Au au", "Miau", etc.).  
​
e. Idade negativa: Se não houver controlo, o programa aceita um valor errado sem problema. Para evitar isto logo à nascença, metemos a validação a correr logo dentro do construtor (_init_) quando o objeto é criado
