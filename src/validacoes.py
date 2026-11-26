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
    if len(cpf) != 11:
        raise ValueError("CPF invalido.")
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
