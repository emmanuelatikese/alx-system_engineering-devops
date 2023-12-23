#creating a file in tmp

$dealing_file = '/tmp/school'

file { $dealing_file:
ensure  => 'present',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',}
