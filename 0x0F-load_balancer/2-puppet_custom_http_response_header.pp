#this is all about the puppet
# This is about automations

exec {'update':
        command => 'sudo apt update',
        provider => 'shell'
}

package {'nginx':
        ensure => 'installed',
        required => Exec['update']
}

file {'/var/www/html/index.html':
        content => 'Hello World!',
        owner => 'ubuntu',
        group => 'ubuntu',
        mode => '762',
}

exec { 'redirect_me':
        command => 'sed -i "21i\	location ~ redirect_me {\n\trewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n}" /etc/nginx/sites-available/default',
        provider => 'shell'
}

exec {'adding header':
        command => 'sed -i "5i\ add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
        provider => 'shell'
}

service {'nginx':
        ensure => 'running',
        require => Package['nginx']
}
