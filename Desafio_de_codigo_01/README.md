<h1>Desafio de código - Dominando os Fundamentos Básicos do Python</h1>

<div><h2>Desafio</h2>

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
-------------------------------------------------------
<div class="row"><div class="col-md-12"><p class="mb-1"><strong>Dica: Python</strong></p>
  <p>Em Python existe várias formas de implementar o STDIN e STDOUT recomendamos utilizar <strong>sys.stdin.readline</strong> para o STDIN e o <strong>print</strong> para o STDOUT.</p>
  <p class="mb-1"><strong class="mb-1">Exemplo:</strong><pre class="mb-0">import sys</pre><pre class="mb-0">a = int(sys.stdin.readline()) // Lê a linha de entrada</pre><pre>print(a); // Imprime o dado</pre>
</p>
</div>
</div>
