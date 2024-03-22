file { '/tmp':
    ensure  => 'present',
    mode    => '0744',
    path    => '/tmp',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
