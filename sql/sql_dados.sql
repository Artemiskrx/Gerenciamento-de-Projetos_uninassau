-- INSERT
INSERT INTO funcionarios (nome, cpf, cargo, email)
VALUES ('Ana Souza', '52998224725', 'Gerente', 'ana@empresa.com');
INSERT INTO projetos (nome, prazo, orcamento, descricao, funcionario_id)
VALUES ('Site novo', '2027-03-31', 15000.00, 'Redesenho do site', 1);

-- SELECT (com JOIN, mostrando o relacionamento 1:N)
SELECT p.id, p.nome, p.prazo, p.orcamento, f.nome AS responsavel
FROM projetos p
JOIN funcionarios f ON f.id = p.funcionario_id;

-- UPDATE
UPDATE projetos SET orcamento = 18000.00 WHERE id = 1;

-- DELETE
DELETE FROM projetos WHERE id = 1;