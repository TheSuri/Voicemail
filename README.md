Voicemail

USAGE:
***************************************************************************************************************************
To use command line arguments use as: 
"python Voicemail.py"

Follow instructions on screen.


Then select options such as:

"12"
"012"
"6"
 
 OR use as:

example: "python Voicemail.py m 012.345.6789 12 01234 123456 output.mp3"
		 "python Voicemail.py m 012-345-6789 1 012 32 output.mp3"
		 "python Voicemail.py m (012)345-6789 2 2 6 output.mp3"
		 "python Voicemail.py f 012.345.6789 12 0123456 12 output.mp3"
		 "python Voicemail.py f 012.345.6789 1 023 1 out.mp3"
		 "python Voicemail.py f (012)345.6789 1 035 2 output.mp3"


Gender: m for male and f for female. "male" "Male" & "Female" "female" work too
phone number: as long as 10 digits any format works
Beginning: numbers from 1-2 example "1" "2" "12" works
Reasons: numbers from 0-4 for male and 0-6 for female
Ending: Usage numbers from 1-6 for male and 1-2 for female

Lots of Error checking exists.

If you want to use a menu do not enter any command line arguments.

Note: it is highly recommended to user to input file with '.mp3' extension when prompted for the output file

Note: the actual phone number files is downloaded only if you select '2' in each of the beginning choices for male or female.

Note: File Called sequence.txt created with info of files downloaded
*******************************************************************************************************************************



Note: this has been tested on Mac and Unix systems when run through terminal not on any windows systems

This program uses URL Lib2 to download Mp3 files
This program also uses the Unix System's 'Cat' command to concatenate Mp3 files
This program uses 'rm' to delete files that are not required anymore in the end


