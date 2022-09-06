import base64

userSite = ''

senhaCod = '' #em base64
senhaSQL = '' #em base64

senhaSite = base64.b64decode(senhaCod).decode('utf-8')
senhaSQL = base64.b64decode(senhaSQL).decode('utf-8')

siteLogin = ''
siteAcesso = ''
siteDados = f''

idInicial = 39437
idFinal = 85432
