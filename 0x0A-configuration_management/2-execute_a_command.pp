#manifest to kill a process
exec {'executeacommand':
  command => 'pkill -f "killmenow"',
}
