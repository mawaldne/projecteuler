($sum, $sum2) = (0,0);
for (1..100) { $sum += $_**2; $sum2 += $_;}
print $sum2**2 - $sum;

#Whats going on here?
#perl -e 'map {$x[0]+=$_**2;$x[1]+=$_;}(1..100);print $x[1]**2-$x[0],$/ '
