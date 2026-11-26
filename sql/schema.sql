create database if not exists gerenciamento_projetos
	character set utf8mb4 collate utf8mb4_unicode_ci;
use gerenciamento_projetos;

create table if not exists projetos(
	id int auto_increment primary key,
    nome varchar(100) not null,
	cpf char(11) not null unique,
    cargo varchar(60) not null,
    email varchar(120) not null unique
);
rename table projetos to funcionarios;

create table if not exists projetos(
	id int auto_increment primary key,
    nome varchar(100) not null,
    prazo date not null,
    orcamento decimal(12,2) not null check (orcamento > 0 ),
    descricao text,
    funcionario_id int not null,
    constraint fk_projeto_funcionario
		foreign key (funcionario_id) references funcionarios (id)
        on delete restrict
        on update cascade
);
_____________________________________________________________________________________;


-- insert
insert into funcionarios (nome, cpf, cargo, email)
values ("Carlos Roberto", "55018098318", "Gerente", "carlosSabido@gmail.com");

insert into projetos (nome, prazo, orcamento, descricao, funcionario_id)
values ("Site novo", "2027-01-30", 15000.00, "Refazer site", 1);


-- select (com JOIN, mostrando o relacionamento 1:N)
select p.id, p.nome, p.prazo, p.orcamento, f.nome as responsavel
from projetos p
join funcionarios f on f.id = p.funcionario_id;

-- update
update projetos set orcamento = 18000.00 where id = 1;

-- delete
delete from projetos where id = 1;












