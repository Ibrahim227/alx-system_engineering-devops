#Install a specific flask

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install werkzeug==2.1.1',
  path    => '/usr/bin',
}

