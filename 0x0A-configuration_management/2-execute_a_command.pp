#manifest to kill a process
exec {'execute_a_command':
  command => 'pkill -f "killmenow"',
}
