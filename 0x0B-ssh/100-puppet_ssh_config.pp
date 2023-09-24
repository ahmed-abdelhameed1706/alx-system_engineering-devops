#Client Configration with Puppet
$ssh_path = '/etc/ssh/ssh_config'

file_line { 'set identity line':
ensure => present,
path   => $ssh_path,
line   => 'IdentityFile ~/.ssh/school'
}

file_line { 'set password line':
ensure => present,
path   => $ssh_path,
line   => 'PasswordAuthentication no'
}
