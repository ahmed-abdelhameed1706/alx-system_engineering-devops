# manifist to fix apache 500 internal server error

exec { 'fixing':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin/', '/usr/loca/bin/']
}
