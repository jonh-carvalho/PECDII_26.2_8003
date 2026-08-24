Os padrões locais confirmam que o cenário deve separar contexto, atores, regras de negócio e fluxos de uso. O texto atual deixa quatro decisões centrais abertas: o significado da pontuação, quando a disciplina é escolhida, como funciona a alocação e qual é o limite do sistema; vou confirmar essas escolhas para fechar um plano executável.

Com isso, a interpretação fica consistente: o teste gera um peso entre 0 e 1, aplicado a uma disciplina escolhida depois do resultado; a faculdade aloca por curso e horário, respeitando salas. Falta apenas fixar as regras operacionais mínimas para o cenário não depender de suposições escondidas.


As regras operacionais estão fechadas: uma inscrição por aluno/teste/semestre, dados acadêmicos e de salas previamente cadastrados, administrador responsável e pendências explícitas quando a capacidade ou o horário impedirem a alocação. Vou registrar agora o plano final, limitado ao cenário-fonte e sem tocar no site gerado.


## Plan: Cenário Preciso Da Prova

Reescrever `cenario.md` em português, transformando o texto atual em um cenário operacional claro para servir de base aos requisitos e casos de uso.

**Steps**

1. Organizar o documento em: contexto, problema, objetivo, atores, dados, regras de negócio e escopo.
2. Descrever a inscrição do aluno no teste semestral, permitindo apenas uma inscrição por teste e semestre.
3. Explicar que, após o resultado, o aluno escolhe uma disciplina e associa a ela um peso entre `0` e `1`.
4. Descrever a atuação do administrador da faculdade, responsável por testes, cursos, disciplinas, salas, capacidades e horários.
5. Definir a alocação dos alunos por curso e horário, respeitando a capacidade das salas.
6. Registrar exceções: inscrição duplicada, dados inválidos, conflito de horário ou falta de vagas geram pendências e impedem a conclusão automática.
7. Delimitar o escopo: incluir inscrição, resultado/peso e alocação; deixar aplicação presencial, presença, correção e notificações fora do cenário.

**Arquivos relevantes**

- `cenario.md` — único arquivo a ser alterado.
- `documento_de_visao.md` — referência para estrutura de problema, objetivos, usuários e restrições.
- `casos_de_uso.md` — referência para fluxos principais, alternativas e pós-condições.

**Verificação**

1. Conferir se inscrição, associação da pontuação e alocação estão explicitamente descritas.
2. Confirmar as regras validadas: uma inscrição, administrador responsável, salas previamente cadastradas e pendências em conflitos.
3. Executar `mkdocs build --strict` ou o comando equivalente documentado no `README.md`.

**Decisões**

- A pontuação de `0` a `1` representa o peso usado na composição da nota da disciplina.
- O aluno escolhe uma disciplina após receber o resultado.
- A alocação considera curso, horário e capacidade das salas.
- A distribuição detalhada da nota entre várias disciplinas permanece fora do escopo.
- A política de desempate entre salas também ficará para uma definição futura.
