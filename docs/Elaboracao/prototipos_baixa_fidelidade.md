---
title: Protótipos de Baixa Fidelidade
tags:
  - protótipo
  - SALT
  - requisitos
---
# Protótipos de Baixa Fidelidade

Os protótipos abaixo representam o fluxo de inscrição, avaliação, associação de peso e alocação definido no [cenário operacional](../../diagramas/cenario.md). Eles priorizam o conteúdo e as regras de negócio, sem definir cores, identidade visual ou detalhes finais de interação.

## Fluxo do aluno

### 1. Início e inscrição no teste

A tela permite ao aluno consultar o teste do semestre e iniciar uma única inscrição.

```plantuml
@startsalt
{
  {+
    <b>Portal acadêmico</b> | Aluno: Ana Souza | [Sair]
  }
  {
    <b>Teste semestral - 2026/2</b>
    "Descrição:" | Avaliação para composição de carga disciplinar
    "Período:" | 01/09/2026 a 15/09/2026
    "Situação:" | Disponível para inscrição
  }
  {
    "Matrícula:" | "202600123"
    "Curso:" | "Engenharia de Software"
    "Dados acadêmicos:" | "[x] Conferidos"
  }
  {
    [Realizar inscrição] | [Consultar regras]
  }
}
@endsalt
```

### 2. Confirmação e impedimento de duplicidade

A confirmação mostra os dados que serão gravados. A mesma área também comunica a pendência quando já existe inscrição para o teste e semestre.

```plantuml
@startsalt
{
  {+
    <b>Confirmar inscrição</b>
  }
  {
    "Aluno:" | Ana Souza
    "Teste:" | Teste semestral - 2026/2
    "Semestre:" | 2026/2
    "Data:" | 10/09/2026
  }
  {
    "Declaração:" | [x] Confirmo que os dados estão corretos
  }
  {
    [Confirmar inscrição] | [Voltar]
  }
  {
    <b>Resultado da validação</b>
    "Situação:" | Inscrição registrada com sucesso
    "Protocolo:" | INS-2026-000123
  }
}
@endsalt
```

```plantuml
@startsalt
{
  {+
    <b>Inscrição não concluída</b>
  }
  {
    "Situação:" | [!] Pendência de duplicidade
    "Motivo:" | Já existe uma inscrição para este teste no semestre 2026/2.
  }
  {
    "Ação permitida:" | Consultar inscrição existente
  }
  {
    [Ver inscrição] | [Voltar]
  }
}
@endsalt
```

### 3. Resultado e associação do peso

Depois da divulgação do resultado, o aluno escolhe uma disciplina e informa um peso no intervalo de 0 a 1.

```plantuml
@startsalt
{
  {+
    <b>Resultado do teste</b> | Ana Souza
  }
  {
    "Teste:" | Teste semestral - 2026/2
    "Resultado:" | 8,5
    "Status:" | Resultado disponível
  }
  {
    "Disciplina para receber o peso:" | ^Selecione uma disciplina^++
    "Disciplina:" | [ ] Algoritmos II
                     | [ ] Banco de Dados
                     | [ ] Engenharia de Requisitos
    "Peso (0 a 1):" | "0,40"
  }
  {
    [Salvar associação] | [Voltar]
  }
  {
    "Validação:" | O peso deve estar entre 0 e 1, inclusive.
  }
}
@endsalt
```

## Fluxo do administrador

### 4. Cadastro da oferta e validação dos dados

O administrador mantém os dados necessários antes de iniciar a alocação.

```plantuml
@startsalt
{
  {+
    <b>Administração da oferta</b> | [Sair]
  }
  {
    [Testes] | [Cursos] | [Disciplinas] | [Salas] | [Horários]
  }
  {
    <b>Teste semestral - 2026/2</b>
    "Curso vinculado:" | Engenharia de Software
    "Disciplina:" | Algoritmos II
    "Horário:" | Terça, 19:00 - 21:00
    "Sala:" | LAB-02
    "Capacidade:" | 30 alunos
  }
  {
    "Validação dos cadastros:" | [x] Teste  [x] Curso  [x] Disciplina
                                | [x] Horário  [x] Sala  [x] Capacidade
  }
  {
    [Salvar oferta] | [Iniciar alocação]
  }
}
@endsalt
```

### 5. Alocação por curso, horário e capacidade

O painel evidencia a capacidade utilizada e só permite concluir quando não há conflitos nem falta de vagas.

```plantuml
@startsalt
{
  {+
    <b>Alocação de alunos</b> | Teste 2026/2
  }
  {
    "Curso" | "Horário" | "Sala" | "Ocupação" | "Situação"
    "Eng. Software" | Ter 19:00 | LAB-02 | 24 / 30 | OK
    "Eng. Software" | Qui 19:00 | LAB-03 | 30 / 30 | Lotada
    "Sistemas"      | Ter 19:00 | LAB-01 | 18 / 25 | Conflito
  }
  {
    "Alunos pendentes:" | 2
    "Alunos alocados:" | 24
    "Vagas disponíveis:" | 6
  }
  {
    [Executar alocação] | [Ver pendências] | [Exportar resultado]
  }
}
@endsalt
```

### 6. Pendências que impedem a conclusão

Toda inconsistência fica registrada com motivo e ação necessária para o administrador.

```plantuml
@startsalt
{
  {+
    <b>Pendências da alocação</b> | [Voltar ao painel]
  }
  {
    "Aluno / registro" | "Motivo" | "Ação"
    "Ana Souza" | Dados acadêmicos incompletos | Corrigir cadastro
    "Bruno Lima" | Capacidade insuficiente | Disponibilizar outra sala
    "Carla Reis" | Conflito de horário | Revisar oferta
  }
  {
    <b>Alocação automática bloqueada</b>
    "Regra:" | Todas as pendências devem ser resolvidas antes da conclusão.
    "Status:" | [!] Aguardando correção do administrador
  }
  {
    [Corrigir pendência selecionada] | [Atualizar validação]
  }
}
@endsalt
```

## Regras representadas

- Uma inscrição por aluno, teste e semestre.
- Dados acadêmicos obrigatórios e previamente cadastrados.
- Peso numérico entre 0 e 1, inclusive, associado a uma disciplina.
- Alocação condicionada à existência de curso, horário, sala e capacidade.
- Duplicidade, dados inválidos, conflito de horário e falta de vagas geram pendências e bloqueiam a conclusão automática.

## Fonte editável

O código completo das telas está disponível em [prototipos_baixa_fidelidade.puml](../../diagramas/prototipos_baixa_fidelidade.puml).
