CREATE PROCEDURE `dias_disponiveis` ()
BEGIN
    DECLARE total_funcionarios INT;
    SELECT COUNT(*) INTO total_funcionarios FROM funcionario;

    SELECT 
        data_agendada, 
        COUNT(*) as quantidade_atendimentos,
        total_funcionarios
    FROM 
        atendimento
    WHERE
        data_agendada > CURDATE()
    GROUP BY 
        data_agendada;

    IF ROW_COUNT() = 0 THEN
        SELECT 
            total_funcionarios;
    END IF;
END
