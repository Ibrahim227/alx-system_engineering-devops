# Using Puppet, install flask and pip3

exec { 'install_flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
