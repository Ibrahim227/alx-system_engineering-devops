$dir_root = '/tmp'

file { $dir_root:
    ensure  => 'directory',
    mode    => '0744',
    path    => '/tmp',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
