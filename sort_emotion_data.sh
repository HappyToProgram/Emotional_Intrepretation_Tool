#!/bin/bash

# Starting directory must be given:
echo "Enter the path of the IEMOCAP directory:"
read DIR_PATH

# cd to directory 
cd $DIR_PATH

# Make folder for each emotion
EMOTIONS=( "Neutral" "Frustration" "Anger" "Sadness" "Excited" "Other" "Happiness" "Surprise" "Fear" "Disgust" )

# Make One Big Directory
mkdir Sorted

for emotion in ${EMOTIONS[@]}
do
	mkdir "$DIR_PATH/Sorted/$emotion"
done

# Search:
for session in $(ls | egrep "Session[0-9]")
do
	echo "Working on $session..."
	cd $DIR_PATH/$session/dialog/EmoEvaluation/Categorical
	TEXTFILELIST1=$(ls | egrep "Ses0[0-9][MF]_impro0[0-9]_.*_cat\.txt" | sort -n | uniq -w 16)
	TEXTFILELIST2=$(ls | egrep "Ses0[0-9][MF]_script0[0-9]_.*_cat\.txt" | sort -n | uniq -w 19)
	TEXTFILELIST=$TEXTFILELIST1" "$TEXTFILELIST2
	#echo $TEXTFILELIST
	for textfile in $TEXTFILELIST
	do
		echo "Reading $textfile..."
		FOLDER_PATH=$(sed 's/_e[0-9]*_cat.txt//' <<<"$textfile")
		#echo "cd to $DIR_PATH/$session/sentences/wav/$FOLDER_PATH"
		cd $DIR_PATH/$session/sentences/wav/$FOLDER_PATH
		
		while read -r line
	       	do
			WAVFILE=$(awk '{ print $1 }' <<<"$line")
			EMOTION=$(awk '{ print $2 }' <<<"$line" | sed 's/://; s/;//')
			#echo $WAVFILE $EMOTION
			if ! [[ -f "$WAVFILE.wav" ]]
			then echo "FILE IS NOT FOUND. $session/sentences/wav/$FOLDER_PATH $WAVFILE"
			fi
			if ! [[ -d $DIR_PATH/Sorted/$EMOTION ]]
			then echo "FOLDER DOES NOT EXIST FOR EMOTION: $EMOTION"
			fi

			# Copy Files:
			cp $DIR_PATH/$session/sentences/wav/$FOLDER_PATH/$WAVFILE.wav $DIR_PATH/Sorted/$EMOTION

		done < $DIR_PATH/$session/dialog/EmoEvaluation/Categorical/$textfile
	done
done
