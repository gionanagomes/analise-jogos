def categorizar_horario_dia(hora_inicio):
    if hora_inicio == 'qualquer':
        return 'qualquer horário'
    try:
        hora = int(hora_inicio)
    except ValueError:
        return 'qualquer horário'
    
    if 6 <= hora <= 11:
        return 'manhã'
    elif 12 <= hora <= 17:
        return 'tarde'
    else:
        return 'noite/madrugada'