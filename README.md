Hacer maquina virtual


cat data.tok | tr ' ' "\n" |tr '[:upper:]' '[:lower:]' | awk 'NF' | sort | uniq -c |sort | tail -n 100 | sed 's/^.\{8\}//g' 


