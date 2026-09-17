mkdir report
touch summary.txt

$(find "report" -type f | wc -l > summary.txt)
$(find "report" -mindepth 1 -type d | wc -l >> summary.txt) 
$(ls report |  wc -l >> summary.txt)  
cat summary.txt
