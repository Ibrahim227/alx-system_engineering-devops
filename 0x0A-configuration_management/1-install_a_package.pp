# Using Puppet, install flask and pip3

exec { 'flask':
  ensure   => '2.1.0',
  provider => 'python3-pip',
}
