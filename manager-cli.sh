# Login
while true
do
	echo -n "User login: "
	read user
	echo -n "Password: "
	read -s pw # hide user input
	
	# Check stuff here
	# currently a dummy setup 
	if [ $user = "turtlebasket" ] && [ $pw = "yeet" ] ; then
		echo "" # newline
		break
	fi
	echo ; echo "Unrecognized user/password"
done

echo "                _         _____      _    _____ _ _   _            " 
echo "     /\        | |       / ____|    | |  / ____(_) | | |           " 
echo "    /  \  _   _| |_ ___ | |     __ _| |_| (___  _| |_| |_ ___ _ __ " 
echo "   / /\ \| | | | __/ _ \| |    / _\` | __|\\___ \\| | __| __/ _ \\ '__|" 
echo "  / ____ \\ |_| | || (_) | |___| (_| | |_ ____) | | |_| ||  __/ |   " 
echo " /_/    \\_\\__,_|\\__\\___/ \\_____\\__,_|\\__|_____/|_|\__|\\__\\___|_|   "
echo
echo "Logged into control shell. Enter \`help\` for a list of commands."
echo 

while true
do
	echo -n "acs: "
	read input

	if [ $input = "exit" ] || [ $input = "quit" ] || [ $input = "q" ] ; then
		break

	elif [ $input = "help" ] ; then
		echo "=== COMMANDS ==="
		echo "start		Start camera"
		echo "stop		Stop camera"
		echo "state		Get camera's current state"
		echo "exit		Leave the control shell"

	elif [ $input = "state" ] ; then
		echo "Currently $state." 

	elif [ $input = "start" ] ; then
		if [ $state = "running" ] ; then
			echo "Camera is already running."
		else
			echo "Starting camera."
			python3 scan.py
			state="running"
		fi

	elif [ $input = "stop" ] ; then
		echo "Stopping camera..."
		killall scan.py
		state="idle"
		echo "Camera stopped."

	else
		echo "\`$input\` is not a recognized command."

	fi
done
