#installing packages
$flask_packages = {
  'flask'    => '2.1.0',
  'Werkzeug' => '2.1.1',
}

$provider = 'pip3'

$flask_packages.each |$package, $version| {
  package { $package:
    ensure   => $version,
    provider => $provider,
  }
}
