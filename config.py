import base64

userSite = '05107472990'

senhaCod = '' #em base64
senhaSQL = '' #em base64

senhaSite = base64.b64decode(senhaCod).decode('utf-8')
senhaSQL = base64.b64decode(senhaSQL).decode('utf-8')

siteLogin = 'https://www.prppg.ufpr.br/siga/login'
siteAcesso = 'https://www.prppg.ufpr.br/siga/selecionanivelacesso?comboAcesso=TXSEPX40001016070G0XSEPX47XSEPX6XSEPXXSEPX0XSEPX1'
siteDados = f'https://www.prppg.ufpr.br/siga/graduacao/discente?d={id}&aba=informacoes'

idInicial = 39437
idFinal = 85432
