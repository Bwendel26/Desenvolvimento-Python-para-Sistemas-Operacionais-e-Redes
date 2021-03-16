### 12. Indique uma maneira de criar um processo externo ao seu programa usando o módulo ‘os’ e usando o módulo ‘subprocess’ de Python. Dê um exemplo de cada. <h3>
  

**R:** <p>Através do método os.<b>startfile</b>(<i>path[, operation]</i>) do módulo <b><i>os</i></b> do Python que inicia o arquivo com o programa associado a ele caso exista.</p>
<p>Ex.: os.<b>startfile</b>() <ul><li>os.startfile('C:\Users\Username\text_file.txt')</ul>
Este comando inicia um processo do bloco de notas no windows e abre o arquivo text_file.txt.</p>
<p>Ou então, a partir do módulo subprocess com os.subprocess.<b>Popen</b>(<i>args</i>) do módulo <b><i>os</i></b> que executa o programa descrito por <i>args</i> em um novo processo.</p>
<p>os.subprocess.<b>Popen</b>() <ul><li>os.subprocess.<b>Popen</b>('notepad')</ul></p>