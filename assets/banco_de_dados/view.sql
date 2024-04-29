CREATE VIEW contrato_detalhes AS
SELECT 
    a.id AS atendimento_id,
    a.data_agendada AS atendimento_data,
    a.placa AS atendimento_placa,
    a.cancelado AS atendimento_cancelado,
    cliente.id AS cliente_id,
    cliente.nome AS cliente_nome,
    cliente.email AS cliente_email,
    f.id AS funcionario_id,
    f.nome AS funcionario_nome, 
    c.id AS contrato_id,
    c.data AS contrato_data,
    c.status AS contrato_status,
    p.data AS pagamento_data,
    p.valor AS pagamento_valor,
    p.desconto AS pagamento_desconto,
    p.valor_total AS pagamento_valor_total,
    p.forma_pagamento AS pagamento_forma,
    car.nome AS carro_nome,
    car.modelo AS carro_modelo,
    car.img AS carro_img,
    s.img AS servico_img,
    s.nome AS servico_nome,
    s.preco AS servico_preco
FROM 
    contrato c
JOIN 
    cliente ON cliente.id = c.cliente_id
LEFT JOIN 
    funcionario f ON f.id = c.Funcionario_id
JOIN 
    Pagamento p ON c.id = p.contrato_id
JOIN 
    atendimento a ON c.id = a.contrato_id
JOIN 
    carro car ON a.carro_id = car.id
JOIN 
    servico s ON a.servico_id = s.id;