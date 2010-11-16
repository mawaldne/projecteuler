#my $sum = 0;
#for $k (1 .. 999) {
#	if ($k % 3 == 0 or $k % 5 == 0){
#		$sum += $k;
#	}
#}
#print $sum;

for (0..999) { $i+=$_ if (!($_%3) || !($_%5)); } 
print "$i\n";

