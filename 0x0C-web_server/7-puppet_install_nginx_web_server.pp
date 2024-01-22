# Update package repositories
exec { 'dist_update':
  command  => 'sudo apt update',
  path     => ['/bin', '/usr/bin'],  # Specify the PATH to resolve the issue
  provider => 'shell',
}

# Install Nginx package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['dist_update'],
}

# Create index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  owner   => $USER,
  group   => $USER,
  mode    => '0644',
}

# Use sed to insert the location block
exec { 'insert_redirect_location':
  command => "sudo sed -i '20i\\
    location ~ redirect_me {\\
        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\\
    }' /etc/nginx/sites-available/default",
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
