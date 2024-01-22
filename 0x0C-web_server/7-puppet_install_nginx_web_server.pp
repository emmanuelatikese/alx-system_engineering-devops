# Update package repositories

exec { 'dist update':
        command  => '/usr/bin/apt-get update',
        provider => 'shell'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['dist update']
}

file {'/var/www/html/index.html':
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
  owner   => $USER,
  group   => $USER,
  mode    => '0644',
}

exec {'redirect_me':
  command  => "sed -i '20i\\
        location ~ redirect_me {\\
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\\
        }' /etc/nginx/sites-available/default",
  provider => 'shell'
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
