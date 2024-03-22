# Using Puppet, install flask and pip3

exec { 'flask':
  ensure   => 'flask=2.1.0',
  provider => 'pip3',
}
