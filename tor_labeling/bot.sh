i=0;

while [ $i -lt 2 ]
do

sleep 5;
xdotool mousemove 530 1035; xdotool click 1;

sleep 1;
xdotool mousemove 1600 900; xdotool click 1; xdotool key ctrl+c Up Return;

sleep 1;
xdotool mousemove 270 410; xdotool click 1;

sleep 2;

xdotool mousemove 980 530;
xdotool click 1;
sleep 1;
xdotool mousemove 1300 480;
xdotool click 1;
sleep 1;
xdotool mousemove 1800 280;
xdotool click 1;


j=0;
while [ $j -lt 200 ]
do
sleep 0.1;
xdotool key Page_Up;
j=$[$j+1]
done


sleep 1;
xdotool mousemove 980 530;
xdotool click 1;
sleep 1;
xdotool mousemove 1300 380;
xdotool click 1;
sleep 1;
xdotool mousemove 1800 280;
xdotool click 1;

sleep 1;
xdotool mousemove 530 1035; xdotool click 1;


sleep 1;

xdotool mousemove 980 530;
xdotool click 1;
sleep 1;
xdotool mousemove 1300 480;
xdotool click 1;
sleep 1;
xdotool mousemove 1800 280;
xdotool click 1;


j=0;
while [ $j -lt 200 ]
do
sleep 0.1;
xdotool key Page_Up;
j=$[$j+1]
done


sleep 1;
xdotool mousemove 980 530;
xdotool click 1;
sleep 1;
xdotool mousemove 1300 380;
xdotool click 1;
sleep 1;
xdotool mousemove 1800 280;
xdotool click 1;


sleep 1;
xdotool mousemove 270 410; xdotool click 1;

i=$[$i+1]
done
