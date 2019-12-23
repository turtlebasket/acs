python3 scan.py > scan.log & 
raspivid -o – -t 0 -n | vlc -vvv stream:///dev/stdin –sout ‘#rtp{sdp=rtsp://:8554/}’:demux=h264 &
python3 web.py > web.log
