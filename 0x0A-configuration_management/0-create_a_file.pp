file { '/tmp/school':
    ensure  => 'school',
    mode    => '0744',
    path    => '/tmp',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
