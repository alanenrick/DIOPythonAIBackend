<h1>Desafio de código - Dominando os Fundamentos Básicos do Python</h1>

<div><h2>Desafio 01.1</h2>

<p>Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor '<code>float</code>'. Crie uma função chamada <code>recomendar_plano</code> para receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.</p>

<p><strong>Planos Oferecidos:</strong><br>
<br>
- Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.<br>
- Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.<br>
- Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.</p>

<h2>Entrada</h2>

<p>Como entrada solicite o consumo médio mensal de dados em GB (float).</p>

<h2>Saída</h2>

<p>Retorne o plano ideal para o cliente de acordo com o consumo informado na entrada.</p>

<h2>Exemplos</h2>

<p>A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.</p>

<table>
	<thead>
		<tr>
			<th>Entrada</th>
			<th>Saída</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
			<p>10</p>
			</td>
			<td>
			<p>Plano Essencial Fibra - 50Mbps</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>19</p>
			</td>
			<td>Plano Prata Fibra - 100Mbps</td>
		</tr>
		<tr>
			<td>
			<p>21</p>
			</td>
			<td>
			<p>Plano Premium Fibra - 300Mbps</p>
			</td>
		</tr>
	</tbody>
</table> <br><br></div>
--------------------------------------------------------------------------------------------------------------------------

<div><h2>Desafio 01.2</h2>

<p>Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.</p>

<h2>Entrada</h2>

<p>O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.</p>

<h2>Saída</h2>

<p>Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.</p>

<h2>Exemplos</h2>

<p>A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.</p>

<table>
	<thead>
		<tr>
			<th>Entrada</th>
			<th>Saída</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
			<p>Antena<br>
			Roteador<br>
			Switch</p>
			</td>
			<td>
			<p>Lista de Equipamentos:<br>
			- Antena<br>
			- Roteador<br>
			- Switch</p>
			</td>
		</tr>
		<tr>
			<td><br>
			Servidor<br>
			Cabinet Rack<br>
			Access Point<br>
			&nbsp;</td>
			<td>Lista de Equipamentos:<br>
			- Servidor<br>
			- Cabinet Rack<br>
			- Access Point</td>
		</tr>
		<tr>
			<td>
			<p>Edge Routers<br>
			Patch Cord<br>
			UPS</p>
			</td>
			<td>Lista de Equipamentos:<br>
			- Edge Routers<br>
			- Patch Cord<br>
			- UPS</td>
		</tr>
	</tbody>
</table> <br><br></div>

---------------------------------------------------------------------------------------------------

<div><h2>Desafio 01.3</h2>

<p>Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto.</p>

<p><strong>Formato esperado:</strong><br>
O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9. Lembre-se de respeitar os espaços entre os números quando preciso.</p>

<h2>Entrada</h2>

<p>Uma string representando o número de telefone.</p>

<h2>Saída</h2>

<p>Uma mensagem indicando se o número de telefone é válido ou inválido.</p>

<h2>Exemplos</h2>

<p>A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.</p>

<table>
	<thead>
		<tr>
			<th>Entrada</th>
			<th>Saída</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
			<p>(88) 98888-8888</p>
			</td>
			<td>
			<p>Número de telefone válido.</p>
			</td>
		</tr>
		<tr>
			<td><br>
			(11)91111-1111</td>
			<td>Número de telefone inválido.</td>
		</tr>
		<tr>
			<td>
			<p>225555-555</p>
			</td>
			<td>Número de telefone inválido.</td>
		</tr>
	</tbody>
</table> <br><br></div>