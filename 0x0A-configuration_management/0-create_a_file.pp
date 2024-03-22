file { '/tmp/0-create_a_file.pp':
    ensure  => 'present',
    mode    => '0744',
    path    => '/tmp/0-create_a_file.pp',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
