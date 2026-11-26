create database if not exists gerenciamento_projetos
	character set utf8mb4 collate utf8mb4_unicode_ci;
use gerenciamento_projetos;

create table if not exists funcionarios(
	id int auto_increment primary key,
    nome varchar(100) not null,
	cpf char(11) not null unique,
    cargo varchar(60) not null,
    email varchar(120) not null unique
);

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



