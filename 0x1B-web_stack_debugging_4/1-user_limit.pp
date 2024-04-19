# just working on the limit

exec { 'more hard file limit':
    command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/'
}

exec { 'more on soft file':
    command => 'sed -i "/holberton soft/s/4/50000/" /etc/sercurity/limits.conf',
    path    => '/usr/local/bin/:/bin/'
}
