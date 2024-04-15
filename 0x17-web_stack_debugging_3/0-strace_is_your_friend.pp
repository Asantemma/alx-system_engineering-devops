# Finds out why Apache is returning a 500 error and fixes using strace.
exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}