# Update package repositories
apt::update { 'dist_update':
  before => Package['nginx']
}

# Install Nginx package
package { 'nginx':
  ensure  => 'installed',
  require => Apt::Update['dist_update'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '7624',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('module_name/nginx_config.erb'), # Use a template for better readability and maintainability
  require => File['/var/www/html/index.html'],
  notify  => Service['nginx'],
}

nginx::resource::vhost { 'default':
  ensure   => present,
  vhost    => true,
  require  => File['/etc/nginx/sites-available/default'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
