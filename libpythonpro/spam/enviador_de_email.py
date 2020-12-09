class Enviador:
    def __init__(self):
        self.qtd_email_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailEnvalido(f'Email de remetente inválido: {remetente}')
        self.qtd_email_enviados += 1
        return remetente


class EmailEnvalido(Exception):
    print('Foi Encontrado um email invalido ao tentar enviar!!')
    pass
