-- SELECT (com JOIN, mostrando o relacionamento 1:N)
SELECT p.id, p.nome, p.prazo, p.orcamento, f.nome AS responsavel
FROM projetos p
JOIN funcionarios f ON f.id = p.funcionario_id;

-- UPDATE
UPDATE projetos SET orcamento = 18000.00 WHERE id = 1;

-- DELETE
DELETE FROM projetos WHERE id = 1;