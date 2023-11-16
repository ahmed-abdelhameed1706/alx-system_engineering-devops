# fix default nginx file

file { '/etc/default/nginx':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "ULIMIT=\"-n 2000\"\n",
  notify  => Service['nginx']
}

service { 'nginx':
  ensure => running,
  enable => true,
}
