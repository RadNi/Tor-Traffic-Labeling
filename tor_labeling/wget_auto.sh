rand=`cat /dev/urandom | tr -dc 'a-zA' | fold -w 3 | head -n 1`;

STR="https://www.google.com/search?source=hp&ei=UTgSXNLdHoXzkwX09ofwDQ&q=$rand&btnK=Google+Search&oq=$rand&gs_l=psy-ab.3..35i39l2j0i67l2j0l5j0i10.977.1387..1490...0.0..0.154.564.0j4......0....1..gws-wiz.....0.Vcjaa8oscZs"
echo $STR

wget -r -p -U Mozilla $STR 

