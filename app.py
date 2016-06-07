import mod_wsgi.server

mod_wsgi.server.start(
  '--log-to-terminal',
  '--port', '8080',
  '--trust-proxy-header', 'X-Forwarded-For',
  '--trust-proxy-header', 'X-Forwarded-Port',
  '--trust-proxy-header', 'X-Forwarded-Proto',
  '--url-alias', '/static/', './static/',
  '--application-type', 'module',
  '--entry-point', 'demo.wsgi',
)
