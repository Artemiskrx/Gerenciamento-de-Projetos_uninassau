import re
from datetime import datetime, date
from decimal import Decimal, InvalidOperation

def validar_texto(valor, campo):
    valor = valor.strip()
    if not valor:
        raise ValueError(f"{campo} nao pode ficar vazio.")
    return valor

def validar_cpf(cpf):
    cpf = re.sub(r"\D", "", cpf)  # remove pontos e traco
    if len(cpf) != 11 or cpf == cpf[0] * 11:  # tamanho e sequencias iguais
        raise ValueError("CPF invalido.")
    for i in range(9, 11):  # calcula os 2 digitos verificadores
        soma = sum(int(cpf[n]) * (i + 1 - n) for n in range(i))
        digito = (soma * 10 % 11) % 10
        if digito != int(cpf[i]):
            raise ValueError("CPF invalido (digito verificador).")
    return cpf

def validar_email(email):
    email = email.strip()
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        raise ValueError("E-mail invalido.")
    return email

def validar_orcamento(valor):
    try:
        numero = Decimal(str(valor).replace(",", "."))
    except InvalidOperation:
        raise ValueError("Orcamento deve ser um numero.")
    if not numero.is_finite() or numero <= 0:
        raise ValueError("Orcamento deve ser maior que zero.")
    return numero

def validar_prazo(texto):
    try:
        prazo = datetime.strptime(texto.strip(), "%d/%m/%Y").date()
    except ValueError:
        raise ValueError("Prazo invalido. Use o formato DD/MM/AAAA.")
    if prazo < date.today():
        raise ValueError("O prazo nao pode estar no passado.")
    return prazo
