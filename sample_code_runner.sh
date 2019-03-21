FILECOUNT=0
find samples -print | grep -i -e "\.py$"    > list.txt

set -e 
while IFS="" read -r p || [ -n "$p" ]
do
  if [[ "$p" =~ $(echo ^\($(sed 's/[[:blank:]]//g' sampleCodeIgnoreList.txt | paste -sd '|' /dev/stdin)\)$) ]]; then
    printf '\n#### SKIPPED - %s ####\n' "$p"
  else
    printf '\n\n**** RUNNING - %s ****\n' "$p"
	FILECOUNT=$((FILECOUNT+1))
  fi
  python $p
done < list.txt
printf '\n\n**** %s Sample Codes ran successfully ****\n' "$FILECOUNT"