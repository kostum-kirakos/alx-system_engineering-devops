# Killing a process named killmenow.
exec { 'killMeNow':
  command => '/usr/bin/pkill -f killmenow'
}
