# Cenário: Inscrição, avaliação e alocação de alunos em disciplinas por teste semestral

## 1. Contexto
A faculdade realiza, em cada semestre, um teste acadêmico para avaliar o desempenho dos alunos em um contexto de seleção e composição de carga disciplinar. O processo envolve a inscrição do aluno em um teste específico, a validação dos dados acadêmicos e da disponibilidade de vagas e horários, a atribuição de um resultado e a posterior escolha de disciplina pela qual o aluno deseja receber a ponderação correspondente.

O cenário descrito abrange apenas a operação de inscrição, resultado, associação de peso e alocação. A gestão do ambiente presencial, presença, correção, comunicação e notificações não faz parte deste contexto.

## 2. Problema
A instituição precisa controlar de forma consistente e segura o processo de inscrição e alocação de alunos em testes e disciplinas, sem permitir duplicidade, inconsistências de dados, conflitos de horários ou uso indevido da capacidade das salas. Sem um cenário operacional bem definido, a instituição corre o risco de:

- aceitar mais de uma inscrição por aluno para o mesmo teste e semestre;
- registrar dados incompletos ou inválidos;
- atribuir disciplina, peso ou horário sem respeitar os limites definidos;
- gerar alocações automáticas sem evidenciar pendências quando a operação não pode ser concluída;
- operar sem responsabilidade clara sobre o cadastro de cursos, disciplinas, salas, horários e capacidade.

## 3. Objetivo
Definir um cenário operacional claro que permita descrever e validar os requisitos do sistema, garantindo que:

- cada aluno possa se inscrever apenas uma vez em cada teste por semestre;
- o resultado do teste seja associado a um peso entre 0 e 1;
- o aluno escolha uma disciplina para receber esse peso;
- a faculdade aloque os alunos em cursos/horários respeitando a capacidade das salas;
- conflitos e inconsistências gerem pendências explícitas e impeçam a conclusão automática da alocação.

## 4. Atores

### 4.1 Aluno
- realiza inscrição no teste semestral;
- informa ou confirma dados acadêmicos necessários;
- recebe o resultado do teste;
- escolhe uma disciplina para associação do peso;
- não participa diretamente da definição da alocação final, exceto pela sua presença no processo de inscrição e escolha de disciplina.

### 4.2 Administrador da faculdade
- cadastra e mantém testes, cursos, disciplinas, salas, horários e capacidades;
- valida e acompanha as inscrições;
- verifica pendências e impede a execução automática quando há inconsistência;
- acompanha a alocação final dos alunos por turma, curso e horário.

### 4.3 Sistema
- valida regras de negócio;
- impede registros duplicados e inválidos;
- registra pendências quando determinada operação não pode ser concluída;
- realiza a alocação respeitando capacidade de sala e disponibilidade de horário.

## 5. Dados do cenário
Os dados relevantes são os seguintes:

- aluno: identificador, dados acadêmicos, histórico mínimo necessário para inscrição;
- teste: identificador, semestre, descrição, curso ou conjunto de cursos vinculados;
- inscrição: aluno, teste, semestre, data de inscrição, dados válidos e estado da inscrição;
- resultado do teste: nota ou classificação atribuída ao aluno;
- disciplina: identificador, curso, nome, turno ou período de oferta;
- peso: valor numérico no intervalo de 0 a 1, associado a uma disciplina escolhida pelo aluno após o resultado;
- curso: identificador, nome, turma, turno e horário;
- sala: identificador, capacidade, curso ou uso permitido;
- horário: período de aula disponível para o curso;
- capacidade da sala: número máximo de alunos permitidos;
- pendência: registro de impedimento para conclusão da alocação, conforme motivo.

## 6. Regras de negócio

### 6.1 Inscrição
- Cada aluno pode realizar apenas uma inscrição por teste e por semestre.
- A inscrição só é aceita se os dados acadêmicos do aluno forem válidos e estiverem previamente cadastrados.
- Caso o aluno tente se inscrever novamente para o mesmo teste no mesmo semestre, o sistema deve registrar a duplicidade como falha de regra.
- A inscrição não pode ser concluída quando houver dados obrigatórios ausentes ou inconsistentes.

### 6.2 Resultado e associação de peso
- Após a realização do teste, o resultado é disponibilizado ao aluno.
- O aluno escolhe uma disciplina que receberá a ponderação do teste.
- O peso deve estar no intervalo de 0 a 1, inclusive.
- O peso representa a contribuição dessa avaliação na composição da nota da disciplina escolhida.
- A distribuição detalhada do peso entre múltiplas disciplinas não faz parte deste cenário.

### 6.3 Administração da faculdade
- O administrador é responsável pelo cadastro e manutenção de testes, cursos, disciplinas, salas, capacidades e horários.
- A faculdade deve manter os dados cadastrais em estado consistente antes da alocação.
- Caso os dados de sala, curso ou horário estejam incompletos, a alocação não pode ocorrer automaticamente.

### 6.4 Alocação por curso, horário e sala
- A alocação considera curso, horário e capacidade das salas.
- Cada aluno deve ser alocado em um curso e em um horário compatível com a oferta e com a disponibilidade da sala.
- A alocação só é concluída quando houver espaço na sala e não houver conflito de horário.
- A instituição deve respeitar tanto a capacidade da sala quanto os horários previamente definidos.

### 6.5 Pendências e impedimentos
- Inscrição duplicada gera pendência e impede a conclusão automática do processo.
- Dados inválidos ou incompletos geram pendência.
- Conflito de horário entre curso, disciplina ou aluno gera pendência.
- Falta de vagas ou capacidade insuficiente na sala gera pendência.
- Quando uma pendência é identificada, o processo deve ser interrompido até que o problema seja resolvido pelo administrador ou pela operação responsável.

## 7. Fluxo operacional do cenário

1. O administrador cadastra os dados do teste, do curso, das disciplinas, das salas, das capacidades e dos horários disponíveis.
2. O aluno realiza a inscrição no teste semestral, respeitando a regra de uma inscrição por teste e semestre.
3. O sistema valida dados acadêmicos e aplicação da regra de unicidade.
4. O teste é realizado e o resultado é registrado.
5. O aluno escolhe uma disciplina e informa o peso desejado, dentro do intervalo de 0 a 1.
6. O sistema verifica a consistência das informações e a disponibilidade para a alocação.
7. A faculdade aloca o aluno em um curso e horário conforme a sala disponível e a capacidade permitida.
8. Se houver impedimento, o sistema registra pendência e a alocação não é concluída automaticamente.

## 8. Escopo do cenário
Este cenário inclui:

- inscrição do aluno em teste semestral;
- validação da unicidade da inscrição;
- registro do resultado do teste;
- escolha da disciplina e atribuição do peso entre 0 e 1;
- alocação do aluno em curso/horário de acordo com a capacidade das salas;
- registro de pendências para inconsistências e conflitos.

## 9. Fora de escopo
O presente cenário não inclui:

- aplicação presencial do teste;
- controle de presença do aluno;
- correção manual ou automatizada das provas;
- notificações e comunicações ao aluno;
- processo de matrícula acadêmica em sentido amplo;
- logística de ambiente físico fora da alocação de salas e horários;
- políticas futuras de desempate entre salas;
- cálculo detalhado da nota final em múltiplas disciplinas.

## 10. Resumo do cenário
O processo é regido por regras claras de unicidade, consistência e capacidade. O aluno realiza uma única inscrição por teste e semestre, recebe o resultado, associa um peso de 0 a 1 a uma disciplina escolhida e, em seguida, a faculdade aloca esse aluno em curso e horário, respeitando salas, capacidade e pendências. O cenário define a base operacional para a criação dos requisitos e dos casos de uso associados ao sistema, sem incluir atividades acadêmicas ou administrativas fora do escopo da inscrição, ponderação e alocação.
