<?php

$handle=STDIN;
if(isset($argv[1])) {
    $handle = fopen($argv[1], "r");
}

while(!feof($handle)){
    $line = fgets($handle);
    //Removes URLs
    $line = preg_replace("@(https?://([-\w\.]+[-\w])+(:\d+)?(/([\w/_\.#-]*(\?\S+)?[^\.\s])?)?)@", ' ', $line);    
    //Removes trailing https    
    $line = str_replace("https", ' ', $line);    
    //Removes all punctuation.
	$line = preg_replace('#[[:punct:]]#', ' ', $line);
	//Removes all non-character
	$line = preg_replace('~\P{Xan}++~u', ' ',$line);
	//Removes duplicated whitespace
	$line = preg_replace('/\s+/S', " ",$line);
    
    echo $line;
}

