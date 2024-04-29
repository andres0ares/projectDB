CREATE VIEW contrato_detalhes_com_confirmacao AS
SELECT 
    cd.*,
    COALESCE(ca.confirmado, bo.confirmado, pi.confirmado, be.confirmado) AS confirmacao_pagamento
FROM 
    contrato_detalhes cd
LEFT JOIN 
    cartao ca ON cd.contrato_id = ca.Pagamento_contrato_id
LEFT JOIN 
    boleto bo ON cd.contrato_id = bo.Pagamento_contrato_id
LEFT JOIN 
    pix pi ON cd.contrato_id = pi.Pagamento_contrato_id
LEFT JOIN 
    berries be ON cd.contrato_id = be.Pagamento_contrato_id;
