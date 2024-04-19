#checking the performance of the server base onthe number of requests

exec { 'solving nginx':
    command => "sed -i 's/15/4096/' /etc/default/nginx",
    path    => '/usr/local/bin/:/bin/'
}

->exec { 'nginx start again':
    command => 'nginx restart',
    path    => '/etc/init.d/'
}
