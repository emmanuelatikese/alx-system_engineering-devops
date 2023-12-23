#kill a file
exec { 'kill':
  path	  => ['usr/bin/', '/bin'],
  command => 'pkill -f killmenow',
}
