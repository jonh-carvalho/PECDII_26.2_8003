## Caso de uso: Comprar produtos

**Objetivo:** Permitir que um cliente encontre produtos, efetue uma compra e receba a confirmação do pedido.

**Ator principal:** Cliente

**Atores secundários:** Sistema de pagamento e serviço de entrega

**Pré-condições:**
- O catálogo de produtos está disponível.
- O cliente possui uma conta ou informa os dados necessários para a compra.
- Os produtos selecionados têm estoque disponível.

**Fluxo principal:**
1. O cliente consulta o catálogo e pesquisa um produto.
2. O sistema apresenta os detalhes, o preço e a disponibilidade do produto.
3. O cliente seleciona a quantidade e adiciona o produto ao carrinho.
4. O cliente revisa o carrinho e inicia o checkout.
5. O cliente informa o endereço de entrega e escolhe a forma de pagamento.
6. O sistema valida os dados e envia a transação ao serviço de pagamento.
7. O pagamento é aprovado e o sistema registra o pedido.
8. O sistema atualiza o estoque e exibe o número do pedido.
9. O cliente recebe a confirmação da compra e o prazo estimado de entrega.

**Fluxos alternativos e exceções:**
- Se o produto estiver esgotado, o sistema informa a indisponibilidade e solicita a atualização do carrinho.
- Se o pagamento for recusado, o sistema informa o cliente e permite tentar outra forma de pagamento.
- Se os dados de entrega forem inválidos, o sistema solicita a correção antes de prosseguir.

**Pós-condições:** O pedido fica registrado com o status correspondente, o estoque é atualizado e o cliente pode acompanhar a entrega.
